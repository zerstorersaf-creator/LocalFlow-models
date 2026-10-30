#!/usr/bin/env python3
"""Anonymous catalogue download, interrupted-transfer resume, exact length and SHA-256.

Uses no GitHub token. Data goes to --output outside source git. It verifies the
immutable distribution URLs/pins, including that they return weights rather than
Git LFS pointer files. Android device downloader/lifecycle testing remains separate.
"""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request


def verify_entry(label, filename, url, expected_bytes, expected_sha, output_dir):
    destination = output_dir / filename
    print(f"[{label}] Testing anonymous GET & Range resume for {filename} ({expected_bytes / 1024 / 1024:.1f} MB)...", flush=True)
    
    # Intentionally interrupt a normal unauthenticated GET, then resume.
    with urllib.request.urlopen(url, timeout=120) as response:
        if response.status != 200 or int(response.headers["Content-Length"]) != expected_bytes:
            raise ValueError(f"Wrong full-download response for {url}: status={response.status}, content-length={response.headers.get('Content-Length')}")
        first = response.read(65536)
        
    if len(first) != 65536:
        raise ValueError(f"Insufficient first segment: got {len(first)} bytes")
        
    digest = hashlib.sha256(first)
    count = len(first)
    request = urllib.request.Request(url, headers={"Range": f"bytes={count}-"})
    with urllib.request.urlopen(request, timeout=300) as response, destination.open("wb") as output:
        if response.status != 206 or response.headers.get("Content-Range") != f"bytes {count}-{expected_bytes-1}/{expected_bytes}":
            raise ValueError("Server cannot safely resume a model download")
        output.write(first)
        while block := response.read(1024 * 1024 * 4):
            count += len(block)
            if count > expected_bytes:
                raise ValueError("Server exceeded pinned model size")
            digest.update(block)
            output.write(block)
            
    if count != expected_bytes:
        destination.unlink(missing_ok=True)
        raise ValueError(f"Download size mismatch for {label}: count={count} (expected {expected_bytes})")
        
    if expected_sha is not None and digest.hexdigest().lower() != expected_sha.lower():
        destination.unlink(missing_ok=True)
        raise ValueError(f"Download SHA mismatch for {label}: sha={digest.hexdigest()} (expected {expected_sha})")
        
    print(f"[{label}] Verified anonymous download, resume, and SHA-256 successfully!", flush=True)
    return {
        "url": url,
        "bytes": count,
        "sha256": digest.hexdigest(),
        "anonymous_get": "passed",
        "interrupted_range_resume": "passed"
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--target", choices=["all", "production", "whisper"], default="production",
                        help="Which models to verify (default: production)")
    args = parser.parse_args()
    
    repository = Path(__file__).resolve().parents[1]
    args.output.mkdir(parents=True, exist_ok=True)
    results = {}

    # 1. Verify production-v1 models
    if args.target in ("all", "production"):
        prod_dir = repository / "production-v1"
        if (prod_dir / "models-manifest.json").exists():
            manifest_data = json.loads((prod_dir / "models-manifest.json").read_text(encoding="utf-8"))
            prefix = manifest_data["distribution_prefix"]
            for m in manifest_data["models"]:
                if m.get("distribution_parts"):
                    part_files = []
                    for part in m["distribution_parts"]:
                        p_label = f"{m['id']}-part{part['part']}"
                        p_url = part["distribution_url"]
                        res = verify_entry(p_label, part["filename"], p_url, part["bytes"], part.get("sha256"), args.output)
                        results[p_label] = res
                        part_files.append(args.output / part["filename"])
                        
                    # Test reassembly
                    combined_path = args.output / m["filename"]
                    print(f"[{m['id']}] Reassembling {len(part_files)} parts into {m['filename']}...", flush=True)
                    h_comb = hashlib.sha256()
                    with combined_path.open("wb") as fout:
                        for p_path in part_files:
                            with p_path.open("rb") as fin:
                                while chunk := fin.read(1024 * 1024 * 8):
                                    fout.write(chunk)
                                    h_comb.update(chunk)
                    comb_sha = h_comb.hexdigest()
                    comb_size = combined_path.stat().st_size
                    assert comb_size == m["bytes"], f"Reassembled size mismatch: {comb_size} != {m['bytes']}"
                    assert comb_sha.lower() == m["sha256"].lower(), f"Reassembled SHA mismatch: {comb_sha} != {m['sha256']}"
                    print(f"[{m['id']}] Reassembly verified successfully! SHA-256 matches: {comb_sha}", flush=True)
                    results[m["id"]] = {
                        "filename": m["filename"],
                        "bytes": comb_size,
                        "sha256": comb_sha,
                        "reassembly": "passed"
                    }
                else:
                    url = prefix + m["filename"]
                    res = verify_entry(m["id"], m["filename"], url, m["bytes"], m["sha256"], args.output)
                    results[m["id"]] = res

    # 2. Verify whisper models
    if args.target in ("all", "whisper"):
        whisper_dir = repository / "singapore-whisper-v1"
        if (whisper_dir / "public-download-validation.json").exists():
            published = json.loads((whisper_dir / "public-download-validation.json").read_text(encoding="utf-8"))
            prefix = "https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/"
            for label in ("singlish", "sing2eng"):
                m_path = whisper_dir / f"{label}-manifest.json"
                if m_path.exists():
                    manifest = json.loads(m_path.read_text(encoding="utf-8"))
                    url = published[label]["url"]
                    res = verify_entry(label, manifest["filename"], url, int(manifest["bytes"]), manifest["sha256"], args.output)
                    results[label] = res

    validation_path = args.output / "public-download-validation.json"
    validation_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"\nAll validations passed! Results saved to {validation_path}")


if __name__ == "__main__":
    main()

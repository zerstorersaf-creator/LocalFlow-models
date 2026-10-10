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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    metadata = repository / "singapore-whisper-v1"
    published = json.loads((metadata / "public-download-validation.json").read_text())
    prefix = "https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/"
    entries = []
    for label in ("singlish", "sing2eng"):
        manifest = json.loads((metadata / (label + "-manifest.json")).read_text())
        url = published[label]["url"]
        if url != prefix + manifest["filename"]:
            raise ValueError("Unexpected distribution URL")
        if (published[label]["bytes"], published[label]["sha256"]) != (manifest["bytes"], manifest["sha256"]):
            raise ValueError("Distribution metadata and manifest differ")
        entries.append((label, manifest["filename"], url, manifest["bytes"], manifest["sha256"]))
    args.output.mkdir(parents=True, exist_ok=True)
    results = {}
    for label, filename, url, byte_text, expected_sha in entries:
        expected_bytes = int(byte_text)
        destination = args.output / filename
        # Intentionally interrupt a normal unauthenticated GET, then resume.
        with urllib.request.urlopen(url, timeout=120) as response:
            if response.status != 200 or int(response.headers["Content-Length"]) != expected_bytes:
                raise ValueError("Wrong full-download response")
            first = response.read(65536)
        if len(first) != 65536:
            raise ValueError("Insufficient first segment")
        digest = hashlib.sha256(first)
        count = len(first)
        request = urllib.request.Request(url, headers={"Range": f"bytes={count}-"})
        with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as output:
            if response.status != 206 or response.headers.get("Content-Range") != f"bytes {count}-{expected_bytes-1}/{expected_bytes}":
                raise ValueError("Server cannot safely resume a model download")
            output.write(first)
            while block := response.read(1024 * 1024):
                count += len(block)
                if count > expected_bytes:
                    raise ValueError("Server exceeded pinned model size")
                digest.update(block)
                output.write(block)
        if count != expected_bytes or digest.hexdigest() != expected_sha:
            destination.unlink()
            raise ValueError("Download integrity failed")
        results[label] = dict(url=url, bytes=count, sha256=digest.hexdigest(),
                              anonymous_get="passed", interrupted_range_resume="passed")
        print(label, "anonymous download and resume verified", flush=True)
    (args.output / "public-download-validation.json").write_text(json.dumps(results, indent=2) + "\n")


if __name__ == "__main__":
    main()

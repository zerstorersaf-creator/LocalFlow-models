# LocalFlow Models

Public verified distribution and backup mirror of on-device speech recognition and LLM cleanup models for [LocalFlow](https://github.com/zerstorersaf-creator/LocalFlow).

Download them directly from LocalFlow **Settings → Speech Models & LLM**, or via the direct links below. Downloads require no GitHub account or API token and support HTTP Range resumes.

---

## Production Models (`production-v1`)

| Model | Kind | Runtime | Size | Licence | Direct Download | SHA-256 |
|---|---|---|---|---|---|---|
| **SenseVoice Multilingual** | Speech (ASR) | Sherpa ONNX | 163 MB | Apache-2.0 | [sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2024-07-17.tar.bz2](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2024-07-17.tar.bz2) | `7d1efa2138a65b0b488df37f8b89e3d91a60676e416f515b952358d83dfd347e` |
| **Qwen3 0.6B Disfluency Cleanup** | LLM Polish | llama.cpp | 429 MB | Apache-2.0 | [Qwen3-0.6B-Q4_0.gguf](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-0.6B-Q4_0.gguf) | `da2572f16c06133561ce56accaa822216f2391ef4d37fba427801cd6736417d4` |
| **Qwen3-ASR 0.6B Multilingual** | Speech (ASR) | Sherpa ONNX | 879 MB | Apache-2.0 | [sherpa-onnx-qwen3-asr-0.6B-int8-2026-03-25.tar.bz2](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/sherpa-onnx-qwen3-asr-0.6B-int8-2026-03-25.tar.bz2) | `393f8a14e2f5fb96746aaab342997a40641001fbd5bf9592a080a8329178ee96` |
| **Qwen3 1.7B High-Capacity Polish** | LLM Polish | llama.cpp | 1.06 GB | Apache-2.0 | [Qwen3-1.7B-Q4_0.gguf](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-1.7B-Q4_0.gguf) | `c876f159707a4e4f70e045106c69db15bfc935a4981706fd4f65c6e7ea1e81c5` |
| **Qwen3 4B Long-Form Structuring** | LLM Polish | llama.cpp | 2.38 GB | Apache-2.0 | [Part 1](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-4B-Q4_0.gguf.part1) / [Part 2](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-4B-Q4_0.gguf.part2) | `bd3ca6c0af689d5c396b8a7c7ac121fca58a687cb8b0e71f01e2611ac9358903` |

### Qwen3 4B Split Reassembly

To comply with GitHub Release's 2 GiB per-asset constraint, `Qwen3-4B-Q4_0.gguf` is distributed in two parts:
- **Part 1:** `Qwen3-4B-Q4_0.gguf.part1` (1,258,291,200 bytes)
- **Part 2:** `Qwen3-4B-Q4_0.gguf.part2` (1,117,482,112 bytes)

Reassemble with:
- **Windows (cmd):** `copy /b Qwen3-4B-Q4_0.gguf.part1 + Qwen3-4B-Q4_0.gguf.part2 Qwen3-4B-Q4_0.gguf`
- **Linux / macOS:** `cat Qwen3-4B-Q4_0.gguf.part1 Qwen3-4B-Q4_0.gguf.part2 > Qwen3-4B-Q4_0.gguf`

See [production-v1 metadata and documentation](production-v1/README.md).

---

## Historical Archive: Singapore Whisper v1 (`singapore-whisper-v1`)

| Model | Download | Licence | Language |
| --- | --- | --- | --- |
| Whisper Small Singlish | [Q5_1 model](https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/ggml-small-singlish-q5_1.bin) | Apache-2.0 | English transcription |
| Whisper Small Sing2Eng | [Q5_1 model](https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/ggml-small-sing2eng-q5_1.bin) | MIT | English transcription |

See [singapore-whisper-v1 release notes](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/tag/singapore-whisper-v1),
[checksums](singapore-whisper-v1/SHA256SUMS.txt), and
[source attribution and licences](singapore-whisper-v1/README.md).

---

## Verification & Integrity

Run the automated verification script to validate anonymous downloading, HTTP Range chunked resume, and exact SHA-256 verification:
```bash
python scripts/verify-downloads.py --output /tmp/model-verification
```

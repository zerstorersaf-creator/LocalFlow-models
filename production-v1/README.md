# LocalFlow Production Models (Release production-v1)

Official verified backup and distribution mirror of on-device speech recognition and LLM cleanup models for [LocalFlow](https://github.com/zerstorersaf-creator/LocalFlow).

All models are pinned with exact byte counts and SHA-256 hashes. Downloads require no GitHub account or token and support HTTP Range resume.

---

## Model Catalogue

| Model ID | Name | Kind | Runtime | Size | Licence | Direct Download | SHA-256 |
|---|---|---|---|---|---|---|---|
| `sherpa-zh-en` | SenseVoice Multilingual | Speech (ASR) | Sherpa ONNX | 163 MB (163,002,883 B) | Apache-2.0 | [Download](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2024-07-17.tar.bz2) | `7d1efa2138a65b0b488df37f8b89e3d91a60676e416f515b952358d83dfd347e` |
| `qwen-0.6` | Qwen3 0.6B Disfluency Cleanup | LLM Polish | llama.cpp | 429 MB (428,970,080 B) | Apache-2.0 | [Download](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-0.6B-Q4_0.gguf) | `da2572f16c06133561ce56accaa822216f2391ef4d37fba427801cd6736417d4` |
| `qwen-asr` | Qwen3-ASR 0.6B Multilingual | Speech (ASR) | Sherpa ONNX | 879 MB (878,702,423 B) | Apache-2.0 | [Download](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/sherpa-onnx-qwen3-asr-0.6B-int8-2026-03-25.tar.bz2) | `393f8a14e2f5fb96746aaab342997a40641001fbd5bf9592a080a8329178ee96` |
| `qwen-1.7` | Qwen3 1.7B High-Capacity Polish | LLM Polish | llama.cpp | 1.06 GB (1,056,782,912 B) | Apache-2.0 | [Download](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-1.7B-Q4_0.gguf) | `c876f159707a4e4f70e045106c69db15bfc935a4981706fd4f65c6e7ea1e81c5` |
| `qwen-4` | Qwen3 4B Long-Form Structuring | LLM Polish | llama.cpp | 2.38 GB (2,375,773,312 B) | Apache-2.0 | [Part 1](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-4B-Q4_0.gguf.part1) / [Part 2](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/download/production-v1/Qwen3-4B-Q4_0.gguf.part2) | `bd3ca6c0af689d5c396b8a7c7ac121fca58a687cb8b0e71f01e2611ac9358903` |

---

## Qwen3 4B Split Reassembly

Due to GitHub Release's maximum 2 GiB per-asset constraint, `Qwen3-4B-Q4_0.gguf` (2,375,773,312 bytes) is hosted in two parts:
- `Qwen3-4B-Q4_0.gguf.part1` (1,258,291,200 bytes)
- `Qwen3-4B-Q4_0.gguf.part2` (1,117,482,112 bytes)

To reassemble after downloading both parts into the same folder:

**Windows (cmd):**
```cmd
copy /b Qwen3-4B-Q4_0.gguf.part1 + Qwen3-4B-Q4_0.gguf.part2 Qwen3-4B-Q4_0.gguf
```

**macOS / Linux:**
```bash
cat Qwen3-4B-Q4_0.gguf.part1 Qwen3-4B-Q4_0.gguf.part2 > Qwen3-4B-Q4_0.gguf
```

After reassembly, verify the final file hash matches:
```bash
sha256sum Qwen3-4B-Q4_0.gguf
# bd3ca6c0af689d5c396b8a7c7ac121fca58a687cb8b0e71f01e2611ac9358903
```

---

## Upstream Provenance & Attribution

- **SenseVoice Multilingual (`sherpa-zh-en`):**
  - Upstream project: FunAudioLLM / sherpa-onnx ([k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx))
  - Model release: `sherpa-onnx-sense-voice-zh-en-ja-ko-yue-int8-2024-07-17`
  - License: Apache-2.0
- **Qwen3 Models (`qwen-0.6`, `qwen-1.7`, `qwen-4`):**
  - Upstream project: Qwen Team / Alibaba Cloud
  - Quantized distributions: [ggml-org/Qwen3-0.6B-GGUF](https://huggingface.co/ggml-org/Qwen3-0.6B-GGUF), [unsloth/Qwen3-1.7B-GGUF](https://huggingface.co/unsloth/Qwen3-1.7B-GGUF), [unsloth/Qwen3-4B-GGUF](https://huggingface.co/unsloth/Qwen3-4B-GGUF)
  - License: Apache-2.0
- **Qwen3-ASR (`qwen-asr`):**
  - Upstream project: Qwen Team / sherpa-onnx ([k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx))
  - Model release: `sherpa-onnx-qwen3-asr-0.6B-int8-2026-03-25`
  - License: Apache-2.0

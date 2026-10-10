# Experimental Singapore-trained Whisper Small mobile models

Only licensed public model metadata and Git LFS weights live here; no app code or private user recordings/transcripts.

- Singlish: mjwong/whisper-small-singlish, revision 048604a6731fa71b08895a3dd13fb12436381824; Ming Jie Wong; Apache-2.0.
- Sing2Eng transcription: ivabojic/whisper-small-sing2eng-transcribe, revision 0835ed29d2f8893e4fcf63d5ac531dcb086b6ee1; MIT declared by model card.
- Both derive from OpenAI Whisper Small (MIT, Copyright (c) 2022 OpenAI). Full notices/cards accompany these modified weights.

Conversion uses whisper.cpp v1.9.4 / 927cfce34f31707e17f2bff35c349632fb9e2c3a, torch 2.6.0+cpu, transformers 4.48.3, numpy 2.2.6. The pinned HF converter was reviewed to preserve original FP32 small tensors and decoder architecture context 448. Larger tensors are FP16, then quantized with whisper-quantize q5_1. Both exact 479-tensor/tokenizer/mel audits and original/FP16/Q5_1 synthetic CPU inference completed. Not device-validated or an accuracy benchmark.

Use English transcription, not translation. Synthetic tests did not preserve Mandarin/code-switch content and some names were incorrect even in original checkpoints. No claim of Mandarin accuracy, real Singapore-accent quality or Samsung performance. Optional experimental comparison only.

Each mobile file is 190,085,504 bytes. Checksums and immutable source provenance are in manifests and SHA256SUMS.txt. Verify exact length/SHA-256. Both anonymous GET and interrupted Range-resume checks passed. Git stores pointers; LFS serves the weights. Future weights require a new pinned version.

## Immutable downloads

- [ggml-small-singlish-q5_1.bin](https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/ggml-small-singlish-q5_1.bin)
- [ggml-small-sing2eng-q5_1.bin](https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/ggml-small-sing2eng-q5_1.bin)

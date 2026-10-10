# LocalFlow models

Public distribution of licensed experimental speech models used by LocalFlow.
Download them from LocalFlow **Settings → Speech models**, or use the links below.
Each file is about 190 MB. Downloads require no GitHub account or token.

| Model | Download | Licence | Language |
| --- | --- | --- | --- |
| Whisper Small Singlish | [Q5_1 model](https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/ggml-small-singlish-q5_1.bin) | Apache-2.0 | English transcription |
| Whisper Small Sing2Eng | [Q5_1 model](https://media.githubusercontent.com/media/zerstorersaf-creator/LocalFlow-models/42e671ab1f8eda09cf59ad1ef34bfb354ad65b7a/weights/singapore-whisper-v1/ggml-small-sing2eng-q5_1.bin) | MIT | English transcription |

These are opt-in trials. Synthetic conversion tests passed, but Singapore-accent
accuracy, Mandarin/code-switch support and Samsung performance are unvalidated.

See [release notes](https://github.com/zerstorersaf-creator/LocalFlow-models/releases/tag/singapore-whisper-v1),
[checksums](singapore-whisper-v1/SHA256SUMS.txt), and
[source attribution, licences and conversion provenance](singapore-whisper-v1/README.md).
Always verify exact size and SHA-256. The download links pin an immutable commit.

## Repository maintenance

Git stores small LFS pointers; Git LFS stores the weights. The Raw button can
return a pointer, so use the links above for direct downloads. LocalFlow contains
no bundled weights and sends no audio or transcripts here.

For a local copy including weights, install Git LFS and run `git lfs install`,
then clone this repository and run `git lfs pull`.

The **Verify public model downloads** workflow checks anonymous downloads,
interrupted-transfer resume, byte lengths and hashes. It uses no signing or
private app credentials. Run it manually after changing hosting configuration.

To publish new weights, review their licence and source revision, upload with
Git LFS, record immutable URLs and exact hashes, then validate before updating
LocalFlow. Preserve existing pinned commits for installed app versions.

See [owner settings](REPOSITORY-SETUP.md) for repository settings requiring admin access.

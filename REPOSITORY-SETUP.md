# Models-only repository settings

Public visibility, default branch main, Git LFS weights and a public experimental
release are configured. Both immutable download URLs pass anonymous size/hash
and interrupted-resume checks. No credentials are required by consumers.

The GitHub integration cannot edit repository administration settings (HTTP 403).
An owner can set the following in Settings and the About panel:

- Description: Licensed experimental Singapore-trained Whisper models for LocalFlow, with immutable downloads and verified checksums.
- Website: https://github.com/zerstorersaf-creator/LocalFlow-models/releases/tag/singapore-whisper-v1
- Topics: localflow, whisper, speech-recognition, singlish.
- Disable the unused wiki; keep Issues available for model-download reports.
- Keep Actions enabled with read-only default token permissions. The download
  verification workflow explicitly requests contents: read and needs no secrets.

This repository distributes models and their verification metadata. App source,
APKs, signing backups and user recordings/transcripts belong elsewhere.

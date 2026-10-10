---
library_name: transformers
tags:
- automatic-speech-recognition
- whisper
- speech
- transcription
- singlish
license: mit
datasets:
- singapore-national-speech-corpus
language:
- en
metrics:
- wer
base_model:
- openai/whisper-small
---

# Whisper-small Singlish2English transcription model

[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model-blue)](https://huggingface.co/ivabojic/whisper-small-sing2eng-transcribe)

## Model overview

This model is a fine-tuned version of [`openai/whisper-small`](https://huggingface.co/openai/whisper-small), trained on over **2 million speech samples** from the [Singapore National Speech Corpus (NSC)](https://www.imda.gov.sg/how-we-can-help/national-speech-corpus). It focuses on **Singaporean-accented English** (Singlish), which are typically underrepresented in general-purpose ASR systems.

---

## Custom dataset overview

To enable fine-tuning of open-source foundation ASR models, we curated **NSC<sub>P16</sub>** bespoke dataset constructed from the NSC corpus. It is designed to capture the range and richness of Singlish across both non-conversational and conversational contexts.

- **Non-conversational speech** includes:
  - **Part 1:** Phonetically-balanced scripts consisting of standard English sentences spoken in local accents.
  - **Part 2:** Sentences randomly generated from themes such as people, food, places, and brands.

- **Conversational and expressive speech** includes:
  - **Part 3:** Natural dialogues on everyday topics between Singaporean speakers.
  - **Part 5:** Stylized recordings simulating debates, finance-related discussions, and emotional expressions (both positive and negative).
  - **Part 6:** Scenario-based dialogues, where speakers engage in topic-driven, semi-scripted interactions covering various themes.

Together, these components make NSC<sub>P16</sub> a robust dataset for building speech models that generalize well across local speech styles, tones, and speaking conditions.

**Table 1: Overview of the custom-created transcription datasets.**

| **Name**        | **Samples** | **Total hours** | **Avg. duration (s)** | **Min (s)** | **Max (s)** |
|------------------|-------------|------------------|------------------------|-------------|-------------|
| NSC<sub>P16_train</sub>    | 2,048,000   | 2944.1           | 5.2                    | 0.1         | 30.1        |
| NSC<sub>P16_valid</sub>    | 50,000      | 73.4             | 5.3                    | 0.8         | 29.1        |
| NSC<sub>P16_test</sub>     | 10,000      | 19.1             | 6.9                    | 1.0         | 26.1        |

## Evaluation

Evaluation was conducted on the held-out NSC<sub>P16</sub> dataset. Performance was measured using **Word Error Rate (WER)**, comparing the fine-tuned model against the off-the-shelf Whisper-small baseline.

**Table 2: Evaluation results on the test dataset using WER. A lower WER indicates better performance (↓).**

| Model                              | WER (↓) |
|-----------------------------------|---------|
| Whisper-small (off-the-shelf)    | 23.64   |
| Whisper-small-Sing2Eng (fine-tuned) | **7.14** |

This represents a **16.50 percentage point absolute reduction** and a **69.8% relative improvement** in WER over the baseline Whisper-small model on the NSC<sub>P16</sub> test set. 

By learning from diverse local accents and speaking styles, this model significantly improves transcription accuracy for Singaporean speech, making it suitable for both research and production applications in **multilingual** and **code-switched** environments.

## Usage

```python
import torchaudio, torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration

model_name = 'ivabojic/whisper-small-sing2eng-transcribe'
audio_path = 'path_to_audio'  # e.g: https://github.com/IvaBojic/Singlish2English/blob/main/small_dataset/audios/00862042_713.wav

# Load model and processor
model = WhisperForConditionalGeneration.from_pretrained(model_name)
processor = WhisperProcessor.from_pretrained(model_name)

# Load and resample audio if needed
audio, sr = torchaudio.load(audio_path)
if sr != 16000:
    resampler = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)
    audio = resampler(audio)
audio = audio.squeeze().numpy()

# Preprocess and generate transcription
inputs = processor(audio=audio, sampling_rate=16000, return_tensors="pt")

with torch.no_grad():
    predicted_ids = model.generate(inputs.input_features)

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
print(transcription)
```

## Project repository

For training scripts, evaluation tools, sample audio files, and more, visit the GitHub repository: 
[https://github.com/IvaBojic/Singlish2English](https://github.com/IvaBojic/Singlish2English)
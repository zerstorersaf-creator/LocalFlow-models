---
base_model:
- openai/whisper-small
language:
- en
metrics:
- wer
pipeline_tag: automatic-speech-recognition
license: apache-2.0
library_name: transformers
model-index:
- name: whisper-small-singlish
  results:
  - task:
      type: automatic-speech-recognition
    dataset:
      name: SASRBench-v1
      type: mjwong/SASRBench-v1
      split: test
    metrics:
      - name: WER
        type: WER
        value: 18.49
- name: whisper-small-singlish
  results:
  - task:
      type: automatic-speech-recognition
    dataset:
      name: AMI
      type: edinburghcstr/ami
      subset: ihm
      split: test
    metrics:
      - name: WER
        type: WER
        value: 30.85
- name: whisper-small-singlish
  results:
  - task:
      type: automatic-speech-recognition
    dataset:
      name: GigaSpeech
      type: speechcolab/gigaspeech
      subset: test
      split: test
    metrics:
      - name: WER
        type: WER
        value: 16.02
tags:
- whisper
---
# Whisper small-singlish

**Whisper small-singlish** is a fine-tuned automatic speech recognition (ASR) model optimized for Singlish. Built on OpenAI's Whisper model, it has been adapted using Singlish-specific data to accurately capture the unique phonetic and lexical nuances of Singlish speech.

## Model Details

- **Developed by:** Ming Jie Wong
- **Base Model:** [openai/whisper-small](https://huggingface.co/openai/whisper-small)
- **Model Type:** Encoder-decoder
- **Metrics:** Word Error Rate (WER)
- **Languages Supported:** English (with a focus on Singlish)
- **License:** Apache-2.0

### Description
Whisper small-singlish is developed using an internal dataset of 66.9k audio-transcript pairs. The dataset is derived exclusively from the Part 3 Same Room Environment Close-talk Mic recordings of [IMDA's NSC Corpus](https://www.imda.gov.sg/how-we-can-help/national-speech-corpus). 

The original Part 3 of the National Speech Corpus comprises approximately 1,000 hours of conversational speech from around 1,000 local English speakers, recorded in pairs. These conversations cover everyday topics and include interactive game-based dialogues. Recordings were conducted in two environments:
- Same Room, where speakers shared a room and were recorded using a close-talk mic and a boundary mic.
- Separate Room, where each speaker was recorded individually using a standing mic and a telephone (IVR).

Audio segments for the internal dataset were extracted using these criteria:
- **Minimum Word Count:** 10 words
  
  _This threshold was chosen to ensure that each audio segment contains sufficient linguistic context for the model to better understand instructions in Singlish. Shorter segments may bias the model towards specific utterances or phrases, limiting its overall comprehension._
- **Maximum Duration:** 20 seconds

  _This threshold was chosen to provide enough context for accurate transcription while minimizing noise and computational complexity for longer audio segments._
- **Sampling Rate**: All audio segments are down-sampled to 16kHz.

Full experiments details will be added soon.

### Fine-Tuning Details
We applied fine-tuning on a single A100-80GB GPU.

#### Training Hyperparameters
The following hyperparameters are used:
- **batch_size**: 64
- **gradient_accumulation_steps**: 1
- **learning_rate**: 1e-6
- **warmup_steps**: 300
- **max_steps**: 5000
- **fp16**: true
- **eval_batch_size**: 16
- **eval_step**: 300
- **max_grad_norm**: 1.0
- **generation_max_length**: 225

#### Training Results
The table below summarizes the model’s progress across various training steps, showing the training loss, evaluation loss, and Word Error Rate (WER).

| Steps | Train Loss | Eval Loss | WER                |
|:-----:|:----------:|:---------:|:------------------:|
| 300   | 1.4347	 | 0.6711    | 30.840211          |
| 600   | 0.6508     | 0.5130    | 22.538497          |
| 900   | 0.4950     | 0.3556    | 18.816530          |
| 1200  | 0.3862     | 0.3452    | 17.253038          |
| 1500  | 0.3859     | 0.3391    | 17.947677          |
| 1800  | 0.4018     | 0.3345    | 16.759187          |
| 2100  | 0.3887     | 0.3314    | 16.242452          |
| 2400  | 0.3730     | 0.3292    | 15.687331          |
| 2700  | 0.3628     | 0.3277    | 15.857115          |
| 3000  | 0.3439     | 0.3230    | 15.750816          |
| 3300  | 0.3806     | 0.3247    | 15.223008          |
| 3600  | 0.3495     | 0.3239    | 15.361788          |
| 3900  | 0.3424     | 0.3233    | 15.544122          |
| 4200  | 0.3583     | 0.3223    | 15.279849          |
| 4500  | 0.3409     | 0.3222    | 15.590628          |
| 4800  | 0.3431     | 0.3220    | 15.286493          |

The final checkpoint is taken from the model that achieved the lowest WER score during the 4800 steps.

### Benchmark Performance
We evaluated Whisper small-singlish on [SASRBench-v1](https://huggingface.co/datasets/mjwong/SASRBench-v1), a benchmark dataset for evaluating ASR performance on Singlish:
| Model                                                                                                  | WER     |
|:------------------------------------------------------------------------------------------------------:|:-------:|
| [openai/whisper-small](https://huggingface.co/openai/whisper-small)                                    | 147.80% |
| [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3)                              | 103.41% |
| [jensenlwt/fine-tuned-122k-whisper-small](https://huggingface.co/jensenlwt/whisper-small-singlish-122k)| 68.79%  |
| [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)                  | 27.58%  |
| [mjwong/whisper-small-singlish](https://huggingface.co/mjwong/whisper-small-singlish)                  | 18.49%  |
| [mjwong/whisper-large-v3-singlish](https://huggingface.co/mjwong/whisper-large-v3-singlish)            | 16.41%  |
| [mjwong/whisper-large-v3-turbo-singlish](https://huggingface.co/mjwong/whisper-large-v3-turbo-singlish)| 13.35%  |

## Disclaimer
While this model has been fine-tuned to better recognize Singlish, users may experience inaccuracies, biases, or unexpected outputs, particularly in challenging audio conditions or with speakers using non-standard variations. Use of this model is at your own risk; the developers and distributors are not liable for any consequences arising from its use. Please validate results before deploying in any sensitive or production environment.

## How to use the model
The model can be loaded with the `automatic-speech-recognition` pipeline like so:

```python
from transformers import pipeline
model = "mjwong/whisper-small-singlish"
pipe = pipeline("automatic-speech-recognition", model)
```

You can then use this pipeline to transcribe audios of arbitrary length.

```python
from datasets import load_dataset
dataset = load_dataset("mjwong/SASRBench-v1", split="test")
sample = dataset[0]["audio"]

result = pipe(sample)
print(result["text"])
```

## Contact
For more information, please reach out to mingjwong@hotmail.com.

## Acknowledgements 
1. https://www.jensenlwt.com/blog/singlish-whisper-finetuning-asr-for-singapore-unique-english
2. https://github.com/huggingface/community-events/blob/main/whisper-fine-tuning-event/README.md
3. https://medium.com/htx-dsai/finetuning-whisper-for-the-singaporean-home-team-context-a3ae1a6ae809
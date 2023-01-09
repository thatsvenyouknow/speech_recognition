from transformers import *
import torch
import soundfile as sf
import torchaudio

def init_wav2vec2(model_name = "facebook/wav2vec2-large-960h-lv60-self"):
    """
    model: pretrained model to use (default: 1.18GB facebook model)
    """
    setup = {"processor": Wav2Vec2Processor.from_pretrained(model_name),
             "model": Wav2Vec2ForCTC.from_pretrained(model_name)}
    return setup

def run_wav2vec2(file_path, setup):
    audio, sr = torchaudio.load(file_path)
    audio = audio.squeeze()

    #resample sampling rate to 16000 (to work with pretrained model)
    resampler = torchaudio.transforms.Resample(sr, 16000)
    audio = resampler(audio)

    #tokenize wav
    input_values = setup["processor"](audio, return_tensors="pt", sampling_rate=16000)["input_values"]

    #perform inference
    logits = setup["model"](input_values)["logits"]

    #use argmax to get the predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)

    #decode the IDs to text and save in words container
    transcription = setup["processor"].decode(predicted_ids[0])
    output = transcription.lower()
    return output
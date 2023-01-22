from transformers import *
import torch
import soundfile as sf
import torchaudio
import time

def init_wav2vec2(model_name = "facebook/wav2vec2-large-960h-lv60-self"):
    """
    model_name: pretrained model to use (default: 1.18GB facebook model)
                alternatively: facebook/wav2vec2-large-robust-ft-libri-960h
    """
    setup = {"processor": Wav2Vec2Processor.from_pretrained(model_name),
             "model": Wav2Vec2ForCTC.from_pretrained(model_name),
             "resampler": torchaudio.transforms.Resample(44100, 16000)}
    return setup

def run_wav2vec2(file_path, setup):
    """
    file_path: path to audio file
    setup: dictionary from init_wav2vec2
    """
    audio, _ = torchaudio.load(file_path)
    audio = audio.squeeze()

    #resample sampling rate to 16000 (to work with pretrained model)
    audio = setup["resampler"](audio)

    #tokenize wav + start timing model
    start = time.time()
    input_values = setup["processor"](audio, return_tensors="pt", sampling_rate=16000)["input_values"]

    #perform inference 
    logits = setup["model"](input_values)["logits"]

    #use argmax to get the predicted IDs
    predicted_ids = torch.argmax(logits, dim=-1)

    #decode the IDs to text and save in words container
    transcription = setup["processor"].decode(predicted_ids[0])
    model_time = time.time() - start  
    output = transcription.lower()
    return output, model_time
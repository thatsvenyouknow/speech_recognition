import json
import os
from scipy.io import wavfile
from tqdm import tqdm
from vosk import Model, KaldiRecognizer

def init_vosk(model_path = "vosk-model-en-us-0.42-gigaspeech", sample_rate = 44100):
    assert os.path.exists(model_path), "model not in current path"
    load_model = Model(model_path)
    setup = {"model": KaldiRecognizer(load_model, sample_rate)}
    setup["model"].SetWords(True)
    return setup

def run_vosk(file_path, setup, n_frames = 4000, thresh = 0):
    output = ""
    #confs = [] #in case confidence values for each detected word are desired

    with open(file_path, "rb") as f:
        audio = f.read()
    audio_bytes = bytes(bytearray(audio))

    #Run Speech Recognizer
    i = 0
    while True:
        data = audio_bytes[n_frames*i:n_frames*(i+1)]
        i += 1

        if data == b"": #if indexing is out of range
            break

        if setup["model"].AcceptWaveform(data):
            try: #if section does not contain a word, we get KeyError
                instance = json.loads(setup["model"].Result())
                #if min. confidence, append detected words to lists
                for entry in instance["result"]:
                    if entry["conf"] > thresh:
                        #confs.append(entry["conf"])
                        output += entry["word"]
                        output += " "

            except KeyError:
                continue

    #last detected word is not in model.Result(), therefore...
    last_instance = json.loads(setup["model"].FinalResult())
    for entry in last_instance["result"]:
        if entry["conf"] > thresh:
            #confs.append(entry["conf"])
            output += entry["word"]
    return output
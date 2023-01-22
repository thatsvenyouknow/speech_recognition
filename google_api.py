import os
import time
from google.cloud import speech

def init_google(model = "default", key = "google_key.json"):
    """
    model: "default", "video", "command_and_search"
    key: path to Google Service key [json]
    Note: Cloud Speech-to-Text API needs to be enabled in your account!
    """
    assert os.path.exists(key), "path to key does not exist"

    #Note: for non-wav (or non-flac) files, an encoding parameter must be passed to config
    setup = {"client": speech.SpeechClient.from_service_account_file(key),
             "config": speech.RecognitionConfig(
                    sample_rate_hertz = 44100,
                    language_code = "en-US",
                    model = model
                    )
            }
    return setup

def run_google(file_path, setup):
    """
    file_path: path to audio file
    setup: dictionary from init_google
    """
    with open(file_path, "rb") as f:
        audio = f.read()
        start = time.time()
        audio_file = speech.RecognitionAudio(content = audio)
        response = setup["client"].recognize(
            config = setup["config"],
            audio = audio_file
        )
        try:
            output = response.results[0].alternatives[0].transcript
            model_time = time.time() - start
        except IndexError:
            output = " "
            model_time = time.time() - start   
    return output, model_time
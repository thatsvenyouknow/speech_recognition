from tqdm import tqdm
import whisper

def init_whisper(mode = "base"):
        """
        mode: "tiny", "base", "small", "medium", "large"
        """
        #CUDA_LAUNCH_BLOCKING=1
        setup = {"model": whisper.load_model(mode)}
        return setup

def run_whisper(file_path, setup):
    """
    Note: Internally, the transcribe() method reads the entire file and processes the audio 
        with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions 
        on each window.
    """
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio) #pad/trim to fit 30 seconds
    output = setup["model"].transcribe(audio)["text"]
    return output
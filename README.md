# speech_recognition



## About
This repo contains the recordings of 10 exemplary robot commands, spoken by 13 different persons, which were obtained in noisy environments. The goal of the project is to establish which of the speech-to-text models performs best with the selected sentences.

## Getting Started
Some of the models require additional instructions on how to make them work, which is listed in the following.

### Whisper
[Whisper](https://github.com/openai/whisper) is a general-purpose speech recognition model. Besides installing whisper, one also needs to install Pytorch 3.7+, and the command-line tool ffmpeg. Instructions can be found under the provided link. Whisper offers several model sizes (tiny, base, small, medium, large), the usage of which may depend on your system. The init_whisper function of the speech_to_text class allows to choose which model shall be used. 

### Vosk (Kaldi)
In order to run the Vosk model, one needs to download one of the available models [here](https://alphacephei.com/vosk/models) and put the model into the current path for it to be loaded. For the model comparison, the "vosk-model-en-us-0.42-gigaspeech" was used which contains a generic US English model trained by Kaldi on Gigaspeech and is the largest available English model to use with Vosk. 

### Google Cloud Speech to Text
The [Google Cloud Speech to Text API](https://cloud.google.com/speech-to-text) is an on-demand cloud service. Only 60 minutes of audio per month (+300$ free credits upon creating a new account) are free and afterwards the service costs 0.015-0.07€ per minute audio, depending on which underlying model is used. For that a service account needs to be created ([website](https://console.cloud.google.com)), including billing information to confirm that you are a real person. Of the several models that are offered, three will be used in the comparison:

- default: advised for audios that contain a single speaker. Ideally, the audio is high-fidelity, recorded at 16,000Hz or greater sampling rate.
- video: often the best choice for audio that was recorded with a high-quality microphone or that has lots of background noise. For best results, provide audio recorded at 16,000Hz or greater sampling rate. This is a premium model and therefore costs more than the standard rate
- command_and_search: Used for transcribing shorter audio clips, like voice commands. 

A description of the models can be found [here](https://cloud.google.com/speech-to-text/docs/speech-to-text-requests) under "model selection".

To get started, there are good tutorials on the webpage. The short-version is as follows:
1. Create Project: After logging into your created account on the google cloud website above (and handling your billing information), create a new project.
2. Create Service Account: In the settings (top left), maneouver to APIs & Services - Credentials - Create Credentials to create a "Service Account" (choose a name and grant this service account access as "owner" - click Done)
3. Create Key: Now that the service account is created, click on the created account under "Service Accounts" and go to "Keys". Hit the "Add Key"-button and create the json key, which will be downloaded automatically. Save the downloaded key in your project folder (e.g. as "google_key.json"), as we will need to load the key in python to process audio files.
4. Enable API: Search for "Cloud Speech to Text" on the Google Cloud Platform to get to the API. Enable the API. 
5. After installing in your python env (pip install --upgrade google-cloud-speech), the code should run.

Note: Performance may be approved by using [model adaptation](https://cloud.google.com/speech-to-text/docs/adaptation-model) which helps the algorithm to detect frequently expected words. This option is not used in the comparison.

### Wav2Vec 2.0
[Wav2Vec 2.0](https://github.com/facebookresearch/fairseq/blob/main/examples/wav2vec/README.md) is an ASR model that uses unsupervised pretraining before fine-tuning the model with supervised learning. The model requires the transformers, soundfile, pytroch and torchaudio library which have to be installed and imported before running the model. 

### Help
In case something remains unclear, please do not hesitate to contact me by mail: sven.guenther@tum.de

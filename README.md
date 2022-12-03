# speech_recognition



## About
This repo contains the recordings of 10 exemplary robot commands which were obtained in noisy environments. The goal of the project is to establish which of the speech-to-text models performs best with selected sentences.

## Getting Started
Some of the models require additional instructions on how to make them work, which is listed in the following.

### Vosk (Kaldi)
In order to run the Vosk model, one needs to download one of the available models [here](https://alphacephei.com/vosk/models) and put the model into the current path for it to be loaded. For the model comparison, the "vosk-model-en-us-0.42-gigaspeech" was used which contains a generic US English model trained by Kaldi on Gigaspeech and is the largest available English model to use with Vosk. 

### Whisper
[Whisper](https://github.com/openai/whisper) is a general-purpose speech recognition model. Besides installing whisper, one also needs to install the command-line tool ffmpeg. Instructions can be found under the provided link. Whisper offers several model sizes (tiny, base, small, medium, large), the usage of which may depend on your system. The init_whisper function of the speech_to_text class allows to choose which model shall be used. 

### Next

'''
This script loads the whisper model files into directory. How to run this script:
    python .\WhisperModelLoad.py

The model files are located in the following directory:
    C:\Users\user\.cache\whisper

whisper github:
    https://github.com/openai/whisper
'''
import whisper
whisper.load_model("tiny")
whisper.load_model("medium")
# whisper.load_model("large-v3")
# 功能
Convert audio files (`.wav`, `*.mp3`, `*.m4a`, `*.mp4`) into Chinese text using Whisper + inaSpeechSegmenter.

# 執行
python TalkToText.py

備註：不需要特別執行WhisperModelLoad.py，程式也會自動下載whisper model至whisper/asset

# pip
python -m pip install --upgrade pip

pip install whisper inaSpeechSegmenter moviepy==1.0.3 python-docx tkinter

# 中文語音轉文字模型
## Whisper
Whisper 是 OpenAI 開發的一款 自動語音識別 (ASR, Automatic Speech Recognition) 模型，能夠將音訊轉換為文字。它基於深度學習技術，主要使用 Transformer 架構，並通過大量的多語言和多種音訊數據進行訓練。
### 主要功能
1. 語音轉文字 (Speech-to-Text, STT)
支援多語言語音轉錄（如英語、中文、日語、法語等）。
能處理不同音質、口音和背景噪音。
2. 語言識別
可以自動檢測音訊的語言，然後進行轉錄。
3. 時間戳記 (Timestamps)
產生帶有時間標記的字幕，使其適合用於影片字幕或語音分析應用。
4. 翻譯 (Speech Translation)
可將語音轉錄成英文字幕，適用於跨語言應用場景。

# 講者分離模型(Speaker Diarization)
## inaSpeechSegmenter
inaSpeechSegmenter 是一個用於 音訊分割 (speech segmentation) 和 語音類別識別 的 Python 套件，由 INA (Institut National de l'Audiovisuel) 開發。
### 主要功能
1. 語音區段分割
可以將音訊檔案中的 語音、音樂、靜音 進行區分。
2. 說話人識別 (Speaker Diarization)
可區分不同的說話者，標記誰在說話（但不提供具體身分）。
3. 性別分類
針對語音部分，能識別出該說話者的性別（男性或女性）。


備註：解說內容主要由GPT4o生成

---
# Execution
Run the following command:

python TalkToText.py

Note: There is no need to manually run `WhisperModelLoad.py`, as the program will automatically download the Whisper model to `whisper/asset`.

# pip Installation
python -m pip install --upgrade pip

pip install whisper inaSpeechSegmenter moviepy==1.0.3 python-docx tkinter

# Chinese Speech-to-Text Model
## Whisper
Whisper is an Automatic Speech Recognition (ASR) model developed by OpenAI that converts audio into text. It is based on deep learning techniques, primarily using a Transformer architecture, and has been trained on a large dataset containing multiple languages and various types of audio data.

### Key Features
1. Speech-to-Text (STT)
Supports multilingual speech transcription, including English, Chinese, Japanese, French, and more.
Capable of handling different audio qualities, accents, and background noise.
2. Language Identification
Automatically detects the language of the audio before transcription.
3. Timestamps
Generates subtitles with timestamps, making it suitable for video subtitles and speech analysis applications.
4. Speech Translation
Can transcribe speech into English subtitles, making it useful for cross-language applications.

# Speaker Diarization Model
## inaSpeechSegmenter
inaSpeechSegmenter is a Python package for speech segmentation and speaker classification, developed by INA (Institut National de l'Audiovisuel).

### Key Features
1. Speech Segmentation
Can separate speech, music, and silence in an audio file.
2. Speaker Diarization
Differentiates between multiple speakers and labels who is speaking (without providing specific identities).
3. Gender Classification
Identifies the gender (male or female) of the speaker in speech segments.

Note: The explanation content is generated by GPT-4o.

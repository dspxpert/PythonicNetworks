#!/usr/bin/python3
# pip install gTTS pydub textblob
# need ffmpeg and ffprobe, install ffmpeg from https://www.gyan.dev/ffmpeg/builds/
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
#from textblob import TextBlob
from langdetect import detect
import sys

def ttsPlay(message, lang='auto', display=True):
    message = message.strip()
    if message=='':
        return
    if display==True:
        print(message)
    if lang=='auto':
        #lang = TextBlob(message).detect_language()
        lang = detect(message)
    tts = gTTS(message, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    song = AudioSegment.from_file(fp, format="mp3")
    play(song)

def filePlay(argv):
    for file in argv:
        with open(file, "r") as fp:
            for line in fp:
                ttsPlay(line)
                
if __name__ == "__main__":
    if len(sys.argv) < 2:   # without argument, display usage and play demo
        print('ttsPlay.py [files_to_read]')
        ttsPlay('Thank you.', 'en')
        ttsPlay('감사합니다.', 'ko')
    else:
        filePlay(sys.argv[1:])

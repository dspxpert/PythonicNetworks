#!/usr/bin/python3
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def ttsPlay(message, lang='en', Display=True):
    if Display==True:
        print(message)
    tts = gTTS(message, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    song = AudioSegment.from_file(fp, format="mp3")
    play(song)

if __name__ == "__main__":
    ttsPlay('Thank you.')
    ttsPlay('감사합니다.', 'ko')

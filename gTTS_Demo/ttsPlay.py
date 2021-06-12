#!/usr/bin/python3

import vlc
import time
from gtts import gTTS
from mutagen.mp3 import MP3

def ttsPlay(message, lang='en', display=True, Speed=1.0):
    ttsfile = 'last_tts.mp3'
    media_player = vlc.MediaPlayer()

    tts = gTTS(message, lang=lang)
    tts.save(ttsfile)

    media_length = MP3(ttsfile).info.length + 0.1*Speed
    if display==True:
        print(f"{message} : {media_length:0.2f}sec.")

    media = vlc.Media(ttsfile)
    media_player.set_media(media)
    media_player.set_rate(Speed)
    media_player.play()
    time.sleep(media_length/Speed)

if __name__ == "__main__":
    #for i in range(0, 101, 20):
    #    ttsPlay(f'The Progress is {i}%')
    #ttsPlay('The test has completed.')
    ttsPlay('Thank you.')
    ttsPlay('감사합니다.', 'ko')

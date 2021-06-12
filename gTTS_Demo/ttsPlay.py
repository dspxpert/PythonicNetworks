#!/usr/local/bin/python3
# https://wikidocs.net/15213
# https://wikidocs.net/15214

import vlc
import time
from gtts import gTTS
from mutagen.mp3 import MP3

def ttsPlay(message, lang='en', display=True):
    ttsfile = 'ttsplay.mp3'
    media_player = vlc.MediaPlayer()

    tts = gTTS(message, lang=lang)
    tts.save(ttsfile)

    media_length = MP3(ttsfile).info.length + 0.1
    if display==True:
        print(f"{message} : {media_length:0.2f}sec.")

    media = vlc.Media(ttsfile)
    media_player.set_media(media)
    media_player.play()
    time.sleep(media_length)

if __name__ == "__main__":
    #for i in range(0, 101, 20):
    #    ttsPlay(f'The Progress is {i}%')
    ttsPlay(f'The test has completed. Thank you.')
    ttsPlay('감사합니다.', 'ko')
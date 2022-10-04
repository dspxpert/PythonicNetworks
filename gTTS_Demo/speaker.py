# Required library
# pip install SpeechRecognition

import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from langdetect import detect
import time

# Speech Recognition(Listen)
def listen(recognizer, audio):
    try:
        text = r.recognize_google(audio, language='ko')
        print(f'[YOU] {text}')
        answer(text)
    except sr.UnknownValueError:
        print('Recognition failed')
    except sr.RequestError as e:
        print(f'Request failed : {e}') # API key error, Network problem

# Answer
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘 서울의 기온은 20도 입니다. 맑은 하늘이 예상됩니다.'
    elif '환율' in input_text:
        answer_text = '오늘의 원 달러 환율은 1400원 입니다.'
    elif '고마워' in input_text:
        answer_text = '천만에요.'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요.'
        stop_listening(wait_for_stop = False)
    else:
        answer_text = '다시 한 번 말씀해 주세요.'
    speak(answer_text)

# Text to Speech
def speak(text):
    text = text.strip()
    if text=='':
        return
    
    print(f'[AI ] {text}')
    lang = detect(text)
    tts = gTTS(text, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    song = AudioSegment.from_file(fp, format="mp3")
    play(song)    

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
#stop_listening(wait_for_stop = False) # to Stop Recognition

while True:
    time.sleep(0.1)

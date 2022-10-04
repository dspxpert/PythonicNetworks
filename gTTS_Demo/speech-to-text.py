# Required library
# pip install SpeechRecognition

import speech_recognition as sr

# Listen from Microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Listening...')
    audio = r.listen(source)

# Listen from File(wav, aiff/aiff-c, flac), not mp3
r = sr.Recognizer()
with sr.AudioFile('sample.wav') as source:
    print('Listening...')
    audio = r.record(source)

try:
    # Using Google API, Limit 50 times/day
    text = r.recognize_google(audio, language='en-US')
    print(text)
    
    # 한글인식
    text = r.recognize_google(audio, language='ko')
    print(text)
    
except sr.UnknownValueError:
    print('Recognition failed')
except sr.RequestError as e:
    print(f'Request failed : {e}') # API key error, Network problem

import ttsPlay
#from langdetect import detect
from textblob import TextBlob
import sys

if len(sys.argv) < 2:
    print("textReader.py file_to_read [file_to_read_n]")
    exit()

lang = "en"
files = sys.argv[1:]

for file in files:
    '''
    fp = open(file, "r")
    lines = fp.readlines()

    for line in lines:
        if line.strip() == "":
            continue
        #lang = detect(line)
        lang = TextBlob(line).detect_language()
        ttsPlay.ttsPlay(line.strip(), lang)
        
    fp.close()
    '''
    with open(file, "r") as fp:
        for line in fp:
            
            if line.strip() == "":
                continue
            #lang = detect(line)
            lang = TextBlob(line).detect_language()
            ttsPlay.ttsPlay(line.strip(), lang)

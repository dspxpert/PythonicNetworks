import ttsPlay
import sys

if len(sys.argv) < 2:
    print("textReader.py file_to_read [file_to_read_n] [-k]")
    exit()

lang = "en"
if sys.argv[-1] == "-k":
    lang = "ko"
    files = sys.argv[1:-1]
else: 
    files = sys.argv[1:]

for file in files:
    '''
    fp = open(file, "r")
    lines = fp.readlines()

    for line in lines:
        if line.strip() == "":
            continue
        ttsPlay.ttsPlay(line.strip(), lang)
        
    fp.close()
    '''
    with open(file, "r") as fp:
        for line in fp:
            if line.strip() == "":
                continue
            ttsPlay.ttsPlay(line.strip(), lang)

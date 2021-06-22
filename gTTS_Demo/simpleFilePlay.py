import ttsPlay
import sys

with open(sys.argv[1]) as fp:
    for line in fp:
        if line.strip() == "":
            continue
        ttsPlay.ttsPlay(line.strip())
        

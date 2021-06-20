import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
import sys

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
#cap.set(3,1280)
#cap.set(4,720)

while True:
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    
    for barcode in decode(image):
        myData = barcode.data.decode('utf-8')
        
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(image,[pts],True,(255,0,255),5)
        
        pts2 = barcode.rect
        cv2.putText(image, myData,(pts2[0],pts2[1]), cv2.FONT_HERSHEY_PLAIN, 0.9, (255,0,255), 2)
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(image, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv2.imshow('Barcode Reader', image)
    if cv2.waitKey(5) == ord('q'):
      cap.release()
      sys.exit()
      
cap.release()

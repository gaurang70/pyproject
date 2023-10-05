import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)
cx,cy,w,h=100, 100, 200, 200

while True:
    success, img = cap.read()

    if img is None:
        continue  # Skip this iteration and continue with the next frame

    hands, _ = detector.findHands(img)

    if hands:


      
        cursor = hands[0]
        if cx-w//2 < cursor['lmList'][8][0] < cx+w//2 and cy-h//2 < cursor['lmList'][8][1] < cy+h//2:
            colorR = (0, 255, 0)
            cx, cy = cursor['lmList'][8][0], cursor['lmList'][8][1]

        else:
            colorR=(255,0,255)    
            
    cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), colorR, cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

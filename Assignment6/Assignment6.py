import numpy as np
import cv2
# Create our body classifier
body_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture("C:/Users/Shalaka.DESKTOP-9R8N143/Desktop/Face detect/Pedastrate1.mp4")






while cap.isOpened():
    
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
  
    bodies = body_classifier.detectMultiScale(gray, 1.1, 3)
    
    
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
      
        cv2.imshow('Pedestrians', frame)

   # if cv2.waitKey(25) & 0xFF==ord('q'):
      #  break
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()

cv2.destroyAllWindows()
    

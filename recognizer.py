import cv2
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from io import BytesIO
from PIL import image
import numpy as np


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
print 'now recognizing starts'
recognizer=cv2.createLBPHFaceRecognizer()
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer.load('/home/pi/projectfyp/trainer.yml')

img=BytesIO()
cam=PiCamera()
cam.resolution(1680,2240)
cam.start_preview()
sleep(2)

cam.capture(img,format='jpeg',resize=(1200,1600),quality=75)
img.seek(0)
pic=Image.open(img)
gray=cv2.cvtColor(np.array(pic),cv2.COLOR_BGR2GRAY)
## here detector would crop face out of image
faces=detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
for (x,y,w,h) in faces:
    cv2.rectangle((x,y),(x+w,y+h),(0,255,0),2)
Id,conf=recognizer.predict(gray[y:y+h,x:x+w])
print conf
print Id
if (conf<40):
    GPIO.output(11,GPIO.HIGH)
    if(Id==1):
        Id='baqir'
        print Id
        sleep(2)
    elif(Id==2):
	  Id=’Ihtisham’
	  Print Id
	  Sleep (2)
	elif(Id==3):
	   Id=’Zaid’
	   Print Id
	   Sleep(2)
     elif(Id==4):
         Id=’Hasan’
	    Print Id
	    Sleep(2)
     elif(Id==5):
	   Id=’Naveed’
	   Print Id
	   Sleep(2) 
else:
    Id='unknown'
    print Id
    GPIO.output(12,GPIO.HIGH)
    sleep(2)
GPIO.cleanup()
cv2.destroyAllWiindows()

from picamera import PiCamera
from time import sleep
import cv2
Id=raw_input('enter your id = ')

cam=PiCamera()
cam.resolution=(1680,2240)
print 'taking images'
cam.start_preview()
sleep(2)
cam.color_effects=(128,128)
for i in xrange(0,11):
    cam.capture('/home/pi/projectfyp/dataSet/User.'+Id+'.'+str(i)+'.jpg')
    print 'change pose'
    sleep(1)
print 'done'
cam.stop_preview()
cv2.destroyAllWindows()

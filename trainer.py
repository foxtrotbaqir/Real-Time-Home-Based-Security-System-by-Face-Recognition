import cv2,os
import numpy as np
from PIL import Image

recognizer=cv2.createLBPHFaceRecognizer()
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
path='/home/pi/projectfyp/dataSet'
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in   os.listdir('/home/pi/projectfyp/dataSet')]
    print imagePaths
    faceSamples=[]
    IDs=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        ID=int(os.path.split(imagePath)[-1].split(".")[1])
        print ID
        faces=detector.detectMultiScale(imageNp)
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            IDs.append(ID)
    return faceSamples,IDs
faces,ids=getImagesAndLabels(path)
recognizer.train(faces,np.array(ids))
print ids
recognizer.save('/home/pi/projectfyp/trainer.yml')
print 'training of images done'

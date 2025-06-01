import cv2
import numpy as np
import os
from PIL import Image
def train():
    database = 'face_dataset'
    img_dir = [x[0] for x in os.walk(database)][1::]
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    faceSamples = []
    ids = []
    for path in img_dir:
        path = str(path)
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            image_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split('.')[1])
            faces = detector.detectMultiScale(image_numpy)
            for x,y,w,h in faces:
                faceSamples.append(image_numpy[y:y+h,x:x+w])
                ids.append(id)
    recognizer.train(faceSamples,np.array(ids))
    recognizer.write('trainer.yml')
    print('\n[INFO] {0} faces trained. Exiting program'.format(len(np.unique(ids))))
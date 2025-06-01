import cv2
def recognize(names):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")
    faceCasCade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 0
    web = cv2.VideoCapture(0)
    web.set(3,640)
    web.set(4,480)
    minW = 0.1*web.get(3)
    minH = 0.1*web.get(4)
    while True:
        ret,img = web.read()
        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCasCade.detectMultiScale(gray,1.2,5, minSize=(int(minW),int(minH)))
        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
            id,confidence = recognizer.predict(gray[y:y+h,x:x+w])
            if (confidence<50):
                id = names[str(id)]
            else:
                id = 'Unknown'
            cv2.putText(img,str(id),(x+5,y-5),font,1,(0,0,0),2)
        cv2.imshow("Camera",img)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    web.release()
    cv2.destroyAllWindows()
import cv2
import os
def create_data(n_id,name):
    web = cv2.VideoCapture(0)
    web.set(3,640)
    web.set(4,480)
    faces = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    f_dir = 'face_dataset'
    f_name = name
    os.makedirs(f_dir, exist_ok=True)
    path = os.path.join(f_dir,f_name)
    if not os.path.isdir(path):
        os.mkdir(path)
    counter = 0
    while (True):
        ret,img = web.read()
        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        multi_face = faces.detectMultiScale(gray,1.3,5)
        for x,y,w,h in multi_face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
            counter+=1
            cv2.imwrite("{}/{}.{}.{}{}".format(path,name,n_id,counter,".jpg"),gray[y:y+h,x:x+w])
            cv2.imshow("Image",img)
        if cv2.waitKey(20) & 0xff==ord('q'):
            break
        elif counter>=40:
            break
    web.release()
    cv2.destroyAllWindows()
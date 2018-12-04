import cv2
import numpy as np
import pickle
import keras

model=pickle.load(open('facedetector.pkl','rb'))

cam=cv2.VideoCapture(0)

while True:
   
    ret,frame =cam.read()

    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    low=np.array([0,48,80])
    high=np.array([20,255,255])

    mask=cv2.inRange(hsv,low,high)

    output=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("camera image",frame)

    img=cv2.imread(loc+"image.jpg",0)
    img=np.array(cv2.resize(img,(28,28)))
    img=img.reshape(-1,28,28,1)

    res=model.predict(img)[0]
    if np.argmax(res)==1 : print ("mouth open")
    else: print("mouth closed")
    
    cv2.imshow("Binary Object detected",mask)
    cv2.imshow("Object Detected",output)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
cam.release()

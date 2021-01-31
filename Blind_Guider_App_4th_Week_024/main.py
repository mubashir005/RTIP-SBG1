import cv2
import pyttsx3

a = cv2.VideoCapture(0)
a.set(3,1280)
a.set(4,720)
a.set(10,70)
classNames= []
classFile = 'coco.names'
engine = pyttsx3.init()
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
while True:
    success,img = a.read()
    classIds, conf, bbox = net.detect(img,confThreshold=0.5)
    print(classIds,bbox)
    if len(classIds) != 0:

        text = "Sir !!An Obstacle is detected Before you!!! "
        engine.say(text)
        engine.runAndWait()

        for classId, confidence,box in zip(classIds.flatten(),conf.flatten(),bbox):

            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


    cv2.imshow("Detecting Objects",img)
    cv2.waitKey(1)

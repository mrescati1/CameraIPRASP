import cv2
import time as t
import datetime as date
from myThread.py import convThread

def setVideoName():
    dt=date.datetime.now()
    h=dt.strftime('%Y-%m-%d-%H-%M')
    videoName= h + "-record.avi"
    return videoName


cap = cv2.VideoCapture("rtsp://192.168.1.21:554/11")
vid = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
iD=0
while(True):
    videoName=setVideoName()
    output = cv2.VideoWriter("/home/pi/recordings/"+ videoName, vid, 25, (1280,720))
    start=t.time()
    while (cap.isOpened()):
        ret, frame= cap.read()
        output.write(frame)
        now= t.time()
        if(now > start + 60*10):
            break
    converter=convThread( iD , videoName)
    converter.start()
    iD+=0

cap.release()



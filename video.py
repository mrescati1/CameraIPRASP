import cv2
import time as t
import datetime as date
from myThread import videoStream
from myThread import convThread
from myThread import myThread
def setVideoName():
    dt=date.datetime.now()
    h=dt.strftime('%Y-%m-%d-%H-%M')
    videoName= h + "-record.avi"
    return videoName



cap = cv2.VideoCapture("rtsp://192.168.1.88:554/11")
vid = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
videoName=setVideoName()
videoStream(videoName, cap, vid)
iD=0
while(True):
    videoNameOld=videoName
    videoName=setVideoName()
    converter=convThread( 1 , videoNameOld)
    cap.release()
    cap = cv2.VideoCapture("rtsp://192.168.1.88:554/11")
    videoStream(videoName, cap, vid) 
    #stream.start()
    converter.start()
    #stream.join()
    iD+=1




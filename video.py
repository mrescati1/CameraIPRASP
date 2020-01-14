import cv2
import time as t
import datetime as date

cap = cv2.VideoCapture("rtsp://192.168.1.21:554/11") 
vid = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
#vid = cv2.VideoWriter_fourcc('X', '2', '6', '4')
while(True):
    dt=date.datetime.now()
    h=dt.strftime('%Y-%m-%d-%H-%M')
    output = cv2.VideoWriter("/home/pi/recordings/"+ h+ "-record.avi", vid, 25, (1280,720))
    start=t.time()
    while (cap.isOpened()):
        ret, frame= cap.read()
        output.write(frame)
        now= t.time()
        if(now > start + 60*10):
            break
cap.release()



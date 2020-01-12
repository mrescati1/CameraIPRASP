import cv2
import time as t
cap = cv2.VideoCapture("rtsp://192.168.1.21:554/11") 
vid = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("/home/pi/recordings/cam_video.avi", vid, 25.0, (1280,720))
i=0
start=t.time()
while (cap.isOpened()):
    ret, frame= cap.read()
    output.write(frame)
    now= t.time()
    if(now > start + 60):
        break

cap.release()



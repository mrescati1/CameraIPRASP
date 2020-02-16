import threading
import time as t
import subprocess
import cv2
import os


def videoConvert(videoName):
    print("converting " + videoName )
    os.system("bash converter.sh " + videoName)
    os.system("rm ../recordings/" + videoName)

def videoStream(videoName, cap, vid):
    output = cv2.VideoWriter("/home/pi/recordings/"+ videoName, vid, 25, (1280,720))
    start=t.time()
    while (cap.isOpened()):
      try:
        ret, frame= cap.read()
        output.write(frame)
        now= t.time()
        if(now > start + 60*10):
            break
      except:
        cap.release()
        cap = cv2.VideoCapture("rtsp://192.168.1.88:554/11")


class convThread (threading.Thread):
   def __init__(self, threadID, videoName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.videoName = videoName
   def run(self):
      print "Starting " + str(self.threadID)
      videoConvert(self.videoName)
      print "Exiting " + str(self.threadID)

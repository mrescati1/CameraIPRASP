import threading
import time
import subprocess

exitFlag = 0

def videoConvert(videoName):
    print("converting " + videoName )
    subprocess.run("bash convert.sh " + videoName)
    subprocess.run("rm ../recordings/" + videoName)

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
      print "Starting " + self.threadID
      convert_video(self.videoName)
      print "Exiting " + self.threadID

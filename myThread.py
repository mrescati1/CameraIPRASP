import threading
import time
import subprocess

exitFlag = 0

def convert_video(videoName):
    print("converting " + videoName )
    subprocess.run("bash convert.sh " + videoName)
    subprocess.run("rm ../recordings/" + videoName)
def stream_video(videoName, cap, vid):



class convThread (threading.Thread):
   def __init__(self, threadID, videoName):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.videoName = videoName
   def run(self):
      print "Starting " + self.threadID
      convert_video(self.videoName)
      print "Exiting " + self.threadID

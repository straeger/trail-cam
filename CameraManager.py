from time import sleep
import picamera
import datetime
import os
from RelaiManager import RelaiManager

class CameraManeger:

    camera = 0
    path = 0

    def getTimeStamp(self):
        return datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S_%f")

    def captureImage(self):
        self.camera.capture( '%s/image_%s%s' % (self.path, self.getTimeStamp(), '.jpg'))
        self.camera.capture('%s/image_%s%s' % (self.path, self.getTimeStamp(), '.jpg'))
        self.camera.capture('%s/image_%s%s' % (self.path, self.getTimeStamp(), '.jpg'))
        self.camera.capture('%s/image_%s%s' % (self.path, self.getTimeStamp(), '.jpg'))

    def captureVideo(self):
        print "%s - Taking picture"
        self.camera.start_recording('%s/video_%s%s' % (self.path, self.getTimeStamp(), '.h264'))
        sleep(5)
        self.camera.stop_recording()

    def __init__(self, path):
        self.camera = picamera.PiCamera()
        self.path = path

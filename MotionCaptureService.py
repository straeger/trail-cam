from time import sleep
import RPi.GPIO as GPIO
import time
import datetime
import os

from RelaiManager import RelaiManager
from CameraManager import CameraManeger
from InfraredLightManager import LightManager

class MotionCaptureService:

    relaiManager = 0
    cameraManager = 0
    lightManager = 0

    def capture(self,gpio):
        print "%s - Warten auf Bewegung" % datetime.datetime.now()
        isNight = self.lightManager.isNight()

        print isNight

        if(isNight):
            print "Relai On"
            self.relaiManager.off()


        self.cameraManager.captureImage()

        if(isNight):
            print "Relai Off"
            self.relaiManager.on()

    def __init__(self, gpioInputPin, relaiPin, lightPin):
        GPIO.setmode(GPIO.BOARD)
        self.relaiManager = RelaiManager(relaiPin)
        self.cameraManager = CameraManeger("/home/pi/Pictures")
        self.lightManager = LightManager(lightPin)
        GPIO.setup(gpioInputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.gpioPin = gpioInputPin
        GPIO.add_event_detect(gpioInputPin, GPIO.RISING, callback=self.capture)
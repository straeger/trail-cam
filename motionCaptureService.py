from time import sleep
import RPi.GPIO as GPIO
import time
import datetime
import os

class MotionCaptureService:

    def capture(self,gpio):
        print "%s - Warten auf Bewegung" % datetime.datetime.now()

    def __init__(self, gpioInputPin):
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpioInputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.gpioPin = gpioInputPin
        GPIO.add_event_detect(gpioInputPin, GPIO.RISING, callback=self.capture)
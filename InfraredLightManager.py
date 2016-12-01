from time import sleep
import picamera
import datetime
import os
import RPi.GPIO as GPIO

class LightManager:

    gpioInputPin = 0

    def isNight(self):
        return GPIO.input(self.gpioInputPin)

    def __init__(self, gpioInputPin):
        self.gpioInputPin = gpioInputPin
        GPIO.setup(self.gpioInputPin, GPIO.IN)
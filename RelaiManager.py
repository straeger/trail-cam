from time import sleep
import RPi.GPIO as GPIO
import time
import datetime
import os

class RelaiManager:

    gpiopin = 0

    def __init__(self, gpioInputPin):
        self.gpioPin =gpioInputPin

        GPIO.setup(gpioInputPin, GPIO.OUT)

    def on(self):
        GPIO.output(self.gpioPin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.gpioPin, GPIO.LOW)
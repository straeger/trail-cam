#motionSensor = gpio 21
#relaus = gpio 16 20
#ligth gpio 26

from time import sleep
import RPi.GPIO as GPIO

from .MotionCaptureService import MotionCaptureService

GPIO.setmode(GPIO.BOARD)
motionCaptureService = MotionCaptureService(21)
motionCaptureService.addEvent()

# you can continue doing other stuff here
while True:
    pass
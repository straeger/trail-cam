#motionSensor = gpio 19
#relaus = gpio 16 20
#ligth gpio 26

from time import sleep
import RPi.GPIO as GPIO

from MotionCaptureService import MotionCaptureService

motionCaptureService = MotionCaptureService(21)

# you can continue doing other stuff here
while True:
    pass
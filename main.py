#!/usr/bin/env python
#motionSensor = gpio 19
#relaus = gpio 16 20
#ligth gpio 26

from time import sleep
import RPi.GPIO as GPIO

from motionCaptureService import MotionCaptureService


motionCaptureService = MotionCaptureService(40, 36, 37)


# you can continue doing other stuff here
while True:
    pass
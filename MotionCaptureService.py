from time import sleep
import RPi.GPIO as GPIO

class MotionCaptureService:
    
    gpioPin = 12345
    var = 1
    counter = 0

    def __init__(self, gpioInputPin):
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpioInputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.gpioPin = gpioInputPin

    def addEvent(self):
        GPIO.add_event_detect(self.gpioPin, GPIO.RISING, callback=self.capture, bouncetime=300)
     
    def capture(self):
        if self.var == 1:
            sleep(1.5)  # confirm the movement by waiting 1.5 sec
            if GPIO.input(7):  # and check again the input
                print("Movement!")

                # stop detection for 20 sec
                GPIO.remove_event_detect(7)
                sleep(20)
                GPIO.add_event_detect(7, GPIO.RISING, callback=self.capture, bouncetime=300)

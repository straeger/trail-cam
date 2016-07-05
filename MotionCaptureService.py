from time import sleep
import RPi.GPIO as GPIO

class MotionCaptureService:
    
    gpioPin = 12345
    counter = 0

    def __init__(self, gpioInputPin):
        print("****Init!")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpioInputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.gpioPin = gpioInputPin

    def addEvent(self):
        print("Add Event!")
        print(self.gpioPin)
        GPIO.add_event_detect(self.gpioPin, GPIO.RISING, callback=self.capture, bouncetime=300)
     
    def capture(self,f):
        print("Movement!")
        sleep(1.5)  # confirm the movement by waiting 1.5 sec
        if GPIO.input(self.gpioPin):  # and check again the input
            print("Movement!")

            # stop detection for 20 sec
            GPIO.remove_event_detect(self.gpioPin)
            sleep(2)
            GPIO.add_event_detect(self.gpioPin, GPIO.RISING, callback=self.capture, bouncetime=300)

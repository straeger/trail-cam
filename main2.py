import time
import RPi.GPIO as GPIO

# Pin-Nummern wie auf dem Raspberry Board verwenden
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) als Output
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)


while 1:
  # LED aus
  GPIO.output(36, GPIO.LOW)
  GPIO.output(38, GPIO.LOW)
  # eine Sekunde warten
  time.sleep(1)
  # LED an
  GPIO.output(36, GPIO.HIGH)
  GPIO.output(38, GPIO.HIGH)
  # eine Sekunde warten
  time.sleep(1)
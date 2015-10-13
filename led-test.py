# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pin16 = 16 # Broadcom pin 18 (P1 pin 12)
pin20 = 20 # Broadcom pin 23 (P1 pin 16)
pin21 = 21

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(16, GPIO.OUT) # LED pin set as output
GPIO.setup(20, GPIO.OUT) # PWM pin set as output
GPIO.setup(21, GPIO.OUT)

GPIO.output(16, GPIO.HIGH)
time.sleep(1)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.HIGH)
time.sleep(1)
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.HIGH)
time.sleep(1)
GPIO.output(21, GPIO.LOW)
GPIO.cleanup() # cleanup all GPIO

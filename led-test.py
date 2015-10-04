# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 16 # Broadcom pin 18 (P1 pin 12)
ledPin = 20 # Broadcom pin 23 (P1 pin 16)


# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output

GPIO.output(ledPin, GPIO.HIGH)
GPIO.output(pwmPin, GPIO.HIGH)
time.sleep(5)
GPIO.output(ledPin, GPIO.LOW)
GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup() # cleanup all GPIO

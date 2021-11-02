#!/usr/bin/env python3
import RPi.GPIO as GPIO

ReedPin = 17
Gpin    = 27
Rpin    = 22

def setup():
	GPIO.setmode(GPIO.BCM)       # 
	GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
	GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
	GPIO.setup(ReedPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set ReedPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(ReedPin, GPIO.BOTH, callback=detect, bouncetime=200)

def Led(x):
	if x == 0:
		GPIO.output(Rpin, 1)
		GPIO.output(Gpin, 0)
	if x == 1:
		GPIO.output(Rpin, 0)
		GPIO.output(Gpin, 1)

def detect():
	Led(GPIO.input(ReedPin))

def loop():
	while True:
		pass

def destroy():
	GPIO.output(Gpin, GPIO.HIGH)       # Green led on
	GPIO.output(Rpin, GPIO.LOW)       # Red led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()


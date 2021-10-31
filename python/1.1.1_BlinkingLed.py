#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
RedLedPin = 17
RedWords = ["pass", "god-", "but"]
GreenLedPin = 18
GreenWords = [" ", "the ", "damned ", "ter"]
def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set LedPin's mode to output,and initial level to High(3.3v)
    GPIO.setup(RedLedPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(GreenLedPin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
    count = 0;
    while True:
        # print ('...LED ON')
        # Turn on LED
        if count % 3 == 0:
            GPIO.output(RedLedPin, GPIO.LOW)
            print(RedWords[int(count / 3)], end='')
        else:
            GPIO.output(RedLedPin, GPIO.HIGH)

        if count % 4 == 0:
            GPIO.output(GreenLedPin, GPIO.LOW)
            print(GreenWords[int(count / 4)], end='')
        else:
            GPIO.output(GreenLedPin, GPIO.HIGH)

        if count % 12 == 0:
            count = 0
            print("")

        count = count + 1
        time.sleep(0.3)
        # print ('LED OFF...')
        # Turn off LED
        # GPIO.output(RedLedPin, GPIO.HIGH)
        # time.sleep(0.5)
# Define a destroy function for clean up everything after the script finished
def destroy():
    # Turn off LED
    GPIO.output(RedLedPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()                   
# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
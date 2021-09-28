import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)

cyclesNumber = 24
period = 0.3

def runningLight(cyclesNumber, period):
    lednumber = 0;

    for i in range(cyclesNumber):

        GPIO.output(dac[lednumber], 1)
        time.sleep(period)
        GPIO.output(dac[lednumber], 0)

        if lednumber <= 6:
            lednumber = lednumber + 1
        else:
            lednumber = lednumber - 7;

cyclesNumber = 24;
period = 0.5;

runningLight(cyclesNumber, period)

GPIO.output(leds + dac, 0)
GPIO.cleanup()
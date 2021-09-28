import RPi.GPIO as GPIO
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

pattern = [1, 0, 1, 0, 0, 0, 1, 0]
pattern1 = [1, 1, 1, 1, 0, 0, 0, 0]
pattern2 = [1, 0, 1, 0, 1, 0, 1, 0]
pattern3 = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)

period = 2

def lightPattern (pattern, period):
    GPIO.output(leds, pattern)
    sleep(period)
    GPIO.output(leds, pattern)

lightPattern(pattern, period)
lightPattern(pattern1, period)
lightPattern(pattern2, period)
lightPattern(pattern3, period)

GPIO.cleanup()
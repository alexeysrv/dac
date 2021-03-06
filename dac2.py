import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        
        for i in range(0, 255, 1):
            signal = bin2dac(i)
            time.sleep(0.02)
            voltage = i / levels * maxVoltage
            print("Entered value = {:^3} -> {}, output votage = {:.2f}".format(i, signal, voltage))
        for i in range (255, 0, -1):
            signal = bin2dac(i)
            time.sleep(0.02)
            voltage = i / levels * maxVoltage
            print("Entered value = {:^3} -> {}, output votage = {:.2f}".format(i, signal, voltage))

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")

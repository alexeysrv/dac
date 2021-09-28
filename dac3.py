import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
#GPIO.setup(dac, GPIO.OUT)

p = GPIO.PWM(23, 1000)  
p.start(0)
try:
    while True:
            dc = int(input())
            if dc >= 0 and dc <= 100:
                p.ChangeDutyCycle(dc)
            else:
                print("Enter a new dc ")
finally:
    p.stop()
    GPIO.cleanup()
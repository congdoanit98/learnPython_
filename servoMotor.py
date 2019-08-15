import RPi.GPIO as GPIO
import time

pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0
dc = [1, 1]
try:
    while True:
        for i in dc:
            p.ChangeDutyCycle(i)
            time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.ChangeDutyCycle(10.0)
        time.sleep(1)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(5.0)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        
except:
    p.stop()
GPIO.cleanup()
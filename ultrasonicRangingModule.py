import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 13
echo = 19

print('start')

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.5)
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        
        while GPIO.input(echo) == 0:
            start = time.time()
#            print('end')
            
        while GPIO.input(echo) == 1:
            end = time.time()
        
        pulse_time = end - start
        distance = pulse_time * 17000
        distance = round(distance, 2)
        print(distance, 'cm')
except:
    GPIO.cleanup()
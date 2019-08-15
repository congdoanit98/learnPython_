import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 24
sw = 16
scale = [261, 293, 329, 349, 391, 415, 440, 493]
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(sw, GPIO.IN)
p = GPIO.PWM(buzzer, 100)

#little star
list = [1, 1, 2, 1, 4, 3, 1, 2, 1, 6, 4]

try:
    while 1:
        if GPIO.input(sw) == 1:
            p.start(100)
            p.ChangeDutyCycle(90)
            for i in range(len(list)):
                p.ChangeFrequency(scale[list[i]])
                if (i+1) % 6 == 0:
                    time.sleep(1)
                else:
                    time.sleep(0.5)
            p.stop()
except:
    GPIO.cleanup()
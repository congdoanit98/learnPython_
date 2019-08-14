# change color 
import RPi.GPIO as G
import time
G.setmode(G.BOARD)

redled = 3
greenled = 5
blueled = 7
G.setup(redled, G.OUT, initial = G.LOW)
G.setup(greenled, G.OUT, initial = G.LOW)
G.setup(blueled, G.OUT, initial = G.LOW)

G.output(redled, G.HIGH)
G.output(greenled, G.HIGH)
G.output(blueled, G.HIGH)
while True:
    G.output(blueled,G.HIGH)
    G.output(greenled,G.LOW)
    G.output(redled,G.LOW)
    time.sleep(0.25)
    G.output(blueled,G.LOW)
    G.output(greenled,G.HIGH)
    G.output(redled,G.LOW)
    time.sleep(0.25)
    G.output(blueled,G.LOW)
    G.output(greenled,G.LOW)
    G.output(redled,G.HIGH)
    time.sleep(0.25)
G.cleanup()
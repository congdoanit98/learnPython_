# enter the color from kb
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
    a =input()
    if(a =='b'):
        G.output(blueled,G.HIGH)
        G.output(greenled,G.LOW)
        G.output(redled,G.LOW)
    elif(a == 'g'):
        G.output(blueled,G.LOW)
        G.output(greenled,G.HIGH)
        G.output(redled,G.LOW)
    elif(a == 'r'):
        G.output(blueled,G.LOW)
        G.output(greenled,G.LOW)
        G.output(redled,G.HIGH)
    else:
        break
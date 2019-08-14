# use switch control led
import RPi.GPIO as G
import time
G.setmode(G.BOARD)
button = 11
var =0
G.setup(button, G.IN)
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
    val = G.input(button)
    if(val==0):
        G.output(blueled,G.HIGH)
        G.output(greenled,G.LOW)
        G.output(redled,G.LOW)
    elif(val==1):
        G.output(blueled,G.LOW)
        G.output(greenled,G.HIGH)
        G.output(redled,G.LOW)
    else:
        break
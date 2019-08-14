import RPi.GPIO as G
import time
G.setmode(G.BOARD)
button = 12
var =0
G.setup(button, G.IN)
try:
    while True:
        val = G.input(button)
        print(val)
        if (val == 1):
            print('button on')
            time.sleep(1)
        else:
            print('button off')
            time.sleep(1)
            
except KeyboardInterrupt:
    pass
G.cleanup()

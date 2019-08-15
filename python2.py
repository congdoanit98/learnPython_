import RPi.GPIO as G
import time
G.setmode(G.BOARD)
val = 0
ball =11
G.setup(ball,G.IN)
try:
    while True:
        val = G.input(ball)
        if(val==0):
            print('ball off')
            time.sleep(1)
        else:
            print('ball on')
            time.sleep(1)
except KeyboardInterrupt:
    pass
G.cleanup()
        
        
        
        
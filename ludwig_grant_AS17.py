# File Name: ludwig_grant_AS17.py
# File Path: /home/ludwigg/Python/PyRpi_AS17/ludwig_grant_AS17.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS17/ludwig_grant_AS17.py

# Grant Ludwig
# 12/6/2019
# AS.17
# Create a custom class to display an animated graphics object

from graphics import *
from Ghost import *
import time
import random

WIN_HEIGHT = 800
WIN_WIDTH = 800
PIXEL_SIZE = 10
EYE_TIMER = 1

win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")
           
Pinky = Ghost("pink", 100, 100, win)
Blinky = Ghost("Red", 0, 0, win)

changeTime = time.time() + EYE_TIMER
while(True):
    # if changeTime - time.time() < 0:
        # Pinky.SetEyeDirection(random.randint(0,4))
        # Blinky.SetEyeDirection(random.randint(0,4))
        # changeTime = time.time() + EYE_TIMER
        
    Pinky.SetEyeDirection(random.randint(0,4))
    Blinky.SetEyeDirection(random.randint(0,4))
    Pinky.Animate()
    Blinky.Animate()
    update(5)
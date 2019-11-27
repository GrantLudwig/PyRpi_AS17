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

WIN_HEIGHT = 800
WIN_WIDTH = 800
PIXEL_SIZE = 10

win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")
           
Pinky = Ghost("pink", 100, 100, win)
Blinky = Ghost("Red", 0, 0, win)

while(True):
    Pinky.Animate()
    Blinky.Animate()
    update(5)
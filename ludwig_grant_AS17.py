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
SKIRT_TIMER = .2

win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("grey")
           
ghosts = []
ghosts.append(Ghost("pink", 100, 50, -4, 3, win))
ghosts.append(Ghost("Red", 0, 0, 5, 7, win))
ghosts.append(Ghost("Blue", 400, 400, 5, -6, win))
ghosts.append(Ghost("Orange", 750, 600, -1, -4, win))

changeTime = time.time() + SKIRT_TIMER
while(True):
    for g in ghosts:
        if g.GetX() <= 0:
            g.xDir = abs(g.xDir)
        elif g.GetX() >= WIN_WIDTH:
            g.xDir = -abs(g.xDir)
        if g.GetY() <= 0:
            g.yDir = abs(g.yDir)
        elif g.GetY() >= WIN_HEIGHT:
            g.yDir = -abs(g.yDir)
        g.Move()
    if changeTime - time.time() < 0:
        for g in ghosts:
            g.Animate()
            changeTime = time.time() + SKIRT_TIMER
    update(60)
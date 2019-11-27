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

thing = []
ghost = []
skirt = False
for i in range(10): # col
    ghost.append([])
    thing.append([])
    for j in range(10): # row
        ghost[i].append(Rectangle(Point(i * PIXEL_SIZE, j * PIXEL_SIZE), Point((i * PIXEL_SIZE) + PIXEL_SIZE, (j * PIXEL_SIZE) + PIXEL_SIZE)))
        if (i < 2 or i > 7) and j == 0:
            thing[i].append(0)
        elif (i == 0 or i == 9) and j == 1:
            thing[i].append(0)
        elif j == 9:
            if skirt:
                ghost[i][j].draw(win)
                ghost[i][j].setFill("Black")
                skirt = False
                thing[i].append(1)
            else:
                skirt = True
                thing[i].append(0)
        else:
            ghost[i][j].draw(win)
            ghost[i][j].setFill("Black")
            thing[i].append(1)
          
skirt = True  
ghost2 = []        
for i in range(10): # col
    ghost2.append([])
    for j in range(10): # row
        ghost2[i].append(Rectangle(Point(i * PIXEL_SIZE, j * PIXEL_SIZE), Point((i * PIXEL_SIZE) + PIXEL_SIZE, (j * PIXEL_SIZE) + PIXEL_SIZE)))
        if (i < 2 or i > 7) and j == 0:
            None
        elif (i == 0 or i == 9) and j == 1:
            None
        elif j == 9:
            if skirt:
                ghost2[i][j].draw(win)
                ghost2[i][j].setFill("Black")
                skirt = False
            else:
                skirt = True
        else:
            ghost2[i][j].draw(win)
            ghost2[i][j].setFill("Black")
            
def drawGhost(remove):
    global ghost
    skirt = False
    for i in range(10): # col
        for j in range(10): # row
            if (i < 2 or i > 7) and j == 0:
                None
            elif (i == 0 or i == 9) and j == 1:
                None
            elif j == 9:
                if skirt:
                    if remove:
                        ghost[i][j].undraw()
                    else:
                        try:
                            ghost[i][j].draw(win)
                        except:
                            None
                    skirt = False
                else:
                    skirt = True
            else:
                if remove:
                    ghost[i][j].undraw()
                else:
                    try:
                        ghost[i][j].draw(win)
                    except:
                        None

def drawGhost2(remove):
    global ghost2
    skirt = True
    for i in range(10): # col
        for j in range(10): # row
            if (i < 2 or i > 7) and j == 0:
                None
            elif (i == 0 or i == 9) and j == 1:
                None
            elif j == 9:
                if skirt:
                    if remove:
                        ghost2[i][j].undraw()
                    else:
                        try:
                            ghost2[i][j].draw(win)
                        except:
                            None
                    skirt = False
                else:
                    skirt = True
            else:
                if remove:
                    ghost2[i][j].undraw()
                else:
                   try:
                        ghost2[i][j].draw(win)
                   except:
                        None

print(thing)
switch = False
while(True):
    drawGhost(switch)
    drawGhost2(not switch)
    switch = not switch
    update(5)
from graphics import *

class Ghost:

    # goes column by column
    GhostShape = (  (0, 0, 1, 1, 1, 1, 1, 1, 1, 0), 
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 0),
                    (1, 1, 3, 2, 1, 1, 1, 1, 1, 1), 
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 0),
                    (1, 1, 3, 2, 1, 1, 1, 1, 1, 1),
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1))
                
    # goes column by column, should be same dimensions as GhostShape
    GhostShape2 = ( (0, 0, 1, 1, 1, 1, 1, 1, 1, 1), 
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 1),
                    (1, 1, 3, 2, 1, 1, 1, 1, 1, 0), 
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 1),
                    (1, 1, 3, 2, 1, 1, 1, 1, 1, 0),
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (0, 0, 1, 1, 1, 1, 1, 1, 1, 0))
                    
    PIXEL_SIZE = 10

    def __init__(self, color, posX, posY, win):
        self.Color = color
        self.posX = posX
        self.posY = posY
        self.Ghost = []
        self.Ghost2 = []
        self.win = win
        self.__setupGhost()
        self.Ghost1Active = True
        
    def __setupGhost(self):
        for i in range(len(self.GhostShape[0])):
            self.Ghost.append([])
            for j in range(len(self.GhostShape)):
                self.Ghost[i].append(Rectangle(Point((i * self.PIXEL_SIZE) + self.posX, (j * self.PIXEL_SIZE) + self.posY), 
                                                Point((i * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.posX, (j * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.posY)))
                if self.GhostShape[i][j] == 1:
                    self.Ghost[i][j].setFill(self.Color)
                    self.Ghost[i][j].draw(self.win)
                elif self.GhostShape[i][j] == 2:
                    self.Ghost[i][j].setFill("White")
                    self.Ghost[i][j].draw(self.win)
                elif self.GhostShape[i][j] == 3:
                    self.Ghost[i][j].setFill("Black")
                    self.Ghost[i][j].draw(self.win)
                    
        for i in range(len(self.GhostShape2[0])):
            self.Ghost2.append([])
            for j in range(len(self.GhostShape2)):
                self.Ghost2[i].append(Rectangle(Point((i * self.PIXEL_SIZE) + self.posX, (j * self.PIXEL_SIZE) + self.posY), 
                                                Point((i * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.posX, (j * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.posY)))
                if self.GhostShape2[i][j] == 1:
                    self.Ghost2[i][j].setFill(self.Color)
                elif self.GhostShape2[i][j] == 2:
                    self.Ghost2[i][j].setFill("White")
                elif self.GhostShape2[i][j] == 3:
                    self.Ghost2[i][j].setFill("Black")
                    
    def Animate(self):
        for i in range(len(self.GhostShape[0])):
            for j in range(len(self.GhostShape)):
                if self.Ghost1Active:
                    if self.GhostShape[i][j] != 0:
                        self.Ghost[i][j].undraw()
                    if self.GhostShape2[i][j] != 0:
                        self.Ghost2[i][j].draw(self.win)
                else:
                    if self.GhostShape[i][j] != 0:
                        self.Ghost[i][j].draw(self.win)
                    if self.GhostShape2[i][j] != 0:
                        self.Ghost2[i][j].undraw()
        self.Ghost1Active = not self.Ghost1Active
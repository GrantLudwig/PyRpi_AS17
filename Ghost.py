from graphics import *

class Ghost:

    # goes column by column
    GhostShape = (  (0, 0, 1, 1, 1, 1, 1, 1, 1, 0), 
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 0),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 1), 
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 0),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 1),
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1))
                
    # goes column by column, should be same dimensions as GhostShape
    GhostShape2 = ( (0, 0, 1, 1, 1, 1, 1, 1, 1, 1), 
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 1),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 0), 
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 1),
                    (1, 1, 2, 2, 1, 1, 1, 1, 1, 0),
                    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                    (0, 0, 1, 1, 1, 1, 1, 1, 1, 0))
                    
    EyeLowerLeft = ((0,1),(0,0)) # 1
    EyeLowerRight = ((0,0),(0,1)) # 2
    EyeUpperLeft = ((1,0),(0,0)) # 3
    EyeUpperRight = ((0,0),(1,0)) # 0
                    
    PIXEL_SIZE = 10

    def __init__(self, color, posX, posY, xDir, yDir, win):
        self.Color = color
        self.__posX = posX
        self.__posY = posY
        self.__Ghost = []
        self.__Ghost2 = []
        self.win = win
        self.__setup__Ghost()
        self.__Ghost1Active = True
        self.xDir = xDir
        self.yDir = yDir
        
    def __setup__Ghost(self):
        for i in range(len(self.GhostShape[0])):
            self.__Ghost.append([])
            for j in range(len(self.GhostShape)):
                self.__Ghost[i].append(Rectangle(Point((i * self.PIXEL_SIZE) + self.__posX, (j * self.PIXEL_SIZE) + self.__posY), 
                                                Point((i * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.__posX, (j * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.__posY)))
                if self.GhostShape[i][j] == 1:
                    self.__Ghost[i][j].setFill(self.Color)
                    self.__Ghost[i][j].draw(self.win)
                elif self.GhostShape[i][j] == 2:
                    if self.EyeUpperRight[i%2][j%2] == 1:
                        self.__Ghost[i][j].setFill("Black")
                    else:
                        self.__Ghost[i][j].setFill("White")
                    self.__Ghost[i][j].draw(self.win)
                    
        for i in range(len(self.GhostShape2[0])):
            self.__Ghost2.append([])
            for j in range(len(self.GhostShape2)):
                self.__Ghost2[i].append(Rectangle(Point((i * self.PIXEL_SIZE) + self.__posX, (j * self.PIXEL_SIZE) + self.__posY), 
                                                Point((i * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.__posX, (j * self.PIXEL_SIZE) + self.PIXEL_SIZE + self.__posY)))
                if self.GhostShape2[i][j] == 1:
                    self.__Ghost2[i][j].setFill(self.Color)
                elif self.GhostShape2[i][j] == 2:
                    if self.EyeUpperRight[i%2][j%2] == 1:
                        self.__Ghost2[i][j].setFill("Black")
                    else:
                        self.__Ghost2[i][j].setFill("White")
                        
    # 0 is upper right, 1 it lower right, etc.
    def __SetEyeDirection(self, num):
        for i in range(len(self.GhostShape[0])):
            for j in range(len(self.GhostShape)):
                if self.GhostShape2[i][j] == 2:
                    if num == 0:
                        if self.EyeUpperRight[i%2][j%2] == 1:
                            self.__Ghost[i][j].setFill("Black")
                            self.__Ghost2[i][j].setFill("Black")
                        else:
                            self.__Ghost[i][j].setFill("White")
                            self.__Ghost2[i][j].setFill("White")
                    elif num == 1:
                        if self.EyeLowerRight[i%2][j%2] == 1:
                            self.__Ghost[i][j].setFill("Black")
                            self.__Ghost2[i][j].setFill("Black")
                        else:
                            self.__Ghost[i][j].setFill("White")
                            self.__Ghost2[i][j].setFill("White")
                    elif num == 2:
                        if self.EyeLowerLeft[i%2][j%2] == 1:
                            self.__Ghost[i][j].setFill("Black")
                            self.__Ghost2[i][j].setFill("Black")
                        else:
                            self.__Ghost[i][j].setFill("White")
                            self.__Ghost2[i][j].setFill("White")
                    elif num == 3:
                        if self.EyeUpperLeft[i%2][j%2] == 1:
                            self.__Ghost[i][j].setFill("Black")
                            self.__Ghost2[i][j].setFill("Black")
                        else:
                            self.__Ghost[i][j].setFill("White")
                            self.__Ghost2[i][j].setFill("White")
                    
    def Animate(self):
        for i in range(len(self.GhostShape[0])):
            for j in range(len(self.GhostShape)):
                if self.__Ghost1Active:
                    if self.GhostShape[i][j] != 0:
                        self.__Ghost[i][j].undraw()
                    if self.GhostShape2[i][j] != 0:
                        self.__Ghost2[i][j].draw(self.win)
                else:
                    if self.GhostShape[i][j] != 0:
                        self.__Ghost[i][j].draw(self.win)
                    if self.GhostShape2[i][j] != 0:
                        self.__Ghost2[i][j].undraw()
        self.__Ghost1Active = not self.__Ghost1Active
        
    def Move(self):
        for i in range(len(self.GhostShape[0])):
            for j in range(len(self.GhostShape)):
                self.__Ghost[i][j].move(self.xDir, self.yDir)
                self.__Ghost2[i][j].move(self.xDir, self.yDir)
                
        if self.xDir >= 0:
            if self.yDir >= 0:
                self.__SetEyeDirection(1)
            else:
                self.__SetEyeDirection(0)
        else:
            if self.yDir >= 0:
                self.__SetEyeDirection(2)
            else:
                self.__SetEyeDirection(3)
        
    def GetX(self):
        return (self.__Ghost[0][0].getCenter().x - 5) + int((self.PIXEL_SIZE * len(self.GhostShape[0]))/2)
    
    def GetY(self):
        return (self.__Ghost[0][0].getCenter().y - 5) + int((self.PIXEL_SIZE * len(self.GhostShape))/2)
        
    def GetWidth(self):
        return self.PIXEL_SIZE * len(self.GhostShape[0])
    
    def GetHeight(self):
        return self.PIXEL_SIZE * len(self.GhostShape)
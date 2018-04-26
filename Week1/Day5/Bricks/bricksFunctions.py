import math
import random
import pygame

def reinitialize(xbar, ybar, xball, yball, xballDisplacement, yballDisplacement, timeWait):
    xbar = 200
    ybar = 350

    xball = 230
    yball = 350
    xballDisplacement = round(math.cos(45) * 4)
    yballDisplacement = -round(math.sin(45) * 4)

    timeWait = True

class ball:

    def xchangeSpeed(self, xyDisplacement, speed):
        self.speed = speed
        self.xyDisplacement = xyDisplacement
        self.xyDisplacement = round(math.cos(45) * self.speed)

    def xchangeSpeed(self, xyDisplacement, speed):
        self.speed = speed
        self.xyDisplacement = xyDisplacement
        self.xballDisplacement = round(math.cos(45) * self.speed)

    def reverseSign(self, xyDisplacement):
        self.xyDisplacement = -xyDisplacement

class Brick:

    def __init__(self, screen, xpos, ypos):
        brickArray = []
        brickArray.append(self)
        self.a = random.randint(0, 200)
        self.b = random.randint(0, 200)
        self.c = random.randint(0, 200)
        self.screen = screen
        self.color = pygame.Color(self.a, self.b, self.c)
        self.xpos = xpos
        self.ypos = ypos
        self.ysize = 30
        self.xsize = round(self.ysize * 1.6)
        self.strength = 2

    def reduceStrength(self):
        self.strength -= 0
        if self.strength == 0:
            print('lets destroy this shit, yo')

    def drawBrick(self):
        pygame.draw.rect(self.screen, self.color, (self.xpos, self.ypos, self.xsize, self.ysize))

    def __iter__(self):
        for brick in self.brickArray:
            yield brick.drawBrick()

class game:

    def __init__(self, screen):

        self.brickArray = brickArray
        self.background = pygame.Color(67, 0, 89)
        self.barColor = pygame.Color(0, 255, 255)
        self.ballColor = pygame.Color(0, 255, 255)
        self.screen = pygame.display.set_mode((600, 400))
        self.a = pygame.image.load('icon.ico')
        self.ProgramName = "BrickDestroyer 3: The Revenge"
        self.xbar = 200
        self.ybar = 350
        self.xbarSize = 80
        self.ybarSize = 30
        self.barSpeed = 6
        self.xball = 130
        self.yball = 340

        self.xballSpeed = 4
        self.yballSpeed = 4
        self.middleSpeed = 4
        self.sideSpeed = 6
        self.cornerSpeed = 8
        self.xballDisplacement = round(math.cos(45) * self.xballSpeed)
        self.yballDisplacement = -round(math.sin(45) * self.yballSpeed)
        self.timeWait = False
        self.timeWait2 = False
        self.overrideDisplacement = False

    def displayDetails(self):
        pygame.display.set_icon(self.a)
        pygame.display.set_caption(self.ProgramName)





timeWait = False
timeWait2 = False

overrideDisplacement = False

fpsClocks = pygame.time.Clock()
speedClock = 70

brickArray = []
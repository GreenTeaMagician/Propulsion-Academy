
import sys
import time
from bricksFunctions import *
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("MichalBricks")

a = pygame.image.load('icon.ico')
pygame.display.set_icon(a)

background = pygame.Color(67, 0, 89)
barColor = pygame.Color(0, 255, 255)
ballColor = pygame.Color(0, 255, 255)

xbar = 200
ybar = 350
xbarSize = 80
ybarSize = 30
barSpeed = 6

xball = 130
yball = 340

xballSpeed = 4
yballSpeed = 4
middleSpeed = 4
sideSpeed = 6
cornerSpeed = 8
xballDisplacement = round(math.cos(45) * xballSpeed)
yballDisplacement = -round(math.sin(45) * yballSpeed)

timeWait = False
timeWait2 = False

overrideDisplacement = False

fpsClocks = pygame.time.Clock()
speedClock = 70
brickArray = []

#game(brickArray, 'MichalBricks', 200, 350, 80, 30, 6, 130, 340, 4, 4, 4, 6, 8, xballDisplacement, yballDisplacement)
#Creation of bricks. Still to be done...

brick1 = Brick(screen, 50, 50)
brick2 = Brick(screen, 98, 50)
brick3 = Brick(screen, 146, 50)
brick4 = Brick(screen, 194, 50)
brick5 = Brick(screen, 242, 50)
brick6 = Brick(screen, 290, 50)
brick7 = Brick(screen, 338, 50)
brick8 = Brick(screen, 72, 80)
brick9 = Brick(screen, 120, 80)

brickArray.append(brick1)
brickArray.append(brick2)
brickArray.append(brick3)
brickArray.append(brick4)
brickArray.append(brick5)
brickArray.append(brick6)
brickArray.append(brick7)
brickArray.append(brick8)
brickArray.append(brick9)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(background)

    # Here the ball and the bar are appended onto the screen
    bar = pygame.draw.rect(screen, barColor, (xbar, ybar, xbarSize, ybarSize))
    ball = pygame.draw.circle(screen, ballColor, (xball, yball), 4)
    for i in brickArray:
        i.drawBrick()
    for i in brickArray:
        if xball >= i.xpos and xball <= i.xpos - i.xsize and yball > i.ypos and yball < i.ypos - i.ysize:
            print('Desmond, the moon bear')

    if timeWait:
        if timeWait2:
            timeWait = False
            timeWait2 = False
            time.sleep(1)
        timeWait2 = True
    # These statements rule over the ball hitting the bar, including the edge cases, wihch are labelled
    if yball <= ybar:  # overrideDisplacement makes sure that during edge cases, the ball always goes up
        overrideDisplacement = False
    if yball > ybar + 1 and yball < ybar + ybarSize:
        overrideDisplacement = True
    # Speed changes when ball hits vertical edges of bar
    if yball > ybar and yball < ybar + ybarSize and xball > xbar and xball < xbar + xbarSize:
        if overrideDisplacement:
            yballDisplacement = -abs(round(math.sin(40) * sideSpeed))  # ball always goes up
            xballDisplacement = round(math.cos(20) * cornerSpeed) * (xballDisplacement * (-1) / xballDisplacement)
            if xballDisplacement < 0:
                xballDisplacement = round(math.cos(20) * cornerSpeed)
            else:
                xballDisplacement = -xballDisplacement
        else:
            yballDisplacement = -yballDisplacement
    # These if statements make sure that the ball bounces off walls and the bar, correctly
    if yball < 1:
        yballDisplacement = -yballDisplacement
    if xball > 598:
        xballDisplacement = -xballDisplacement
    if xball < 1:
        xballDisplacement = -xballDisplacement
    if yball > 400:  # This is what happens when the ball goes out of the screen below
        xbar = 200
        ybar = 350

        xball = 230
        yball = 350
        xballDisplacement = round(math.cos(45) * 4)
        yballDisplacement = -round(math.sin(45) * 4)

        timeWait = True
    print(yball >= ybar)

    # This determines the side xyDisplacement when the ball hits left side of the bar
    if yball >= ybar and xball <= xbar + (0.3 * xbarSize) and xball >= xbar:
        xballDisplacement = round(math.cos(60) * sideSpeed)
        yballDisplacement = -abs(round(math.sin(40) * sideSpeed))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            xballDisplacement = round(math.cos(60) * sideSpeed) * -1

    # This determines the side xyDisplacement when the ball hits right side of the bar
    if yball >= ybar and xball <= xbar + xbarSize and xball >= xbar + 0.6 * xbarSize:
        xballDisplacement = round(math.cos(60) * sideSpeed)
        yballDisplacement = -abs(round(math.sin(40) * sideSpeed))

        #This allows the bar to change the direction of the ball depending on what you currently have pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            xballDisplacement = round(math.cos(60) * sideSpeed) * -1

    # This part allows you to move the bar
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            xbar -= barSpeed
        if event.key == pygame.K_RIGHT:
            xbar += barSpeed

    # These two lines allow for the ball to move one step at a time. Change the speed at the variables at the top
    xball += xballDisplacement
    yball += yballDisplacement

    fpsClocks.tick(speedClock)
    pygame.display.update()

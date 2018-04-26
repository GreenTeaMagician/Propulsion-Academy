import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("MichalSnake")

red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)

scrrenFill = screen.fill(blue)

x = 5
y = 5
xf = random.randint(0, 500)
yf = random.randint(0, 500)
state_direction = "down"
fpsClocks = pygame.time.Clock()
jump = 3
foodSize = 12
snakeSize = 25
snake_body = [pygame.Rect(400, 400, snakeSize, snakeSize)]
counter = 0
speed = 70
displacement = False
extraLength = False
extra2Length = False
a = 255
b = 0
c = 0

while True:
    for event in pygame.event.get():
        '''
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        '''
    screen.fill(blue)

    if x +snakeSize> 599:
        break
    if x < 1:
        break
    if y + snakeSize> 399:
        break
    if y < 1:
        break

    colorFood = pygame.Color(a, b, c)
    # snake = pygame.draw.rect(screen, red, (x, y, snakeSize, snakeSize))
    if len(snake_body) == 0:
        snake_body.append(snake)
    for i in snake_body:
        pygame.draw.rect(screen, red, i)
        print(str(i[0]) + ', ' + str(i[1]))
    for i in snake_body[:-1]:
        if i[0] == x and i[1] == y:
            break

    snake_body.append(pygame.Rect(x, y, snakeSize, snakeSize))
    snake_body.pop(0)

    food = pygame.draw.rect(screen, colorFood, (xf, yf, foodSize, foodSize))

    if event.type == pygame.QUIT:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and state_direction != "right":
            state_direction = "left"
        if event.key == pygame.K_RIGHT and state_direction != "left":
            state_direction = "right"
        if event.key == pygame.K_UP and state_direction != "down":
            state_direction = "up"
        if event.key == pygame.K_DOWN and state_direction != "up":
            state_direction = "down"

    if state_direction == "left":
        x -= jump
    if state_direction == "right":
        x += jump
    if state_direction == "up":
        y -= jump
    if state_direction == "down":
        y += jump

#    if extra2Length:
 #       snake_body.append(pygame.draw.rect(screen, red, (x, y, snakeSize, snakeSize)))
  #      extra2Length = False
   # if extraLength:
    #    snake_body.append(pygame.draw.rect(screen, red, (x, y, snakeSize, snakeSize)))
     #   extraLength = False
      #  extra2Length = True
    if xf <= x + snakeSize and xf + foodSize >= x and yf <= y + snakeSize and yf + foodSize >= y:
        print(len(snake_body))
        displacement = True
        snake_body.append(pygame.draw.rect(screen, red, (x, y, snakeSize, snakeSize)))
        xf = random.randint(50, 500)
        yf = random.randint(50, 300)
        print(speed)
        xdissize = 0
        ydissize = 0
        a = random.randint(0, 150)
        b = random.randint(0, 150)
        c = random.randint(0, 150)
        extraLength = True
    fpsClocks.tick(speed)
    pygame.display.update()

print('Haha, you lost, loser. Go home!')
print(f'Your score is: {len(snake_body)}')
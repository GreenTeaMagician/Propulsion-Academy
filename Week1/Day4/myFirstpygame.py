import pygame
import sys
import Inheritance.House
import Inheritance.Shapes
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("MyGame")

red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 255, 0)

screen.fill(white)
x = 0
fpsClocks = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(blue)
	x += 4
	if x > 700:
		x = 0
	pygame.draw.rect(screen, red, (x, 500, 100, 50))
	pygame.display.update()
	fpsClocks.tick(10)

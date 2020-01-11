import pygame, sys
from pygame.locals import *

X_SIZE = 1000
Y_SIZE = 800

pygame.init()
DISPLAY = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption('Pong')

pygame.key.set_repeat(1, 10)
fpsClock = pygame.time.Clock()

class Kulka:
	def __init__(self, x, y, vel_x, vel_y):
		self.x = x
		self.y = y
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.image = pygame.image.load('ball.png')
		self.image = pygame.transform.scale(self.image, (40, 40))
kulka = Kulka(X_SIZE/2, Y_SIZE/2, 6, 6)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				#cos sie stanie	
	DISPLAY.fill((0, 0, 0))
	kulka.x += kulka.vel_x
	kulka.y += kulka.vel_y
	#sufit
	if kulka.y<0:
		kulka.vel_y *= -1
		
	DISPLAY.blit(kulka.image, (kulka.x, kulka.y))
	pygame.display.update()
	fpsClock.tick(30)
	

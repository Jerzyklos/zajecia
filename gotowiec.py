import pygame, sys
from pygame.locals import *
import random

X_SIZE = 400
Y_SIZE = 400

pygame.init()
DISPLAY = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption('Snake')

obrazek_tla = pygame.image.load('siatka_czarna.png')

fpsClock = pygame.time.Clock()
FPS = 7

#stwórz klasę ElementWęża - jej składowe i metody będą na tablicy
#tak się wczytuje obrazek
#self.image = pygame.image.load('nazwa.jpg')
#self.image = pygame.transform.scale(self.image, (20, 20))

#stwórz klasę Wąż - jej składowe i metody będą na tablicy

#stworz klase Ciastko, bardzo podobną do ElementWeza

class ElementWeza:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = pygame.image.load('czerwony.jpg')
		self.image = pygame.transform.scale(self.image, (20, 20))

class Waz:
    def __init__(self):
        self.cialo = [ElementWeza(0,0), ElementWeza(20,0), ElementWeza(40,0)]
        self.predkosc_x = 20
        self.predkosc_y = 0
    def RuszSie(self):
        self.cialo.pop()
        element = ElementWeza(self.cialo[0].x+self.predkosc_x, self.cialo[0].y+self.predkosc_y)
        self.cialo.insert(0, element)
    def UstawPredkosc(self, predkosc_x, predkosc_y):
        self.predkosc_x = predkosc_x
        self.predkosc_y = predkosc_y
    def ZwrocCialo(self):
        return self.cialo
    def Wydluz(self):
        element = ElementWeza(self.cialo[0].x+self.predkosc_x, self.cialo[0].y+self.predkosc_y)
        self.cialo.insert(0, element)
class Ciastko:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = pygame.image.load('niebieski.png')
		self.image = pygame.transform.scale(self.image, (20, 20))

waz = Waz()
ciastko = Ciastko(200, 200)
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                waz.UstawPredkosc(0, 20)
                #naciśnięty guzik w dół
                #zrobić resztę guzików
                pass
            if event.key == K_UP:
                waz.UstawPredkosc(0, -20)
            if event.key == K_LEFT:
                waz.UstawPredkosc(-20, 0)
            if event.key == K_RIGHT:
                waz.UstawPredkosc(20, 0)
    DISPLAY.fill((0, 0, 0))
    
    DISPLAY.blit(obrazek_tla, (0,0))
    #wywolaj waz.Update() - zeby wąż się ruszył
    #zabierz listę elementów węża wywołując metodę waz.ZwrocElementy(), i przejdz po niej for-em, wyświetlając elementy
    if ciastko.x == waz.cialo[0].x and ciastko.y == waz.cialo[0].y:
        waz.Wydluz()
        ciastko.x = random.randint(0, 19)*20
        ciastko.y = random.randint(0, 19)*20
    else:
        waz.RuszSie()
    lista = waz.ZwrocCialo()
    for element in lista:
        DISPLAY.blit(element.image, (element.x, element.y))
    DISPLAY.blit(ciastko.image, (ciastko.x, ciastko.y))
    
    pygame.display.update()
    fpsClock.tick(FPS)

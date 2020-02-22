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
#tak się wczytuje obrazek:
#self.image = pygame.image.load('nazwa.jpg')
#self.image = pygame.transform.scale(self.image, (20, 20))

class ElementWeza:
	pass

#stwórz klasę Wąż - jej składowe i metody będą na tablicy

class Waz:
    def __init__(self):
        pass
    def Rusz(self):
        pass
    def UstawPredkosc(self, predkosc_x, predkosc_y):
        pass
    def ZwrocCialo(self):
        pass
    def Wydluz(self):
        pass

#stworz klase Ciastko, bardzo podobną do ElementWeza(będzie się różnić tylko kolorem)

#stworz zmienną typu wąż i jedno ciastko
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                #naciśnięty guzik w dół
                #zrobić resztę guzików

    DISPLAY.fill((0, 0, 0))
    DISPLAY.blit(obrazek_tla, (0,0))

    #wywolaj waz.Rusz() - zeby wąż się ruszył
    #jeśli wąż zjadł ciastko, wywołaj waz.Wydluz()
    #zabierz listę elementów węża wywołując metodę waz.ZwrocElementy(), i przejdz po niej for-em, wyświetlając elementy

    #DISPLAY.blit(ciastko.image, (ciastko.x, ciastko.y)) #tak się wyświetla element
    
    pygame.display.update()
    fpsClock.tick(FPS)

import pygame, sys
from pygame.locals import *
from math import sqrt

class Statek:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('spaceship.jpg')
        self.image = pygame.transform.scale(self.image, (80, 80))

#tutaj zrób klasę Pocisk, wzoruj się na klasie Statek. Dodaj im pole speed, czyli ma mieć x, y, speed
#tutaj zrób klasę Kosmita. ma mieć x,y i speed. Zrób też klasę KosmitaBoss z innym obrazkiem. 
#KosmitaBoss ma mieć też zmienną zycie, równą 5

FPS = 30
fpsClock = pygame.time.Clock()
X_SIZE = 1000
Y_SIZE = 800

pygame.init()
pygame.key.set_repeat(1, 10)
DISPLAY = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption('Space war')

statek = Statek(X_SIZE - 40, Y_SIZE-60)
pociski = [] #pusta lista wystrzelonych pocisków 
kosmici = [] #pusta lista kosmitów
kosmita_boss = KosmitaBoss(X_SIZE/2 - 100, 20, 2) #5 to speed

#tutaj tworzymy kosmitów - nie ruszać tego kodu
for i in range(10):
    kosmici.append(Kosmita(i*X_SIZE/10, 225, 2))
for j in range(0,3):
    for i in range(4):
        kosmici.append(Kosmita(i*X_SIZE/10, 40 + 60*j, 2))
    for i in range(4):
        kosmici.append(Kosmita((9-i)*X_SIZE/10, 40 + 60*j, 2))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass #tutaj przesuń statek w lewo(zmniejsz x)
        if keys[pygame.K_RIGHT]:
            pass #tutaj przesuń statek w prawo(zwiększ x)
        if keys[pygame.K_SPACE]:
            pass #tutaj strzelamy! dodaj do listy pociski nowy pocisk, używając polecenia append

	for pocisk in pociski:
	    pass #tutaj update pocisków. zmień ich y(x nie zmieniaj) o ich prędkość.
	#rusz kosmitów i kosmitę bossa
	#sprawdź, czy rakieta trafiła kosmitę, jeśli tak, usuń go z listy.
	#sprawdź osobno, czy trafiła bossa. Jeśli tak, odejmij mu życie
	#sprawdź, czy żaden kosmita nie doleciał do statku(y równe Y_SIZE-60-wysokość_kosmity)

    #sprawdzenie, czy pocisk wyleciał poza ekran
    for pocisk in pociski:
        if pocisk.y<0:
            pociski.remove(pocisk)

    DISPLAY.fill((255,255,255))
    DISPLAY.blit(statek.image, (statek.x, statek.y))
    DISPLAY.blit(kosmita_boss.image, (kosmita_boss.x, kosmita_boss.y))

    pygame.display.update()
    fpsClock.tick(FPS)


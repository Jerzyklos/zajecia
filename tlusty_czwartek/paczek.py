import turtle
from random import randint, choice

obrazek = 'paczek.gif'

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor('lightblue')
screen.addshape(obrazek)

zolw1 = turtle.Turtle()
zolw1.color('red')
zolw1.pensize(3)
zolw1.speed(3)

zolw2 = turtle.Turtle()
zolw2.shape(obrazek)
zolw2.penup()

zolw3 = turtle.Turtle()
zolw3.shape(obrazek)
zolw3.penup()

czcionka = ('Courier', 15, 'bold')
#z tej listy wyrazów będziemy losować
slowa_zolwia = ['pączek', 'pączunio', 'pączur']

while True:
    #tak losujemy słowo! slowo = choice(slowa_zolwia) 
    #w ten sposób żółw idzie w losowe miejsce! zolw.setpos(randint(-230, 230), randint(-230,230))
    #tak piszemy słowo: zolw.write(slowo, font=czcionka)
    
    #zadania dla zolw1
    #1. podnieś długopis(penup)
    #2. idź w losowe miejsce
    #3. opuść długopis
    #4. napisz wylosowane słowo

    #zadania dla zolw2 i zolw3
    #1. idź w losowo wylosowane miejsce. I tyle!



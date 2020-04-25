from tkinter import *
import turtle

window = Tk()
window.title("Rysowanie")

pole_tekstowe = Entry(window, width=20)
pole_tekstowe.grid(column=0, row=0)

def RysujKwadrat():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor('lightblue')
    zolw = turtle.Turtle()
    zolw.color('red')
    zolw.pensize(3)
    zolw.speed(3)
    a = int(pole_tekstowe.get())
    i=0
    while i<4:
        zolw.forward(a)
        zolw.left(90)
        i+=1
    
guzik1 = Button(window, text="Rysuj kwadrat 2D", command=RysujKwadrat, width=20)
guzik1.grid(column=0, row=1)

def RysujKolo():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor('lightblue')
    zolw = turtle.Turtle()
    zolw.color('red')
    zolw.pensize(3)
    zolw.speed(3)
    a = int(pole_tekstowe.get())
    zolw.circle(a)
    
guzik2 = Button(window, text="Rysuj koło 2D", command=RysujKolo, width=20)
guzik2.grid(column=0, row=2)

def RysujKwadrat3D():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor('lightblue')
    zolw = turtle.Turtle()
    zolw.color('red')
    zolw.pensize(3)
    zolw.speed(3)
    print('rysuje kwadrat 3D')

guzik3 = Button(window, text="Rysuj kwadrat 3D", command=RysujKwadrat3D, width=20)
guzik3.grid(column=0, row=3)

def RysujProstokat3D():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor('lightblue')
    zolw = turtle.Turtle()
    zolw.color('red')
    zolw.pensize(3)
    zolw.speed(3)
    print('rysuje prostokąt 3D')

guzik4 = Button(window, text="Rysuj prostokąt 3D", command=RysujProstokat3D, width=20)
guzik4.grid(column=0, row=4)

def RysujTrojkat3D():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor('lightblue')
    zolw = turtle.Turtle()
    zolw.color('red')
    zolw.pensize(3)
    zolw.speed(3)
    print('rysuje trojkat 3D')

guzik5 = Button(window, text="Rysuj trójkąt 3D", command=RysujTrojkat3D, width=20)
guzik5.grid(column=0, row=5)

window.mainloop()











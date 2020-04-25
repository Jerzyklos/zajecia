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
    print('rysuje koło')
    
guzik2 = Button(window, text="Rysuj koło 2D", command=RysujKolo, width=20)
guzik2.grid(column=0, row=2)

# Zad. 0. Dopisz w funkcji RysujKolo() rysowanie koła.

# Zad. 1. Dodaj kolejny guzik do rysowania kwadratu 3D. Skopiuj kod do rysowania z poprzednich zadań.
# Zrób najpierw funkcję RysujKwadrat3D(), później guzik.

# Zad. 2. Dodaj kolejny guzik do rysowania prostokąta 3D. Skopiuj kod do rysowania z poprzednich zadań.
# Zrób najpierw funkcję RysujProstokat3D(), później guzik.

# Zad. 3. Dodaj kolejny guzik do rysowania trójkąta 3D. Skopiuj kod do rysowania z poprzednich zadań.
# Zrób najpierw funkcję RysujProstokat3D(), później guzik.

window.mainloop()











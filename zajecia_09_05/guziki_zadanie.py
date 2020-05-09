from tkinter import *
import turtle

# PRZYPOMNIENIE
# tak się pobiera dane z pola tekstowego
#
# a = pole_tekstowe.get()

#tak się otwiera plik:
#
# with open(sciezka) as plik:
#   plik.read() 

window = Tk()
window.title("Rysowanie")

pole_tekstowe_sciezka = Entry(window, width=20)
pole_tekstowe_sciezka.grid(column=1, row=0)

var = StringVar()
label = Label(window, textvariable=var, relief=RAISED )
var.set('Ścieżka do pliku')
label.grid(column=0, row=0)

pole_tekstowe_dane = Entry(window, width=20)
pole_tekstowe_dane.grid(column=1, row=1)

var = StringVar()
label = Label(window, textvariable=var, relief=RAISED )
var.set('Dane')
label.grid(column=0, row=1)

def WyswietlPlikWKonsoli():
    # Zad. 1. Wyświetl zawartość pliku w konsoli
    # Po otwarciu pliku użyj funkcji read() albo readlines()
    pass

guzik1 = Button(window, text="Wyświetl plik w konsoli", command=WyswietlPlikWKonsoli, width=20)
guzik1.grid(column = 0, row=2, columnspan = 2)

def DodajLinijkeDoPliku():
    # Zad. 2. Dodaj linijkę do pliku (doklej)
    # Po otwarciu pliku użyj funkcji read() i write() - uważaj na nadpisanie pliku
    pass

guzik2 = Button(window, text="Dodaj linijkę do pliku", command=DodajLinijkeDoPliku, width=20)
guzik2.grid(column = 0, row=3, columnspan = 2)

def SkasujZawartoscIWklejLinie():
    # Zad3. Skasuj zawartość pliku i wklej zamiast niej nową linijkę.
    # Po otwarciu pliku użyj funkcji write()
    pass

guzik3 = Button(window, text="Zastąp zawartość ilnijką", command=SkasujZawartoscIWklejLinie, width=20)
guzik3.grid(column = 0, row=4, columnspan = 2)

def SkasujZawartoscPliku():
    # Zad4. Skasuj zawartość pliku.
    # Po otwarciu pliku użyj funkcji write()
    pass

guzik4 = Button(window, text="Skasuj zawartość pliku", command=SkasujZawartoscPliku, width=20)
guzik4.grid(column = 0, row=5, columnspan = 2)

def StworzNowyPlik():
    # Zad 5. Stwórz nowy plik. EZ
    pass

guzik5 = Button(window, text="Stwórz nowy plik", command=StworzNowyPlik, width=20)
guzik5.grid(column = 0, row=6, columnspan = 2)

def RysujKwadrat():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor('lightblue')
    zolw = turtle.Turtle()
    zolw.color('red')
    zolw.pensize(3)
    zolw.speed(3)
    i=0
    while i<4:
        zolw.forward(100)
        zolw.left(90)
        i+=1


guzik10 = Button(window, text="Rysuj (jak Ci się nudzi)", command=RysujKwadrat, width=20)
guzik10.grid(column = 0, row=7, columnspan = 2)








# tutaj inicjalizujemy żółwia:

zolw = turtle.Turtle()
zolw.color('red')
zolw.pensize(3)
zolw.speed(3)
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('lightblue')

#tutaj ściąga:
#zolw.forward(100) # idź do przodu o sto pikseli
#zolw.right(90) # skręć w prawo o 90 stopni
#zolw.left(90) # skręć w lewo o 90 stopni
#zolw.penup() # podnieś pióro (przestań pisać)
#zolw.pendown() # obniż pióro (zacznij pisać)

#zolw.xcor() # zwraca nam X żółwia
#zolw.ycor() # zwraca nam Y żółwia
#zolw.pos() # zwraca nam X i Y żółwia

#zolw.setpos(10, 10) # każemy iść żółwiowi na (10, 10)

#startowe_x = zolw.xcor() # współrzędna x żółwia
#startowe_y = zolw.ycor() # współrzędna y żółwia

#ze wskazowkami od dolnego lewego rogu
#kolejne_x = [startowe_x, startowe_x, startowe_x+a, startowe_x+a]
#kolejne_y = [startowe_y, startowe_y+a, startowe_y+a, startowe_y]

# Zad. 1. Każ żółwiowi iść na pozycję (100, 100) i narysuj tam kwadrat.

# Zad. 2. Narysuj dwie skośne linie: jedną zacznij od punktu (50, 50), drugą od (100, 50)

# Zad. 3. Narysuj kwadrat 3D.

# Zad. 4. Narysuj prostokąt 3D.

# Zad. 5. Narysuj trójkąt 3D. Wskazówka: skręcaj za każdym razem o 120 stopni w lewo.

# Zad. 6. Przenieś każde rysowanie do osobnej funkcji.

# *Zad. 7. Przenieś całe rysowanie do klasy Zolw.

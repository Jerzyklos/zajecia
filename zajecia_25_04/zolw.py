

zolw = turtle.Turtle()
zolw.color('red')
zolw.pensize(3)
zolw.speed(3)

#najważniejsze metody
zolw.forward(100) # idź do przodu o sto pikseli
zolw.right(90) # skręć w prawo o 90 stopni
zolw.left(90) # skręć w lewo o 90 stopni
zolw.penup() # podnieś pióro (przestań pisać)
zolw.pendown() # obniż pióro (zacznij pisać)

zolw.xcor() # zwraca nam X żółwia
zolw.ycor() # zwraca nam Y żółwia
zolw.pos() # zwraca nam X i Y żółwia

zolw.setpos(10, 10) # każemy iść żółwiowi na (10, 10)

startowe_x = zolw.xcor() # współrzędna x żółwia
startowe_y = zolw.ycor() # współrzędna y żółwia


#ze wskazowkami od dolnego lewego rogu
kolejne_x = [startowe_x, startowe_x, startowe_x+a, startowe_x+a]
kolejne_y = [startowe_y, startowe_y+a, startowe_y+a, startowe_y]

i=0
while i<4:
    zolw.penup()
    zolw.left(30)  # skierujmy go w dobra strone do rysowania ukośnych linii
    zolw.setpos(kolejne_x[i], kolejne_y[i])
    self.zolw.pendown()
    self.zolw.forward(25)
    self.zolw.right(30) #skierujmy go z powrotem na proste linie

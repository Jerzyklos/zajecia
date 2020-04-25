from tkinter import *

window = Tk()

listbox = Listbox(window)
listbox.pack()

listbox.insert(END, "element listy") # dodajemy element do listy

for item in ["pierwszy element", "drugi element", "trzeci element"]:
    listbox.insert(END, item)

mainloop()

# Zad. 1. Wyświetl listę 10 kolejnych liczb.

# Zad. 2. Wyświetl listę linijek z pliku plik.txt

# *Zad. 3. Dodaj opcję dodawania elementu do pliku.

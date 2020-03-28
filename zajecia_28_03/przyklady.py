from tkinter import *
# 1
"""
window = Tk()
window.title("Nasza aplikacja")
window.geometry('350x200')
window.mainloop()
"""


# 2
"""
window = Tk()
window.title("Nasza aplikacja")
window.geometry('350x200')

tekst = Label(window, text="Gitara siema")
# albo tekst = Label(window, text="Hello", font=("Arial Bold", 50))
tekst.grid(column=0, row=0)
window.mainloop()
"""

# 3

"""
window = Tk()
window.title("Nasza aplikacja")
window.geometry('350x200')

tekst = Label(window, text="Gitara siema")
tekst.grid(column=0, row=0)

guzik = Button(window, text="Kliknij")
guzik.grid(column=1, row=0)

window.mainloop()
"""

# 4
"""
window = Tk()
window.title("Nasza aplikacja")
window.geometry('350x200')

tekst = Label(window, text="Guzik nie kliknięty")
tekst.grid(column=0, row=0)

def guzik_klikniety():
    tekst.configure(text='Kliknięto guzik')
    
guzik = Button(window, text="Kliknij", command=guzik_klikniety)
guzik.grid(column=1, row=0)

window.mainloop()
"""
# 5
"""
window = Tk()
window.title("Nasza aplikacja")
window.geometry('350x200')

tekst = Label(window, text="Witaj anonie")
tekst.grid(column=0, row=0)

pole_tekstowe = Entry(window, width=10)
pole_tekstowe.grid(column=0, row=1)

def guzik_klikniety():
    tekst.configure(text='Witaj ' + pole_tekstowe.get())
    
guzik = Button(window, text="Kliknij", command=guzik_klikniety)
guzik.grid(column=1, row=0)

window.mainloop()
"""










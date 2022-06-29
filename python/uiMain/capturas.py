from textwrap import fill
from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT, scrolledtext,StringVar
import os
import pathlib

class Capturas(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window=window
        self._p3=Frame(self)
        self._p4=Frame(self)
        self._next_el = 0
        saludo=Entry(self._p3,width=100,fg="red")
        self.saludo2 = scrolledtext.ScrolledText(self._p3,height=5)
        self.saludo2.tag_configure("center", justify="center")
        saludo.insert(INSERT, "Bienvenido al software adaptado de XGames")
        self.saludo2.insert(INSERT, 'Xgames es una empresa especialista en venta y distribucion de videojuegos.En los ultimos años la compañia se ha centrado principalmente en vender sus juegos de forma digital.Por lo que surge esta aplicacion con el objetivo de una mejor gestion del proceso de ventas de manera digital.Dentro de esta aplicacion se lleva cuenta de todo el proceso de compra de los videojuegos,bdesde el cliente que lo compra, hasta el dinero que recibe la empresa y los desarrolladores del juego.')
        saludo.grid()
        self._p3.pack(fill="both")
        saludo.pack()
        

        def botonPrincipal():
          from ventana_usuario import ventana_principal 
          self.window.destroy()
          ventana_principal()
          

        self._pantallazos = []
        for i in range(0, 5):
            path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'python/elementos/pantallazo_{0}.png'.format(i))
            pantallazo = PhotoImage(file=path)
            self._pantallazos.append(pantallazo)
        
        

        self._label = Label(self._p4, image=self._pantallazos[0], height=500, width=750)
        self._label.bind('<Enter>', self.proximo)
        self._label.pack()
        self._p4.pack(anchor="s")


        button = Button(self._p4, text="Ventana Principal del Admin", command=botonPrincipal)
        button.pack(anchor="s")
        
    def proximo(self, _):
        if self._next_el < 4:
            self._next_el = self._next_el + 1
        else:
            self._next_el = 0

        self._label.configure(image=self._pantallazos[self._next_el])
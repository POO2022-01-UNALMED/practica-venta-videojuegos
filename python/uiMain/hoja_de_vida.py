from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT
import os
import pathlib

class HojaVida(Frame):
    _posicion_imagen = [(0, 0), (0, 1), (1, 0), (1, 1)]
    def __init__(self, window):
        super().__init__(window)
        self._p5 = Frame(self)
        self._p6 = Frame(self)
        self._text = None
        self._num = 0
        self._labels = []
        self.cargar_txt(0)
        for i in range(0, 4):
            label = Label(self._p6, width=250, height=200)
            (r, c) = HojaVida._posicion_imagen[i]
            label.grid(row=r, column=c)
            self._labels.append(label)
            self.cargar_imagen(0, i)
        self._p5.grid()
        self._p6.grid()

    # Se usa para mostrar la hoja de vida que sigue, aumentando el atributo next_hv
    def proximo(self, _):
        if self._num < 3:
            self._num = self._num + 1
        else:
            self._num = 0
        self.cargar_txt(self._num)
        for i in range(0, 4):
            self.cargar_imagen(self._num, i)

    # Carga el component imagen que sirve para mostrar las fotos
    def cargar_imagen(self, num, num2):
        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'python/elementos/imagen_{0}_{1}.png'.format(num, num2))
        photo = PhotoImage(file=path)
        self._labels[num2].configure(image=photo)
        self._labels[num2].image = photo
    
    # Carga el texto para la hoja de vida respecto al numero asignado 
    def cargar_txt(self, numero):
        self._text = Text(self._p5, height=10)
        self._text.grid(row=1, column=0)
        self._text.bind('<Button-1>', self.proximo)

        path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(), 'python/elementos/descripcion{0}.txt'.format(numero))

        with open(path, "r+") as text:
            self._text.insert(INSERT, text.read())

  
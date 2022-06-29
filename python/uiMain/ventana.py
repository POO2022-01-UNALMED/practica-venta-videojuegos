from tkinter import Tk,Menu
from .capturas import Capturas
from .hoja_de_vida import HojaVida
from baseDatos.deserializador import Deserializador
class ventanaInicio(Tk):
  def __init__(self):
    super().__init__()
    self.title('Xgames')
    self.option_add("*tearOff",  False)
    self.menubar= Menu(self)
    inicio = Menu(self.menubar)
    inicio.add_command(label= "Descripcion", command = lambda: self.capturas.saludo2.pack()) 
    inicio.add_command(label = "Salir", command=lambda: self.destroy())
    Deserializador.deserializarTodo()
    self.menubar.add_cascade(label="Inicio", menu=inicio)
    self.config(menu=self.menubar)
    self.capturas = Capturas(self)
    self.hoja_vida = HojaVida(self)
    self.capturas.grid(row=0, column=0)
    self.hoja_vida.grid(row=0, column=1)


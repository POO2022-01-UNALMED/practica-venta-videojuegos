import tkinter as tk
from uiMain.ventana import ventanaInicio
from baseDatos.deserializador import Deserializador
if __name__ == "__main__":
    print()
    Deserializador.deserializarTodo()
    ventana_inicio = ventanaInicio()
    ventana_inicio.mainloop()



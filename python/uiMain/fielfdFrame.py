import tkinter as Tk
from tkinter import Frame,Label,StringVar,Entry,DISABLED,Button
from .negative_exception import NegativeException
from .number_exception import NumberException
from .empty_exception import EmptyException

class FieldFrame(Frame):
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, tipos):
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        self._entries = list()
        self._tipos = tipos
        super().__init__(master)
        self.actualizacion()
        self._aceptar=None
        self._borrar=None
    
    def actualizacion(self):
        Label(self, text=self._tituloCriterios).grid(padx = 80, column = 0, row = 0)
        Label(self, text=self._tituloValores).grid(padx = 80, column = 1, row = 0)
        for i in range(1, len(self._valores)+1):
            Label(self, text=self._criterios[i-1]).grid(padx = 80, pady=2, column=0, row=i)
            if self._criterios[i-1] in self._habilitado:
                texto = StringVar(value=self._valores[i-1])
                entrada = Entry(self, width = 40, textvariable=texto, state=DISABLED, justify="center")
            else:
                texto = StringVar(value=self._valores[i-1])
                entrada = Entry(self, width = 40, textvariable=texto, justify="center")
        
            entrada.grid(pady =2, column=1, row=i)
            self._entries.append(entrada)


    def validacion(self):

      criteriosFaltantes=[]
      valoresNegativos=[]
      valoresErroneos=[]
      vacio=False
      for i in range(len(self._valores)):
        self._valores[i] = self._entries[i].get()
        if self._valores[i]=="":
          criteriosFaltantes.append(self._criterios[i])
          vacio=True
      for e in range(len(self._valores)):
         if self._tipos[e]==0:
          if self._entries[e].get().isdigit():
            valoresErroneos.append(self._criterios[e])
         if self._tipos[e]==1:
          if vacio==False:
            if  int(self._entries[e].get())<0:
              valoresNegativos.append(self._criterios[e])
        
      if len (criteriosFaltantes)>0:
        faltantes = ", ".join(criteriosFaltantes)
        raise EmptyException("Los siguientes campos faltan por rellenar: " + faltantes)
      elif len(valoresErroneos)>0:
        erroneos = ", ".join(valoresErroneos)
        raise NumberException("En los siguientes campos se ingresaron valores incorrectos: " + erroneos)
      elif len(valoresNegativos)>0:
        negativos = ", ".join(valoresNegativos)
        raise NegativeException("En los siguientes campos se ingresaron valores numericos negativos: " + negativos)
    
    def borrarEntry(self):
        for entrada in self._entries:
            entrada.delete(0, "end")
        
    def getValue(self, criterio):
        criterios_dict = dict(zip(self._criterios, self._valores))
        return criterios_dict[criterio]

    def crearBotones(self,comando):
        aceptar = Button(self, text="Aceptar",command=comando).grid(pady = 50, column = 0, row = len(self._criterios)+1)
        self._aceptar=aceptar
        borrar = Button(self, text="Borrar",command=self.borrarEntry).grid(pady = 50, column = 1, row = len(self._criterios)+1)
        self._borrar=borrar
    

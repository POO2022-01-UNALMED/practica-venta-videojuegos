
class Persona:
    
    #	  
    #	  Descripcion: la clase Persona fue pensada para ser la clase padre
    #	  de empleado y cliente, asi se podra ahorrar codigo
    #

    personas = []	  

    def __init__(self, tarjeta=0, nombre="", documento="", edad=0):
        self._tarjeta = tarjeta
        self._nombre = nombre
        self._documento = documento
        self._edad = edad
        Persona.personas.append(self)
    
    def descripcion(self):
        return self._nombre+"\n" +"Edad: "+str(self._edad)+"\n"

    # Gets y sets de la clase

    def getTarjeta(self):
        return self._tarjeta
    def setTarjeta(self, tarjeta):
        self._tarjeta=tarjeta


    def getNombre(self):
        return self._nombre +"y soy persona"
    def setNombre(self, nombre):
        self._nombre=nombre


    def getDocumento(self):
        return self._documento
    def setDocumento(self, documento):
        self._documento=documento


    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad=edad
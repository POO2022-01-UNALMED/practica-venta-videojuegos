class Videojuego:

    #  
    #	Descripcion: la clase Videojuego guarda todas las caracteriticas de los videojuegos,
    #  esta sera una clase importante(la empresa se basa en la venta de estos) 
    #  auque por sí sola no haga mucho
    #	

    videojuegos = []

    def __init__(self, genero, nombre, precio, valoracion, desarrollador, clasificacion, numValoraciones):
        self._genero=genero
        self._nombre= nombre
        self._precio=int(precio)
        self._valoracion=int(valoracion)
        self._desarrollador=desarrollador
        self._clasificacion=clasificacion
        self._numValoraciones=int(numValoraciones)
        self._valorado=False
        Videojuego.videojuegos.append(self)

    #  
    #  Parametros: Cliente
    #	Descripcion:revisa que haya una compatibilidad entre la edad del cliente y la clasificacion del juego que desea comprar, para que un cliente no adquiera un juego que no tiene permitido adquirir
    #  return: boolean
    #	

    def verificarEdad(self, Cliente):
        if self._clasificacion == "+18" and Cliente.getEdad()>17:
            return True
        elif self._clasificacion == "+16" and Cliente.getEdad()>15:
            return True
        elif self._clasificacion == "+12" and Cliente.getEdad()>11:
            return True
        elif self._clasificacion == "+7" and Cliente.getEdad()>6:
            return True
        elif self._clasificacion == "+3" and Cliente.getEdad()>2:
            return True
        else:
            return False


    #  
    #	Todos los get y sets de la clase
    #	

    def setValoracion(self, valoracion):
        self._valoracion=valoracion
    def setGenero(self, genero):
        self._genero=genero
    def setNombre(self, nombre):
        self._nombre=nombre
    def setPrecio(self, precio):
        self._precio=precio
    def setDesarrollador(self, desarrollador):
        self._desarrollador=desarrollador
    def setClasificacion(self, clasificacion):
        self._clasificacion=clasificacion
    def setNumValoraciones(self, numValoraciones):
        self._numValoraciones=numValoraciones
    def getGenero(self):
        return self._genero
    def getNombre(self):
        return self._nombre
    def getPrecio(self):
        return self._precio
    def getValoracion(self):
        return self._valoracion
    def getDesarrollador(self):
        return self._desarrollador
    def getClasificacion(self):
        return self._clasificacion
    def getNumValoraciones(self):
        return self._numValoraciones
    def setValorado(self, f):
        self._valorado=f
    def getValorado(self):
        return self._valorado
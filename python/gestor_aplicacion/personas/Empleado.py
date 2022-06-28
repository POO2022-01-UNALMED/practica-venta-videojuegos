
import random
from ..gestion.tarjeta import Tarjeta
from ..gestion.Rango import Rango
from ..gestion.catalogo import Catalogo
from ..gestion.Empresa  import Empresa
from ..personas.Persona import Persona
from ..gestion.Videojuego import Videojuego
from ..gestion.Desarrollador import Desarrollador
from uiMain.ciente_nf_exception import ClienteException
from uiMain.rango_exception import RangoException
class Empleado(Persona):

    #	Descripcion: la clase Empleado hereda de Persona; esta clase busca
    #	describir el comportamiento de un empleado, este se encargara del manejo
    #	de todo el manejo tecnico de la empresa: Edicion en el catalogo de videojuegos y desarrolladores
    #	ademas se encargara tambien de vender
    #		





    def __init__(self, nom="", doc=0, edad=0, tar=0, sueldo=0, cargo=0, ventas=0):
        
        super().__init__(tar,nom,doc,edad)
        self._sueldo = sueldo
        self._cargo = cargo
        self._ventas=ventas
        if self._nombre!="":
            Empresa.getListaEmpleados().append(self)


    #
    #	Parametros: void
    #	Descripcion: se crea una descripcion del empleado
    #	Return:String
    #	

    def descripcion(self):
        return super().descripcion()+"Ventas: "+str(self._ventas)+"\n"+ "Saldo Tarjeta: "+str(self.getTarjeta().getSaldo())+"\n"


    #	
    #	Parametros: String
    #	Descripcion: verificar si un desarrollador se encuentra en la lista de desarrolladores autorizados por la empresa
    #	Return: boolean
    #	

    def verificarDesarrollador(self, nombre):
        for i in Empresa.getListaDesarrolladores():
            if i.getNombre()==nombre:
                return True
        return False

    #	
    #	Parametros: Videojuego
    #	Descripcion: Añadir un videojuego al catalogo o no, depediendo si ya esta en el
    #	Return: funcion añadirVideojuegos(String,String,double,String,String)
    #			

    '''def anadirVideojuegos(self, videojuego):
        return self.anadirVideojuegos(videojuego.getGenero(),videojuego.getNombre(),videojuego.getPrecio(),videojuego.getDesarrollador().getNombre(),videojuego.getClasificacion())
'''
    #	
    #	Parametros: String,String,double,String,String
    #	Descripcion: Añadir un videojuego al catalogo o no, depediendo si ya esta en el
    #	Return: String
    #			

    def anadirVideojuegos(self, genero, nombre, precio, desarrollador, clasificacion):
        #verifica si el juego ya existe en el catalogo
        y =Catalogo.verificarExistencia(nombre)
        if y == True:
            return "Videojuego ya existe"
        #si efectivamente ya existe retorna que ya existe

        #caso contrario, verificara si el desarrollador esta en la lista de autorizados por la empresa
        w =self.verificarDesarrollador(desarrollador)
        if w == False:
            #si no lo esta: creara un videojuego con un desarrollador generico,como un juego Indie**
            d = desarrollador
            videojuego = Videojuego(genero,nombre,precio,0,d,clasificacion,0)
            d.getVideojuegos().append(videojuego)
            Catalogo.getVideojuegos().append(videojuego)

            #se añade al catalogo y retorna:  									
            return "Videojuego exitosamente añadido a catalogo"

        #si el desarrollador si esta en nuestra lista:
        for i in Empresa.getListaDesarrolladores():
            if i is desarrollador:
                #se encuentra el desarrollador
                e = Videojuego(genero,nombre,precio,0,i,clasificacion,0)
                Catalogo.getVideojuegos().append(e)

                #se añade el juego con su correspondiente desarrollador
                return "Videojuego exitosamente añadido a catalogo"
        return "" #return comodin:NUNCA SE EJECUTARA ESTE RETURN,SOLO SE NECESITA PARA QUE COMPILE BIEN


    #	
    #	Parametros: String
    #	Descripcion: Buscara el nombre(unico) del videojuego, si lo encuentra lo eliminara y retornara un mensaje,
    #	en caso contrario retornara que el videojuego no se encontro
    #	Return: String
    #	

    def eliminarVideojuego(self, nombre):
        if Catalogo.verificarExistencia(nombre) == False:
            return "Videojuego no encontrado"
        i = 0
        while i < Catalogo.getVideojuegos().size():
            if Catalogo.getVideojuegos().get(i).getNombre() is nombre:
                Catalogo.getVideojuegos().remove(i)
                return "Videojuego encontrado y eliminado"
            i += 1
        return "" #return comodin:NUNCA SE EJECUTARA ESTE RETURN,SOLO SE NECESITA PARA QUE COMPILE BIEN


    #	
    #	Parametros: double, String
    #	Descripcion: Buscara el nombre(unico) del videojuego, si lo encuentra cambiara su precio y retornara un mensaje de exito, 
    #	en caso contrario retornara el mensaje que no lo encontro
    #	Return: String
    #	

    def modificarPrecio(self, precio, nombre):
        if (Catalogo.verificarExistencia(nombre) == True):
            for i in Catalogo.getVideojuegos():
                if i.getNombre()==nombre:
                    i.setPrecio(precio)
                    return "Precio Cambiado"
        return "Videojuego no encontrado"

    #
    #	Parametros: long, 
    #	Descripcion: Se buscara al cliente y se le cambiara su rango, adicionalmente se le regalara un juego
    #	Return: String
    #	


    def descuentoEspecial(self, documento):
        for cliente in Empresa.getListaClientes():
            if cliente.getDocumento()==documento:
                #se verifica que el client exista
                if cliente.getRango()==Rango.ESPECIAL:
                    #Se verifica si ya tiene el rango
                    raise RangoException("No se puede asignar rango especial a este cliente")
                    return "El cliente ya tiene el rango"
                cliente.setRango(Rango.ESPECIAL)
                if len(Catalogo.getVideojuegos()) != 0:
                    #se verifica si el catalogo esta vacio, dificil regalr un juego si no lo hay aun
                    numero = int((random.random()*len(Catalogo.getVideojuegos())))
                    #se crea un numero aleatorio entero
                    nombre1 =Catalogo.getVideojuegos()
                    nombre=nombre1[numero].getNombre()
                    for videojuego in cliente.getBiblioteca():
                        if (videojuego.getNombre() is nombre )== True:
                            return "Se ha reasignado el descuento especial pero no se ha tenido suerte con el juego"
                    v =nombre1[numero]
                    vv = Videojuego(v.getGenero(),v.getNombre(), v.getPrecio(),0, v.getDesarrollador(), v.getClasificacion(), 0)
                    cliente.setRango(Rango.ESPECIAL) #Se asigna el rango
                    cliente.getBiblioteca().append(vv) #se añade a la biblioteca
                    return "Se ha dado el descuescuento especial y se ha regalado el juego: "+Catalogo.getVideojuegos()[numero].getNombre()
                cliente.setRango(Rango.ESPECIAL)
                return "Se ha reasignado el descuento especial pero no se ha tenido suerte con el juego"
        raise ClienteException("Cliente no encontrado")
        return "Cliente no encontrado"

    #	
    #	Parametros: null, 
    #	Descripcion: se rebajara 10% el sueldo del empleado
    #	Return: void
    #	


    def rebajarsueldo(self):
        self._sueldo=self._sueldo*0.9


    #	
    #	Todos los get y sets de la clase
    #	

    def getSueldo(self):
        return self._sueldo
    def setSueldo(self, sueldo):
        self._sueldo=sueldo

    def getVentas(self):
        return self._ventas
    def setVentas(self, ventas):
        self._ventas=ventas

    def getCargo(self):
        return self._cargo
    def setCargo(self):
        return self._cargo
    def getNombre(self):
        return self._nombre

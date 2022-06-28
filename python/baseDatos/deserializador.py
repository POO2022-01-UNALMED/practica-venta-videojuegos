import pickle
from gestor_aplicacion.gestion.Desarrollador import Desarrollador
from gestor_aplicacion.gestion.Empresa import Empresa
from gestor_aplicacion.gestion.Videojuego import Videojuego
from gestor_aplicacion.gestion.catalogo import Catalogo
from gestor_aplicacion.gestion.tarjeta import Tarjeta
from gestor_aplicacion.personas.Persona import Persona
from gestor_aplicacion.gestion.Dian import Dian
import pathlib
import os

class Deserializador():
    
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()
        return lista
    
    def deserializarTodo():
        Desarrollador.desarrolladores = Deserializador.deserializar(Desarrollador.desarrolladores, "Desarrolladores")
        #Empresa.empresas =  Deserializador.deserializar(Empresa.empresas, "Empresas")
        Videojuego.videojuegos = Deserializador.deserializar(Videojuego.videojuegos, "Videojuegos")
        Empresa._listaClientes = Deserializador.deserializar(Empresa._listaClientes, "Clientes")
        Catalogo.catalogos = Deserializador.deserializar(Catalogo.catalogos, "Catalogos")
        Tarjeta.tarjetas = Deserializador.deserializar(Tarjeta.tarjetas, "Tarjetas")
        Persona.personas = Deserializador.deserializar(Persona.personas, "Personas")
        Empresa._listaEmpleados = Deserializador.deserializar(Empresa._listaEmpleados, "Empleados")
        Catalogo._videojuegos=Deserializador.deserializar(Catalogo._videojuegos, "Videojuegos catalogo")
        Empresa. _tarjeta=Deserializador.deserializar(Empresa.tarjeta(),"Tarjeta empresa")
        Empresa._listaDesarrolladores=Deserializador.deserializar(Empresa.getListaDesarrolladores(),"Desarrolladores Empresa")
        Dian._tarjeta=Deserializador.deserializar(Dian.tarjetal(),"Tarjeta Dian")

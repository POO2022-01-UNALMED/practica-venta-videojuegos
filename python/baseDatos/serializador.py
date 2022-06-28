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
class Serializador():
    
    def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        try:
            # Creo el archivo pickle para guardar los objetos
            picklefile = open(camino(className), 'wb')
            # pickle el objeto en el archivo
            pickle.dump(lista, picklefile)
            # cierro el archivo para guardar
            picklefile.close()
            
        except:
            print("paila tuqui tuqui muneco")

    def serializarTodo():

        Serializador.serializar(Desarrollador.desarrolladores, "Desarrolladores")
        #Empresa.empresas =  Deserializador.deserializar(Empresa.empresas, "Empresas")
        Serializador.serializar(Videojuego.videojuegos, "Videojuegos")
        Serializador.serializar(Empresa._listaClientes, "Clientes")
        Serializador.serializar(Catalogo.catalogos, "Catalogos")
        Serializador.serializar(Tarjeta.tarjetas, "Tarjetas")
        Serializador.serializar(Persona.personas, "Personas")
        Serializador.serializar(Empresa._listaEmpleados, "Empleados")
        Serializador.serializar(Catalogo._videojuegos, "Videojuegos catalogo")
        Serializador.serializar(Empresa.tarjeta(),"Tarjeta empresa")
        Serializador.serializar(Empresa.getListaDesarrolladores(),"Desarrolladores Empresa")
        Serializador.serializar(Dian.tarjetal(),"Tarjeta Dian")
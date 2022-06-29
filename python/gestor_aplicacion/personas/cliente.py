from ..personas.Persona import Persona
from ..gestion.Rango import Rango
from ..gestion.Empresa import Empresa
from ..gestion.catalogo import Catalogo
from ..gestion.Videojuego import Videojuego
from uiMain.not_found_exception import NotFoundException
from uiMain.cash_exception import CashException
from uiMain.number_exception import NumberException
'''
    Descripcion: La clase Cliente que hereda de Persona esta pensada para almacenar la biblioteca de videjuegos del cliente,
	  tambien desde esta clase, el cliente podra ver el catalogo de la empresa, comprar los videojuegos que desee, y finalmente,
	  calificar los videojuegos que haya comprado.
    '''

class Cliente(Persona):
    def __init__(self,nom="",doc=0,edad=0,tar=0,historialcompra=0,biblioteca=None):
        super().__init__(tar,nom,doc,edad)
        if biblioteca==None:
            self._biblioteca=[]
        self._historialCompra=historialcompra
        self._rango=Rango.NORMAL
        if self._nombre!="":
            Empresa.getListaClientes().append(self)


    '''
    Parametros: String, double
	   Descripcion: Califica un videojuego que este dentro de la biblioteca del cliente
	   Return: String
    '''

    def calificarVideojuego(self,nombre,cal):
        #Primero se revisa que la calificacion este en un rango adecuado
        if(0<=cal and cal<=10):
            #Luego se revisa si el cliente tiene el videojuego en su biblioteca
            for v in self._biblioteca:
                #Este condicional confirma que efectivamente lo tiene
                if (v.getNombre()==nombre):
                    if v.getValorado()==False:
                        v.setValorado(True)
                        '''
                        Ahora en este ciclo comprobamos que el juego siga en el catalogo, para que la valoracion pueda tener repercusion en sus compras,
						ya que si no esta igual no estaria a la venta

                        '''
                        for u in Catalogo.getVideojuegos():
                            #Este condicional comprueba que siga en el catalogo
                            if u.getNombre()==nombre:
                                # En estos cuatro se esta promediando la calificacion
                                c=(u.getValoracion()*u.getNumValoraciones())+cal
                                c=c/(u.getNumValoraciones()+1)
                                u.setValoracion(c)
                                #Finalmente suma una valoracion mas al videojuego
                                u.setNumValoraciones(u.getNumValoraciones()+1)

                                return "Se ha valorado exitosamente"
                    return "Ya has valorado este videojuego"
            raise NotFoundException("Videojuego no encontrado")
            return "No puede valorar ya que no se ha comprado el videojuego o no se encuentra en el catalogo"
        raise NumberException("La calificacion ingresada no esta permitida")
        return "Valoracion no permitida"
    

    '''
    Descripcion: Este metodo es utilizado para que el cliente pueda ver todo el catalogo de videojuegos disponibles
	Return: String  
    '''

    def verCatalogo(self):
        c=""
        for i in Catalogo.getVideojuegos():
            c=c+"Nombre: "+i.getNombre()+"\n"+"Genero: "+i.getGenero()+"\n"+"Desarrollador: "+i.getDesarrollador().getNombre()+"\n"+"Valoracion: "+str(i.getValoracion())+"\n"+"Precio: "+str(i.getPrecio())+"\n"+"---------------------------------"+"\n"
        return c
    

    '''
    Parametros: String
	Descripcion: Comprueba que un videojuego este en la biblioteca del cliente
	 Return: boolean
    '''

    def comprobarVideojuego(self,name):
        for v in self._biblioteca:
            if v.getNombre()==name:
                return True
        return False
    

    '''
    Parametros: String
	Descripcion: Este metodo busca y compra un videojuego del catalogo mediante la tarjeta del cliente para luego a�adirlo a su biblioteca
	Return: String
    '''

    def comprarVideojuego(self,nombre):
        if self.comprobarVideojuego(nombre)==False:
            x=Catalogo.verificarExistencia(nombre)
            #Verifica que el videojuego existe
            if x==True:
                for i in Catalogo.getVideojuegos():
                    #Luego busca el videojuego requerido en el catalogo
                    if i.getNombre()==nombre:
                        if i.verificarEdad(self)==False:
                            return "No tienes edad suficiente"
                        y=self._tarjeta.pagarVideojuego(i,self)
                        if y==True:
                            n=Videojuego(i.getGenero(),i.getNombre(),i.getPrecio(),0,i.getDesarrollador(),i.getClasificacion(),0)
                            
                            self._biblioteca.append(n)
                            self._historialCompra+=1
                            return "Compra exitosa"
                        if y==False:
                            raise CashException("Dinero insuficiente para realizar la compra")
                            return "Saldo insuficiente"
            if x==False:
                raise NotFoundException("Videojuego no encontrado")
                return "Videojuego no existe"
        return "Ya posees este videojuego"
    


    def juegos(self):
        s=""
        for v in self._biblioteca:
            s=s+v.getNombre()+"\n"
        return s

    '''
    gets y sets de la clase
    '''

    def setBiblioteca(self,b):
        self._biblioteca=b
    
    def getBiblioteca(self):
        return self._biblioteca

    def getRango(self):
        return self._rango
    
    def setRango(self,rango):
        self._rango=rango
    
    def getNombre(self):
        return self._nombre

    def getTarjeta(self):
        return self._tarjeta
    
    def getDocumento(self):
        return self._documento
    






from ..gestion.Empresa import Empresa






'''
	Descripcion: la clase Tarjeta permite la manipulacion y verificacion del dinero
    esta es primordial para todo lo relacionado con la venta hacia clientes y el pago hacia empleados
'''
class Tarjeta:
    tarjetas=[]
    def __init__(self,numero=0,saldo=0):
        self._numero=numero
        self._saldo=saldo
        Tarjeta.tarjetas.append(self)

    '''
    Todos los get y sets de la clase
    '''

    def getNumero(self):
        return self._numero

    def setNumero(self,numero):
        self._numero=numero

    def getSaldo(self):
        return self._saldo

    def setNumero(self,numero):
        self._saldo=numero

    def setSaldo(self,x):
        self._saldo=x


    '''
    Los metodos ingresar y retirar permiten la manipulacion del saldo de la tarjeta
    con una simplificacion de codigo
    '''

    def ingresar(self,x):
        self._saldo=self._saldo+x

    def retirar(self,x):
        self._saldo=self._saldo-x

    '''
        Parametros: Videojuego, Cliente
        Descipcion: el metodo pagarVideojuego permite a un cliente pagar por un videojuego(en caso que tenga el dinero para hacerlo)
        y al comprarlo deposita la comision el la Tarjeta del desarrollador y el resto se deposita en
        la tarjeta de la empresa
        Return: boolean
    '''

    def pagarVideojuego(self,juego,cliente):
        #si puede pagar el videojuego
        if (juego.getPrecio()<=cliente.getTarjeta().getSaldo()):
            for d in Empresa.getListaDesarrolladores():
                if(d.getNombre()==juego.getDesarrollador().getNombre()):
                    #el cliente paga
                    cliente.getTarjeta().retirar(juego.getPrecio()*(1-cliente.getRango().value))
                    #se paga al desarrollador su comision
                    juego.getDesarrollador().getTarjeta().ingresar(juego.getDesarrollador().getComision()*juego.getPrecio())
                    #la empresa ingresa el dinero restante
                    Empresa.getTarjeta().ingresar(juego.getPrecio()*(1-cliente.getRango().value)-(juego.getDesarrollador().getComision()*juego.getPrecio()))
                    return True
            #En caso que el desarrollador no haya pagado a la compañia por vender su videojuego
            #se depositara todo el dinero que haya pagado el cliente en la Tarjeta de la empresa
            cliente.getTarjeta().retirar(juego.getPrecio()*(1-cliente.getRango().value))
            Empresa.getTarjeta().ingresar(juego.getPrecio()*(1-cliente.getRango().value))
            return True
        else:
            return False




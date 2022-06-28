from ..gestion.Dian import Dian




    #    Descrición: La clase desarrollador es un agente externo que se encarga de de venderle a la empresa los videojuegos que esta desarrolle,
    #    este cobrará un pequeño porcentaje de lo que la empresa de venta de videojuegos venda a cada cliente, su objetivo es nutrir el catálogo de videojuegos
    #    con su método principal solicitarIngresoJuego.


class Desarrollador(Dian):
    desarrolladores = []
    def __init__(self,nombre,tarjeta,comision,videojuegos=None):
        self._videojuegos=videojuegos
        if self._videojuegos==None:
            self._videojuegos=[]
        self._nombre = nombre
        self._tarjeta = tarjeta
        self._comision = int(comision)
        Desarrollador.desarrolladores.append(self)

    #    
    #    
    #    Todos los get y set de la clase
    #    

    def getComision(self):
        return self._comision
    def setComision(self, comision):
        self._comision = comision
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre=nombre
    def getTarjeta(self):
        return self._tarjeta
    def setTarjeta(self, tarjeta):
        self._tarjeta=tarjeta
    def getVideojuegos(self):
        return self._videojuegos
    def setVideojuegos(self, v):
        self._videojuegos=v


    #    Parámetros:Videojuego
    #    Descripción:solicitarIngresoJuego es método que interactua con la clase empresa, este va a ingresar un objeto tipo videojuego de su catálogo y el desarrollador, posteriormente llamará aceptarIngresoVideojuego.
    #    Return: void
    #     
    def solicitarIngresoJuego(self):
        from ..gestion.Empresa import Empresa
        Empresa.aceptarIngresoVideojuego(self) #Aplicará el metodo de empresa aceptarIngresoVideojuego y en este entrará en evaluacion para ver si es rentable en la empresa, si lo es, lo agregará al catálogo.


    #    Parametros:null
    #      Descripcion: este metodo calcula la cantidad de impuestos que debe pagarle el desarrollador al gobierno
    #      Return: String

    def calcularImpuesto(self):
        m =self.getTarjeta().getSaldo()
        return "Se debe pagar " +str(m*self._IMPUESTO)

    #    Parametros:null
    #      Descripcion: este metodo paga los impuestos que el desarrollador le debe al gobierno por sus ganancias
    #      Return: void

    def pagarImpuesto(self):
        m =self.getTarjeta().getSaldo()
        self.getTarjeta().retirar(m*self._IMPUESTO)
        Dian.getTarjeta1().ingresar(m*self._IMPUESTO)

    def pagarEmpleadoOJuego(self):
        for v in self._videojuegos:
            self.getTarjeta().retirar(v.getPrecio()*0.1)
            Dian.getTarjeta1().ingresar(v.getPrecio()*0.1)
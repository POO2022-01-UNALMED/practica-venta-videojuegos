from ..gestion.Gobierno import Gobierno

class Dian(Gobierno):
    _IMPUESTOS=0.2
    #Descrición: La clase Dian es abstracta y de ella se heredan Empresa y Desarrollador
    _tarjeta = []
    #Este metodo obliga a la empresa y a los desarrolladores a pagar el impuesto calculado por el gobierno
    def pagarImpuesto(self):
        pass

    #Este metodo obliga a la empresa y a los desarrolladores a pagar el impuesto calculado por sus juegos o empleados
    def pagarEmpleadoOJuego(self):
        pass
    
    #Todods los get y set
    @classmethod
    def tarjetal(cls):
        return cls._tarjeta
    @classmethod
    def tarjetal2(cls,t):
        cls._tarjeta=t

    @classmethod
    def getTarjeta1(cls):
        return cls._tarjeta[0]
    @staticmethod
    def setTarjeta1(cls,tarjeta):
        cls._tarjeta[0] = tarjeta

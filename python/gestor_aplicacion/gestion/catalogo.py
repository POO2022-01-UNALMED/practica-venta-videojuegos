
'''
    Descripcion: Esta clase guardara TODOS los videojuegos que vende la empresa
'''

class Catalogo:
    _videojuegos=[]
    catalogos=[]
    def __init__(self):
        Catalogo.catalogos.append(self)

    '''
    Parametros: String
	Descripcion: verificar si el videojuego consultado existe en el catalogo
	Return: boolean
    '''
    @classmethod
    def verificarExistencia(cls,nombre):
        for v in Catalogo._videojuegos:
            if(v.getNombre()==nombre):
                return True
        return False
    
    '''	
    Todos los get y sets de la clase
    '''

    @classmethod
    def getVideojuegos(cls):
        return cls._videojuegos

    @classmethod
    def setVideojuegos(cls,x):
        cls._videojuegos=x



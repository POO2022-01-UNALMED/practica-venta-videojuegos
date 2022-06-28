

import math

from ..gestion.Dian import Dian
class Empresa(Dian):
    
    _SERIALVERSIONUID = 1

    _listaEmpleados = []
    _listaDesarrolladores = []
    _listaClientes = []
    _tarjeta = []
    _BONIFICACION =500 #bonificacion que se implementara en el metodo revision
    _IMPUESTO =0.2 #Porcentaje de impuestos
    VENTASMINIMAS =20 #este atributo tiene como objetivo poner un minimo de ventas que debe hacer un empleado durante un mes para evaluar su rendimiento
    VENTASMAYORES =70 #este atributo tiene como objetivo imponer un numero de ventas a partir del cual se puede premiar un empleado o grupo de ellos por su rendimiento
 

    #	
    #	Descripcion:la clase Empresa se encarga de todo lo relacionado con la gestion del personal y de los recursos de la empresa, en este caso desde esta clase podremos despedir,ascender, contratar nuevos empleados o evaluar su rendimiento, agregar nuevos juegos al catalogo de la empresa cuyos desarrolladores solicitan la posibilidad de ingresarlo. En particular como solo tenemos que gestionar esta empresa, esta clase tiene todos sus atributos estaticos, ya que esta clase no esta disenada para tener varias instancias
    #	 

    #		
    #    Todos los get y set
    #    


    @classmethod
    def setListaClientes(cls,lista):
        cls._listaClientes=lista
    @classmethod
    def getListaClientes(cls):
        return Empresa._listaClientes

    @staticmethod
    def setListaEmpleados(listaEmpleados):
        Empresa._listaEmpleados=listaEmpleados
    @staticmethod
    def setListaDesarrolladores(listaDesarrolladores):
        Empresa._listaDesarrolladores=listaDesarrolladores


    @staticmethod
    def setTarjeta(tarjeta):
        Empresa._tarjeta=tarjeta

    @staticmethod
    def getListaEmpleados():
        return Empresa._listaEmpleados
    @staticmethod
    def getListaDesarrolladores():
        return Empresa._listaDesarrolladores
    @staticmethod
    def tarjeta():
        return Empresa._tarjeta
    @staticmethod
    def getTarjeta():
        return Empresa._tarjeta[0]

    #	
    #	Parametros: Persona, Long, String
    #	Descripcion: Crear un objeto empleado y anadirlo a la lista de empleados de la empresa
    #	Return: void
    #	 
    @staticmethod
    def contratarEmpleado(persona, sueldo, cargo):
        from..personas.Empleado import Empleado
        empleado = Empleado(persona.getNombre(),persona.getDocumento(),persona.getEdad(),persona.getTarjeta(),sueldo,cargo) #creamos un empleado de la clase Empleado, con los atributos que hereda de pertenecer a la clase Persona y los parametros sueldo y cargo requeridos en el metodo
    @staticmethod
    def contratarEmpleadoEmpleado(nom, doc, edad, sueldo, tar, cargo, ventas):
        from..personas.Empleado import Empleado
        empleado = Empleado(nom, doc, edad, tar, sueldo, cargo, ventas)

    #	
    #	Parametros: Empleado
    #	Descripcion: Sacamos de la lista empleados de la empresa al empleado que se ingresa como parametro
    #	Return: void
    #	 
    @staticmethod
    def despedirEmpleado(empleado):
        for e in Empresa._listaEmpleados:
            if e.getDocumento()==empleado.getDocumento():
               Empresa._listaEmpleados.remove(e) #Si  encontramos  al empleado que ingresa como parametro, lo eliminamos de la lista de empleados de la empresa y eliminamos la referencia del empleado


    #	
    #	Parametros: Empleado, String, long
    #	Descripcion: le damos un nuevo cargo y un nuevo sueldo al empleado ingresado como parametro si efectivamente pertenece a la lista de empoleados de la empresa
    #	Return: void
    #	 
    def ascenderEmpleado(self, empleado, cargo, sueldo):
        if empleado in Empresa._listaEmpleados:
            empleado.setSueldo(sueldo)
            empleado.setCargo(cargo)

    #	
    #	Parametros: Desarrollador, Videojuego
    #	Descripcion: si el desarrollador cobra una comision que no sea tan alta para vender su videojuego en la tienda, ingresamos el videojuego al catologo por medio de un objeto temporal de tipo empleado y devolvemos un boolean true si finalmente se ingreso
    #return: boolean
    #	 
    @staticmethod
    def aceptarIngresoVideojuego(desarrollador):
        from..personas.Empleado import Empleado
        if desarrollador.getComision()<=0.4:
            wwww = Empleado() #instancia temporal de tipo empleado

            for d in Empresa._listaDesarrolladores:
                if d.getNombre()==desarrollador.getNombre():
                    for videojuego in desarrollador.getVideojuegos():
                        wwww.anadirVideojuegos(videojuego) #le agrgamos su nuevo videojuego
                    return True
            Empresa._listaDesarrolladores.append(desarrollador) #si no estaba asociado previamente lo ingresamos a la lista de desarrolladores y anadimos su juego a la tienda
            for videojuego in desarrollador.getVideojuegos():
                wwww.anadirVideojuegos(videojuego)
            return True
        return False

    #	
    #	Parametros: void
    #	Descripcion: paga a todos los empleados su sueldo del mes correspondiente
    #return: String
    #	 
    @staticmethod
    def pagarEmpleados():
        if len(Empresa.getListaEmpleados()) == 0:
            return "No has contratado a nadie aun"
        x =0 #variable temporal para sumar el sueldo de los empleados
        for e in Empresa._listaEmpleados:
            x=x+(e.getSueldo())+(e.getSueldo()*0.1)
        if x> Empresa.getTarjeta().getSaldo():
            return "No hay saldo suficiente y no se ha pagado los impuestos"
        for e in Empresa._listaEmpleados:
            Empresa.getTarjeta().retirar(e.getSueldo()+e.getSueldo()*0.1) #caso contrario se retira el dinero de la tarjeta de la empresa y se paga a todos los empleados
            e.getTarjeta().ingresar(e.getSueldo())
            Dian.getTarjeta1().ingresar(e.getSueldo()*0.1)
        return "El pago se realizo satisfactoriamente" #retorna esto

    #	
    #	Parametros: void
    #	Descripcion: reinicia el conteo de ventas de el mes, para iniciar el mes siguiente con la cuenta en cero y poder implementar correctamente el metodo revisionMensual
    #	return: String
    #	 
    @staticmethod
    def resetearVentas():
        for e in Empresa._listaEmpleados:
            e.setVentas(0)
        return "Se ha reiniciado el numero de ventas"

    #	
    #	Parametros: void
    #	Descripcion:revisa el desempeno de los empleados con 2 objetivos principales,rebajar un 10% el sueldo a los que no alcancen un minimo de ventas y premiar a los empleados que superan un buen numero de ventas
    #	return: String
    #	 

    
    @staticmethod
    def revisionMensual():
        despedidos = [] #en esta variable temporal almacenamos los empleados que no llegaron al minimo de ventas
        mejoresVendedores = [] #en esta variable temporal almacenaremos a los candidatos a mejores vendedores este mes
        c ="" #variable temporal para no mezclar y generar posibles errores
        a ="" #variable temporal para no mezclar y generar posibles errores
        b ="" #variable temporal para no mezclar y generar posibles errores
        bb ="" #variable temporal para no mezclar y generar posibles errores
        for e in Empresa._listaEmpleados:
            if e.getVentas()>=Empresa.VENTASMAYORES:
                mejoresVendedores.append(e) #se añaden a una lista temporal
            if e.getVentas()<Empresa.VENTASMINIMAS:
                despedidos.append(e) #se añaden a una lista temporal

        if (len(despedidos) == 0) and (len(mejoresVendedores)) == 0:
            Empresa.resetearVentas() #se resetea las ventas
            #se retorna un mensaje
            return "No se ha bonificado a nadie y no se le ha reducido el sueldo a nadie"
        elif (len(despedidos) == 0) and (len(mejoresVendedores) != 0):
            Empresa.resetearVentas()
            if Empresa.getTarjeta().getSaldo()<Empresa._BONIFICACION:
                return "No se le ha bajado el sueldo a nadie y no se ha podido pagar la bonificacion" #se resetea las ventas
            for m in mejoresVendedores:
                m.getTarjeta().setSaldo(m.getTarjeta().getSaldo()+(math.trunc(Empresa._BONIFICACION / float(len(mejoresVendedores))))) #pago bonificacion equitativo
                c+=m.getNombre()+" "
            Empresa.getTarjeta().retirar(Empresa._BONIFICACION)
            #se retorna un mensaje
            return "No se le ha bajado el sueldo a nadie y se ha bonificado a: "+c
        elif (len(despedidos) != 0) and (len(mejoresVendedores) == 0):
            Empresa.resetearVentas() #se resetea las ventas
            for g in despedidos:
                a+=g.getNombre()+" "
                (g).rebajarsueldo() #rebajamos 10% su sueldo
            #se retorna un mensaje
            return "No se ha bonificado a nadie y se ha reducido el sueldo a: "+a

        else:
            Empresa.resetearVentas() #se resetea las ventas
            for w in despedidos:
                b+=w.getNombre()+" "
                (w).rebajarsueldo() #rebajamos 10% su sueldo
            if Empresa.getTarjeta().getSaldo()<Empresa._BONIFICACION:
              return "No se ha podido pagar la bonificacion y se ha rebajado el sueldo a: "+b
            for r in mejoresVendedores:
                bb+=r.getNombre()+" "
                r.getTarjeta().setSaldo(r.getTarjeta().getSaldo()+(math.trunc(Empresa._BONIFICACION / float(len(mejoresVendedores))))) #pago bonificacion equitativo

            Empresa.getTarjeta().retirar(Empresa._BONIFICACION)
            #se retorna un mensaje
            return "Se ha bonificado a: "+bb+" y se ha rebajado el sueldo a: "+b

#	Parametros:null
#      Descripcion: este metodo retorna informacion del empleado
#      Return: String
    @classmethod
    def revision(cls):
        c =""
        for e in Empresa._listaEmpleados:
            c+=e.descripcion()+"Sueldo: "+str((e).getSueldo())+"\n"+"------------------------------------------------------------------------"+"\n"
        return c

    #	Parametros:null
    #      Descripcion: este metodo calcula la cantidad de impuestos que debe pagarle la empresa al gobierno
    #      Return: String
    def calcularImpuesto(self):
        m =Empresa.getTarjeta().getSaldo()
        return "Se debe pagar " +str(m*Empresa._IMPUESTO)

    #	Parametros:null
    #      Descripcion: este metodo paga los impuestos que la empresa le debe al gobierno por sus ganancias
    #      Return: void
    def pagarImpuesto(self):
        m =Empresa.getTarjeta().getSaldo()
        Empresa.getTarjeta().retirar(m*Empresa._IMPUESTO)
        Dian.getTarjeta1().ingresar(m*Empresa._IMPUESTO)
    #Parametros:null
    #      Descripcion: este metodo paga los impuestos que la empresa le debe al gobierno por sus empleados
    #      Return: void
    def pagarEmpleadoOJuego(self):
        for e in Empresa._listaEmpleados:
            Dian.getTarjeta1().setSaldo(Dian.getTarjeta1().getSaldo()+e.getSueldo()*0.1)
            Empresa.getTarjeta().retirar(e.getSueldo()*0.1)


package gestorAplicacion.gestion;
import gestorAplicacion.personas.*;
import java.util.ArrayList;
import java.io.Serializable;
public class Empresa extends Dian implements Serializable,Gobierno{
	private static final long serialVersionUID = 1L;

	private static ArrayList<Empleado> listaEmpleados=new ArrayList<Empleado>();
	private static ArrayList<Desarrollador> listaDesarrolladores=new ArrayList<Desarrollador>();
	private static ArrayList<Cliente> listaClientes=new ArrayList<Cliente>();
	private static ArrayList<Tarjeta> tarjeta=new ArrayList<Tarjeta>();
	private static int BONIFICACION=500;//bonificacion que se implementara en el metodo revision
	private static double IMPUESTO=0.2;//Porcentaje de impuestos
	public final static int VENTASMINIMAS=20;//este atributo tiene como objetivo poner un minimo de ventas que debe hacer un empleado durante un mes para evaluar su rendimiento
	public final static int VENTASMAYORES=70;//este atributo tiene como objetivo imponer un numero de ventas a partir del cual se puede premiar un empleado o grupo de ellos por su rendimiento
	public static ArrayList<Empresa> empresas=new ArrayList<Empresa>();
	
	/*
	Descripcion:la clase Empresa se encarga de todo lo relacionado con la gestion del personal y de los recursos de la empresa, en este caso desde esta clase podremos despedir,ascender, contratar nuevos empleados o evaluar su rendimiento, agregar nuevos juegos al catalogo de la empresa cuyos desarrolladores solicitan la posibilidad de ingresarlo. En particular como solo tenemos que gestionar esta empresa, esta clase tiene todos sus atributos estaticos, ya que esta clase no esta disenada para tener varias instancias
	 */

	

	public Empresa(){
		empresas.add(this);}
		/*
    Todos los get y set
    */


	public static void setListaClientes(ArrayList<Cliente> lista){
		Empresa.listaClientes=lista;}
	public static ArrayList<Cliente> getListaClientes(){
		return listaClientes;}

	public static void setListaEmpleados(ArrayList<Empleado> listaEmpleados){
		Empresa.listaEmpleados=listaEmpleados;
	}
	public static void setListaDesarrolladores(ArrayList<Desarrollador> listaDesarrolladores){
		Empresa.listaDesarrolladores=listaDesarrolladores;
	}


	public static void setTarjeta(ArrayList<Tarjeta> tarjeta){
		Empresa.tarjeta=tarjeta;}

	public static ArrayList<Empleado> getListaEmpleados(){
		return listaEmpleados;
	}
	public static ArrayList<Desarrollador> getListaDesarrolladores(){
		return listaDesarrolladores;
	}
	public static ArrayList<Tarjeta> tarjeta(){
		return tarjeta;
	}
	public static Tarjeta getTarjeta(){//solo nos interesa la primera tarjeta, este es un arreglo para serializar la lista
		return tarjeta.get(0);
	}

	/*
	Parametros: Persona, Long, String
	Descripcion: Crear un objeto empleado y anadirlo a la lista de empleados de la empresa
	Return: void
	 */
	public static void contratarEmpleado(Persona persona,Long sueldo,String cargo){  
		Empleado empleado= new Empleado(persona.getNombre(),persona.getDocumento(),persona.getEdad(),persona.getTarjeta(),sueldo,cargo);//creamos un empleado de la clase Empleado, con los atributos que hereda de pertenecer a la clase Persona y los parametros sueldo y cargo requeridos en el metodo
	}
	public static void contratarEmpleadoEmpleado(String nom,long doc,int edad,double sueldo,long tar, String cargo,int ventas )  {
		Empleado empleado= new Empleado( nom, doc, edad, tar, sueldo,  cargo, ventas );}

	/*
	Parametros: Empleado
	Descripcion: Sacamos de la lista empleados de la empresa al empleado que se ingresa como parametro
	Return: void
	 */
	public static void despedirEmpleado(Empleado empleado){
		for (Empleado e: listaEmpleados){ 
			if (e.getDocumento()==empleado.getDocumento()){
				listaEmpleados.remove(e);//Si  encontramos  al empleado que ingresa como parametro, lo eliminamos de la lista de empleados de la empresa y eliminamos la referencia del empleado
				
				return;
			}
		}
	}

	/*
	Parametros: Empleado, String, long
	Descripcion: le damos un nuevo cargo y un nuevo sueldo al empleado ingresado como parametro si efectivamente pertenece a la lista de empoleados de la empresa
	Return: void
	 */
	public void ascenderEmpleado(Empleado empleado,String cargo, long sueldo){
		if(listaEmpleados.contains(empleado)){//verifica que el empleado si pertenezca a la empresa
			empleado.setSueldo(sueldo);
			empleado.setCargo(cargo);
		}
	}

	/*
	Parametros: Desarrollador, Videojuego
	Descripcion: si el desarrollador cobra una comision que no sea tan alta para vender su videojuego en la tienda, ingresamos el videojuego al catologo por medio de un objeto temporal de tipo empleado y devolvemos un boolean true si finalmente se ingreso
return: boolean
	 */
	public static boolean aceptarIngresoVideojuego(Desarrollador desarrollador){
		if (desarrollador.getComision()<=0.4){//verifica que la comision sea aceptable para ingresar el juego a la tienda
			Empleado wwww=new Empleado();//instancia temporal de tipo empleado

			for (Desarrollador d:listaDesarrolladores){
				if (d.getNombre().equals(desarrollador.getNombre())){//comprobamos si el desarrollador estaba asociado previamente a la empresa 
					for(Videojuego videojuego:desarrollador.getVideojuegos()) {
					wwww.anadirVideojuegos(videojuego);}//le agrgamos su nuevo videojuego
					return true;}
			}
			listaDesarrolladores.add(desarrollador) ;//si no estaba asociado previamente lo ingresamos a la lista de desarrolladores y anadimos su juego a la tienda
			for(Videojuego videojuego:desarrollador.getVideojuegos()) {
				wwww.anadirVideojuegos(videojuego);}
			return true;}
		return false;}

	/*
	Parametros: void
	Descripcion: paga a todos los empleados su sueldo del mes correspondiente
return: String
	 */
	public static String pagarEmpleados() {
		if(Empresa.getListaEmpleados().size()==0){
			return "No has contratado a nadie aun";
		}
		double x=0;//variable temporal para sumar el sueldo de los empleados
		for(Empleado e:listaEmpleados){
			x=x+(e.getSueldo())+(e.getSueldo()*0.1);}
		if (x>getTarjeta().getSaldo()) {//si los sueldos son mayores a el sueldo de la empresa, no puede pagar en este momento y por tanto retorna este mensaje
			return "No hay saldo suficiente y no se ha pagado los impuestos";}
		for(Empleado e:listaEmpleados) {
			getTarjeta().retirar(e.getSueldo()+e.getSueldo()*0.1);//caso contrario se retira el dinero de la tarjeta de la empresa y se paga a todos los empleados
			e.getTarjeta().ingresar(e.getSueldo());
		Dian.getTarjeta1().ingresar(e.getSueldo()*0.1);}
		return "El pago se realizo satisfactoriamente";}//retorna esto

	/*
	Parametros: void
	Descripcion: reinicia el conteo de ventas de el mes, para iniciar el mes siguiente con la cuenta en cero y poder implementar correctamente el metodo revisionMensual
	return: String
	 */
	public static String resetearVentas(){
		for (Empleado e:listaEmpleados){//con este ciclo for lo que hacemos es iterar sobre la lista de empleados y asignar como su valor de ventas 0, que es el valor con el que inicia el nuevo mes
			e.setVentas(0);
		}
		return "Se ha reiniciado el numero de ventas";
	}

	/*
	Parametros: void
	Descripcion:revisa el desempeno de los empleados con 2 objetivos principales,rebajar un 10% el sueldo a los que no alcancen un minimo de ventas y premiar a los empleados que superan un buen numero de ventas
	return: String
	 */

	public static String revisionMensual(){
		ArrayList<Empleado> despedidos=new ArrayList<Empleado>();//en esta variable temporal almacenamos los empleados que no llegaron al minimo de ventas
		ArrayList<Empleado> mejoresVendedores= new ArrayList<Empleado>();//en esta variable temporal almacenaremos a los candidatos a mejores vendedores este mes
		String c="";//variable temporal para no mezclar y generar posibles errores
		String a="";//variable temporal para no mezclar y generar posibles errores
		String b="";//variable temporal para no mezclar y generar posibles errores
		String bb="";//variable temporal para no mezclar y generar posibles errores
		for(Empleado e: listaEmpleados){
			if (e.getVentas()>=VENTASMAYORES){
				mejoresVendedores.add(e);//se añaden a una lista temporal
			}
			if(e.getVentas()<VENTASMINIMAS){
				despedidos.add(e);//se añaden a una lista temporal
			}

		}
		if(despedidos.size()==0 && mejoresVendedores.size()==0){
			resetearVentas();//se resetea las ventas
			//se retorna un mensaje
			return "No se ha bonificado a nadie y no se le ha reducido el sueldo a nadie";
		}
		else if(despedidos.size()==0 && mejoresVendedores.size()!=0){
			resetearVentas();
			if(Empresa.getTarjeta().getSaldo()<BONIFICACION){
				return "No se le ha bajado el sueldo a nadie y no se ha podido pagar la bonificacion";
			}//se resetea las ventas
			for(Persona m: mejoresVendedores){
				m.getTarjeta().setSaldo(m.getTarjeta().getSaldo()+(BONIFICACION/mejoresVendedores.size()));//pago bonificacion equitativo
				c+=m.getNombre()+" ";
			}
			Empresa.getTarjeta().retirar(BONIFICACION);
			//se retorna un mensaje
			return "No se le ha bajado el sueldo a nadie y se ha bonificado a: "+c;
		}
		else if(despedidos.size()!=0 && mejoresVendedores.size()==0){
			resetearVentas();//se resetea las ventas
			for(Persona g:despedidos){
				a+=g.getNombre()+" ";
				((Empleado)g).rebajarsueldo();//rebajamos 10% su sueldo
			}
			//se retorna un mensaje
			return "No se ha bonificado a nadie y se ha reducido el sueldo a: "+a;

		}
		else{
			resetearVentas();//se resetea las ventas
			for(Persona w: despedidos){
				b+=w.getNombre()+" ";
				((Empleado)w).rebajarsueldo();//rebajamos 10% su sueldo
			}
			for(Empleado r: mejoresVendedores){
				bb+=r.getNombre()+" ";
				r.getTarjeta().setSaldo(r.getTarjeta().getSaldo()+(BONIFICACION/mejoresVendedores.size()));//pago bonificacion equitativo

			}
			if(Empresa.getTarjeta().getSaldo()<BONIFICACION){
				return "No se ha podido pagar la bonificacion y se ha rebajado el sueldo a: "+b;}
			Empresa.getTarjeta().retirar(BONIFICACION);
			//se retorna un mensaje
			return "Se ha bonificado a: "+bb+" y se ha rebajado el sueldo a: "+b;

		}
		}
	/*Parametros:null
      Descripcion: este metodo retorna informacion del empleado
      Return: String*/
	public static String revision(){
		String c="";
		for(Persona e:listaEmpleados){
			c+=e.descripcion()+"Sueldo: "+((Empleado)e).getSueldo()+"\n"+"\n";}
		return c;}

	/*Parametros:null
      Descripcion: este metodo calcula la cantidad de impuestos que debe pagarle la empresa al gobierno
      Return: String*/
	public String  calcularImpuesto() {
		double m=Empresa.getTarjeta().getSaldo();
		return "Se debe pagar " +m*IMPUESTO;
		
	}
	
	/*Parametros:null
      Descripcion: este metodo paga los impuestos que la empresa le debe al gobierno por sus ganancias
      Return: void*/
	public void pagarImpuesto() {
		double m=Empresa.getTarjeta().getSaldo();
		Empresa.getTarjeta().retirar(m*IMPUESTO);	
		Dian.getTarjeta1().ingresar(m*IMPUESTO);
	}
/*Parametros:null
      Descripcion: este metodo paga los impuestos que la empresa le debe al gobierno por sus empleados
      Return: void*/
	public void pagarEmpleadoOJuego(){
		for(Empleado e:listaEmpleados){
			Dian.getTarjeta1().setSaldo(Dian.getTarjeta1().getSaldo()+e.getSueldo()*0.1);
			Empresa.getTarjeta().retirar(e.getSueldo()*0.1);

		}
	}
}
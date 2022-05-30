package gestorAplicacion.personas;
import gestorAplicacion.gestion.*;
import java.io.Serializable;
public class Empleado extends Persona implements Serializable{
	private static final long serialVersionUID = 1L;
	private double sueldo;
	private String cargo;
	private int ventas=0;//siempre se creara un empleado con ventas=0 ya que acaba de "comenzar" a trabajar
	/*
	Descripcion: la clase Empleado hereda de Persona; esta clase busca
	describir el comportamiento de un empleado, este se encargara del manejo
	de todo el manejo tecnico de la empresa: Edicion en el catalogo de videojuegos y desarrolladores
	ademas se encargara tambien de vender
	*/	

	public Empleado() {}
	public Empleado(String nom,long doc,int edad,long tar,double sueldo, String cargo,int ventas ){
		this(nom,doc,edad,new Tarjeta(tar),sueldo,"Vendedor",0);
	}

	public Empleado(String nom,long doc,int edad,Tarjeta tar,double sueldo, String cargo,int ventas ) {
		super(tar,nom,doc,edad);
		this.sueldo = sueldo;
		this.cargo = cargo;
		this.ventas=ventas;
		Empresa.getListaEmpleados().add(this);}

		public Empleado(String nom,long doc,int edad,Tarjeta tar,double sueldo, String cargo) {
			super(tar,nom,doc,edad);
			this.sueldo = sueldo;
			this.cargo = cargo;
			Empresa.getListaEmpleados().add(this);}
	
/*
	Parametros: void
	Descripcion: se crea una descripcion del empleado
	Return:String
	*/
	
	public String descripcion(){
		return super.descripcion()+"ventas "+ventas+"\n"+ "tarjeta "+this.getTarjeta().getSaldo()+"\n";}

	
	/*
	Parametros: String
	Descripcion: verificar si un desarrollador se encuentra en la lista de desarrolladores autorizados por la empresa
	Return: boolean
	*/

	public boolean verificarDesarrollador(String nombre) {
		for(Desarrollador i:Empresa.getListaDesarrolladores()) {
			if (i.getNombre().equals(nombre)){
				return true;}}
		return false;}
	
	/*
	Parametros: Videojuego
	Descripcion: Añadir un videojuego al catalogo o no, depediendo si ya esta en el
	Return: funcion añadirVideojuegos(String,String,double,String,String)
	*/		
	
	public String anadirVideojuegos(Videojuego videojuego) {
		return anadirVideojuegos(videojuego.getGenero(),videojuego.getNombre(),videojuego.getPrecio(),videojuego.getDesarrollador().getNombre(),videojuego.getClasificacion());}
	
	/*
	Parametros: String,String,double,String,String
	Descripcion: Añadir un videojuego al catalogo o no, depediendo si ya esta en el
	Return: String
	*/		
	
	public String anadirVideojuegos(String genero,String nombre,double precio,String desarrollador,String clasificacion) {
		//verifica si el juego ya existe en el catalogo
		boolean y=Catalogo.verificarExistencia(nombre);
		if (y==true) {
			return "Videojuego ya existe";}
		//si efectivamente ya existe retorna que ya existe

		//caso contrario, verificara si el desarrollador esta en la lista de autorizados por la empresa
		boolean w=this.verificarDesarrollador(desarrollador);
		if (w==false) {
			//si no lo esta: creara un videojuego con un desarrollador generico,como un juego Indie**
			Desarrollador d=new Desarrollador(desarrollador);
			Videojuego videojuego=new Videojuego(genero,nombre,precio,0,d,clasificacion,0);
			d.getVideojuegos().add(videojuego);
			Catalogo.getVideojuegos().add(videojuego);
			
			//se añade al catalogo y retorna:  									
			return "Videojuego exitosamente añadido a catalogo";}

		//si el desarrollador si esta en nuestra lista:
		for(Desarrollador i:Empresa.getListaDesarrolladores()) {
			if (i.getNombre().equals(desarrollador)) {
				//se encuentra el desarrollador
				Videojuego e=new Videojuego(genero,nombre,precio,0,i,clasificacion,0);
				Catalogo.getVideojuegos().add(e);
				
				//se añade el juego con su correspondiente desarrollador
				return "Videojuego exitosamente añadido a catalogo";}}
		return "";}//return comodin:NUNCA SE EJECUTARA ESTE RETURN,SOLO SE NECESITA PARA QUE COMPILE BIEN
	

	/*
	Parametros: String
	Descripcion: Buscara el nombre(unico) del videojuego, si lo encuentra lo eliminara y retornara un mensaje,
	en caso contrario retornara que el videojuego no se encontro
	Return: String
	*/
	
	public String eliminarVideojuego(String nombre) {
		if (Catalogo.verificarExistencia(nombre)==false) {
			return "Videojuego no encontrado";}
		for(int i = 0; i < Catalogo.getVideojuegos().size(); i++) {
			if(Catalogo.getVideojuegos().get(i).getNombre().equals(nombre)) {
				Catalogo.getVideojuegos().remove(i);
				return "Videojuego encontrado y eliminado";}}
		return "";}//return comodin:NUNCA SE EJECUTARA ESTE RETURN,SOLO SE NECESITA PARA QUE COMPILE BIEN
	

	/*
	Parametros: double, String
	Descripcion: Buscara el nombre(unico) del videojuego, si lo encuentra cambiara su precio y retornara un mensaje de exito, 
	en caso contrario retornara el mensaje que no lo encontro
	Return: String
	*/
	
	public String modificarPrecio(double precio,String nombre) {
		if (Catalogo.verificarExistencia(nombre)==true) {
			for(Videojuego i:Catalogo.getVideojuegos()) {
				if (i.getNombre().equals(nombre)) {
					i.setPrecio(precio);		
					return "Precio Cambiado";}}}
		return "Videojuego no encontrado";}
	
/*
	Parametros: long, 
	Descripcion: Se buscara al cliente y se le cambiara su rango, adicionalmente se le regalara un juego
	Return: String
	*/

	
	public String descuentoEspecial(long documento){
		for(Cliente cliente:Empresa.getListaClientes()){
			if(cliente.getDocumento()==documento){
				//se verifica que el client exista
				if(cliente.getRango()==Rango.ESPECIAL){
					//Se verifica si ya tiene el rango
					return "El cliente ya tiene el rango";}
				cliente.setRango(Rango.ESPECIAL);
				if(Catalogo.getVideojuegos().size()!=0){
					//se verifica si el catalogo esta vacio, dificil regalr un juego si no lo hay aun
					int numero = (int)(Math.random()*Catalogo.getVideojuegos().size());
					//se crea un numero aleatorio entero
					String nombre=Catalogo.getVideojuegos().get(numero).getNombre();
					for(Videojuego videojuego:cliente.getBiblioteca()){
						if (videojuego.getNombre().equals(nombre)==true){
							return "Se ha reasignado el descuento especial pero no se ha tenido suerte con el juego";}}
					Videojuego v=Catalogo.getVideojuegos().get(numero);
					Videojuego vv=new Videojuego(v.getGenero(),v.getNombre() , v.getPrecio(),0 , v.getDesarrollador(), v.getClasificacion(), 0);
					cliente.setRango(Rango.ESPECIAL);//Se asigna el rango
					cliente.getBiblioteca().add(vv);//se añade a la bivlioteca
					return "Se ha dado el descuescuento especial y se ha regalado el juego: "+Catalogo.getVideojuegos().get(numero).getNombre();}
				cliente.setRango(Rango.ESPECIAL);
				return "Se ha reasignado el descuento especial pero no se ha tenido suerte con el juego";}			}
			
		return "Cliente no encontrado";}

	/*
	Parametros: null, 
	Descripcion: se rebajara 10% el sueldo del empleado
	Return: void
	*/


	public void rebajarsueldo(){
		this.sueldo=sueldo*0.9;
	}


	/*
	Todos los get y sets de la clase
	*/
	
	public double getSueldo() {
		return this.sueldo;}
	public void setSueldo(double sueldo) {
		this.sueldo=sueldo;}
	
	public int getVentas() {
		return ventas;}
	public void setVentas(int ventas) {
		this.ventas=ventas;}
	
	public String getCargo() {
		return cargo;}
	public void setCargo(String cargo) {
		this.cargo=cargo;}
	public String getNombre(){
		return nombre;
	}			
		
	}
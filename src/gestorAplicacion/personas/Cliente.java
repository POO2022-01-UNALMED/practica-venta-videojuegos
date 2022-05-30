package gestorAplicacion.personas;
import gestorAplicacion.gestion.*;
import java.util.ArrayList;

public class Cliente extends Persona{
	private ArrayList<Videojuego> biblioteca = new ArrayList<Videojuego>();
	private int historialCompra;
	private Rango rango;
	
	/* Descripcion: La clase Cliente que hereda de Persona esta pensada para almacenar la biblioteca de videjuegos del cliente,
	  tambien desde esta clase, el cliente podra ver el catalogo de la empresa, comprar los videojuegos que desee, y finalmente,
	  calificar los videojuegos que haya comprado.
	*/
	public Cliente(){}
	public Cliente(String nom,long doc,int edad,Tarjeta tar,int historialCompra, ArrayList<Videojuego> biblioteca) {
		super(tar,nom,doc,edad);
		this.historialCompra = historialCompra;
		this.biblioteca = biblioteca;
		this.rango=Rango.NORMAL;
		Empresa.getListaClientes().add(this);
	}
	
	/* Parametros: String, double
	   Descripcion: Califica un videojuego que este dentro de la biblioteca del cliente
	   Return: String
	 */


	public String calificarVideojuego(String nombre, double cal) {
		nombre=nombre.toLowerCase();
		//Primero se revisa que la calificacion este en un rango adecuado
		if (0<=cal && cal<=10){
			//Luego se revisa si el cliente tiene el videojuego en su biblioteca
				for(Videojuego v: biblioteca) {
					//Este condicional confirma que efectivamente lo tiene
					if (v.getNombre().equals(nombre)) {
						if(v.getValorado()==false){
							v.setValorado(true);
						/*Ahora en este ciclo comprobamos que el juego siga en el catalogo, para que la valoracion pueda tener repercusion en sus compras,
						ya que si no esta igual no estaria a la venta*/
						for(Videojuego u:Catalogo.getVideojuegos()){
							//Este condicional comprueba que siga en el catalogo
							if (u.getNombre().equals(nombre)){
								// En estos cuatro se esta promediando la calificacion
								double c=(u.getValoracion()*u.getNumValoraciones())+cal;
								c=c/(u.getNumValoraciones()+1);
								u.setValoracion(c);
								//Finalmente suma una valoracion mas al videojuego
								u.setNumValoraciones(u.getNumValoraciones()+1); 

								return "Se ha valorado exitosamente";}}}
						return "Ya has valorado este videojuego";}
							}
				return "No puede valorar ya que no se ha comprado el videojuego o no se encuentra en el catalogo";}
		return "Valoracion no permitida";}
	
	/* Parametros: null
	   Descripcion: Este metodo es utilizado para que el cliente pueda ver todo el catalogo de videojuegos disponibles
	   Return: String  
	 */
	public String verCatalogo() {
		String c="";
		for(Videojuego i: Catalogo.getVideojuegos()) { //Recorre todo el catalogo
			c=c+"Nombre: "+i.getNombre()+"\n"
			+"Genero: "+i.getGenero()+"\n"
			+"Desarrollador: "+i.getDesarrollador().getNombre()+"\n"
			+"Valoracion: "+i.getValoracion()+"\n"
			+"Precio: "+i.getPrecio()+"\n"+"\n";}
		return c;}// y devuelve el nombre de los videojuegos en el catalogo
	
	 /* Parametros: String
	    Descripcion: Comprueba que un videojuego este en la biblioteca del cliente
	    Return: boolean
	  */
	public boolean comprobarVideojuego(String name){
		for(Videojuego v: biblioteca){
			if(v.getNombre().equals(name)){
				return true;}}
		return false;}
	
	/* Parametros: String
	   Descripcion: Este metodo busca y compra un videojuego del catalogo mediante la tarjeta del cliente para luego a�adirlo a su biblioteca
	   Return: String
	 */

	public String comprarVideojuego(String nombre) {
		if(this.comprobarVideojuego(nombre)==false){
			boolean x = Catalogo.verificarExistencia(nombre);
			//Verifica que el videojuego existe
			if(x==true) {
				for(Videojuego i: Catalogo.getVideojuegos()) {
					//Luego busca el videojuego requerido en el catalogo
					if(i.getNombre().equals(nombre)) {
						if(i.verificarEdad(this)==false){
							//verifica la edad
							return"No tienes edad suficiente";
						}
						//Verifica que puede realizar la compra mediante la tarjeta
						boolean y = this.getTarjeta().pagarVideojuego(i,this);
						if(y==true) {
							//Se crea una copia del videojuego
							Videojuego n = new Videojuego(i.getGenero(),i.getNombre(),i.getPrecio(),0,i.getDesarrollador(),i.getClasificacion(),0);
							 //Y luego anade el videojuego a la biblioteca del cliente
							biblioteca.add(n);
							historialCompra++;
					
							return "Compra exitosa";}
						if(y==false) {
							return "Saldo insuficiente";}}}}
			if(x==false) {
				return "Videojuego no existe";}}
		return "Ya posees este videojuego";}

	public String juegos(){
		String s="";
		for(Videojuego v: biblioteca){
			s=s+v.getNombre()+"\n";
		}
		return s;}
	
	 /* gets y sets de la clase*/
	

	public void setBiblioteca(ArrayList<Videojuego> b){
		this.biblioteca=b;}
	public ArrayList<Videojuego> getBiblioteca(){
		return biblioteca;}
	public Rango getRango(){
		return rango;
	}
	public void  setRango(Rango rango){
		this.rango=rango;
	}
	public String getNombre(){
		return nombre;
	}


}
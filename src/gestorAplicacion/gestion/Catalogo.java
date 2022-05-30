
package gestorAplicacion.gestion;
import java.util.ArrayList;
import java.io.Serializable;
public class Catalogo implements Serializable {
  	private static final long serialVersionUID = 1L;
	private static ArrayList<Videojuego> videojuegos = new ArrayList<Videojuego>();
  	public static ArrayList<Catalogo> catalogos=new ArrayList<Catalogo>();
	/*
	Descripcion: Esta clase guardara TODOS los videojuegos que vende la empresa
	*/
	
  	public Catalogo(ArrayList<Videojuego> x){
		this.videojuegos=x;
    	catalogos.add(this);
  }


	/*
	Parametros: String
	Descripcion: verificar si el videojuego consultado existe en el catalogo
	Return: boolean
	*/

	public static boolean verificarExistencia(String nombre) { 
		nombre.toLowerCase(); 
		//pasa el nombre a minusculas para evitar errores
		for(Videojuego v: videojuegos) {
			if (v.getNombre().equals(nombre)){
				return true;}}
		return false;} 


	/*
	Todos los get y sets de la clase
	*/
			

	public static ArrayList<Videojuego> getVideojuegos() {
		return videojuegos;}
	public static void setVideojuegos(ArrayList<Videojuego> videojuegos) {
		Catalogo.videojuegos = videojuegos;}
}
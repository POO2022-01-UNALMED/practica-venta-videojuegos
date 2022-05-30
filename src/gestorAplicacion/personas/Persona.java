package gestorAplicacion.personas;
import gestorAplicacion.gestion.*;
import java.util.ArrayList;
import java.io.Serializable;
public class Persona implements Serializable{
	private static final long serialVersionUID = 1L;
	  protected Tarjeta tarjeta;
	  protected String nombre;
	  protected long documento;
	  protected int edad;
	  public static ArrayList<Persona> personas=new ArrayList<Persona>(); 
	  
	  
	  /*
	  Descripcion: la clase Persona fue pensada para ser la calse padre
	  de empleado y cliente, así se podría ahorrar código
	  */
	public Persona() {personas.add(this);}

	public String descripcion(){
		return nombre+"\n"
		+edad+"\n";}
	
	public Persona(Tarjeta tarjeta, String nombre, long documento, int edad) {
		this.tarjeta = tarjeta;
		this.nombre = nombre;
		this.documento = documento;
		this.edad = edad;}
	
	public Tarjeta getTarjeta() {
		return tarjeta;}
	public void setTarjeta(Tarjeta tarjeta) {
		this.tarjeta=tarjeta;}
	
	
	public String getNombre() {
		return nombre +"y soy persona";}
	public void setNombre(String nombre) {
		this.nombre=nombre;}

	
	public long getDocumento() {
		return documento;}
	public void setDocumento(long documento) {
		this.documento=documento;}
	

	public int getEdad() {
		return edad;}
	public void setEdad(int edad) {
		this.edad=edad;}

	

}
package gestorAplicacion.gestion;
import java.io.Serializable;
import java.util.ArrayList;
import gestorAplicacion.personas.*;
public class Videojuego implements Serializable{
  private static final long serialVersionUID = 1L;
  private String genero;
  private String nombre;
  private double precio;
  private double valoracion;
  private Desarrollador desarrollador;
  private String clasificacion;
  private int numValoraciones;
  private boolean valorado;
  public static ArrayList<Videojuego> videojuegos=new ArrayList<Videojuego>();
  
  /*
	Descripcion: la clase Videojuego guarda todas las caracteriticas de los videojuegos,
  esta sera una clase importante(la empresa se basa en la venta de estos) 
  auque por sí sola no haga mucho
	*/
  
  public Videojuego(String genero,String nombre , double precio, double valoracion, Desarrollador desarrollador, String clasificacion,int numValoraciones){
    this.genero=genero;
    this.nombre= nombre;
    this.precio=precio;
    this.valoracion=valoracion;
    this.desarrollador=desarrollador;
    this.clasificacion=clasificacion;
    this.numValoraciones=numValoraciones;
    this.valorado=false;
    videojuegos.add(this);

  }
  /*
  Parametros: Cliente
	Descripcion:revisa que haya una compatibilidad entre la edad del cliente y la clasificacion del juego que desea comprar, para que un cliente no adquiera un juego que no tiene permitido adquirir
  return: boolean
	*/

  public boolean verificarEdad(Cliente cliente){
    if(this.clasificacion.equals("+18") && cliente.getEdad()>17){
      return true;
    }
    else if(this.clasificacion.equals("+16") && cliente.getEdad()>15){
      return true;
    }
    else if(this.clasificacion.equals("+12") && cliente.getEdad()>11){
      return true;
    }
    else if(this.clasificacion.equals("+7") && cliente.getEdad()>6){
      return true;
    }
    else if(this.clasificacion.equals("+3") && cliente.getEdad()>2){
      return true;
    }
    else{ return false;}
  }

  
  /*
	Todos los get y sets de la clase
	*/
  
  public void setValoracion(double valoracion){
    this.valoracion=valoracion;
  }
  public void setGenero(String genero){
    this.genero=genero;
  }
  public void setNombre(String nombre){
    this.nombre=nombre;
  }
  public void setPrecio(double precio){
    this.precio=precio;
  }
  public void setDesarrollador(Desarrollador desarrollador){
    this.desarrollador=desarrollador;
  }
  public void setClasificacion(String clasificacion){
    this.clasificacion=clasificacion;
  }
  public void setNumValoraciones(int numValoraciones){
    this.numValoraciones=numValoraciones;
  }
  public String getGenero(){
    return genero;
  }
  public String getNombre(){
    return nombre;
  }
  public double getPrecio(){
    return precio;
  }
  public double getValoracion(){
    return valoracion;
  }
  public Desarrollador getDesarrollador(){
    return desarrollador;
  }
  public String getClasificacion(){
    return clasificacion;
  }
  public int getNumValoraciones(){
    return numValoraciones;
  }
  public void setValorado(boolean f){
    this.valorado=f;
  }
  public boolean getValorado(){
    return valorado;
  }
}
package gestorAplicacion.gestion;
import java.util.ArrayList;
import java.io.Serializable;
public class Desarrollador extends Dian implements Serializable,Gobierno{
    public static ArrayList<Desarrollador> desarrolladores=new ArrayList<Desarrollador>();
    private static final long serialVersionUID = 1L;
    private String nombre;
    private Tarjeta tarjeta;
    private ArrayList<Videojuego> videojuegos=new ArrayList<Videojuego>();//Lista de videojuegos que posee el desarrollador
    private double comision; //Este atributo es un porcentaje de las ventas de cada juego que el desarrollador solicite ingresar en el catálogo.
	private double IMPUESTO=0.2;//Atributo con el porcentaje de impuestos

    /*Descrición: La clase desarrollador es un agente externo que se encarga de de venderle a la empresa los videojuegos que esta desarrolle,
    este cobrará un pequeño porcentaje de lo que la empresa de venta de videojuegos venda a cada cliente, su objetivo es nutrir el catálogo de videojuegos
    con su método principal solicitarIngresoJuego.
    */
    
    public Desarrollador(String nombre, Tarjeta tarjeta,ArrayList<Videojuego>videojuegos,double comision){
        this.nombre=nombre;
        this.tarjeta=tarjeta;
        this.videojuegos=videojuegos;
        this.comision=comision;
        desarrolladores.add(this);}
    
    public Desarrollador(String nombre) {
    	this(nombre,new Tarjeta(),new ArrayList<Videojuego>(),0);}
    
    /*
    Todos los get y set
    */
    public double getComision() {
		return comision;
	}
	public void setComision(double comision) {
		this.comision = comision;
    }
	public String getNombre(){
        return this.nombre;
    }
    public void setNombre(String nombre){
        this.nombre=nombre;
    }    
    public Tarjeta getTarjeta(){
        return this.tarjeta;
    }
    public void setTarjeta(Tarjeta tarjeta){
        this.tarjeta=tarjeta;
    }
    public ArrayList<Videojuego> getVideojuegos(){
        return videojuegos;
    }
    public void setVideojuegos(ArrayList<Videojuego> v){
        videojuegos=v;
    }
    /*Parámetros:Videojuego
    Descripción:solicitarIngresoJuego es método que interactua con la clase empresa, este va a ingresar un objeto tipo videojuego de su catálogo y el desarrollador, posteriormente llamará aceptarIngresoVideojuego.
    Return: void
     */
    public void solicitarIngresoJuego(Desarrollador this){
      Empresa.aceptarIngresoVideojuego(this) ;   //Aplicará el metodo de empresa aceptarIngresoVideojuego y en este entrará en evaluacion para ver si es rentable en la empresa, si lo es, lo agregará al catálogo.
    }
    
    
    /*Parametros:null
      Descripcion: este metodo calcula la cantidad de impuestos que debe pagarle el desarrollador al gobierno
      Return: String*/
      public String  calcularImpuesto() {
		double m=this.getTarjeta().getSaldo();
		return "Se debe pagar " +m*IMPUESTO;
		
	}
    /*Parametros:null
      Descripcion: este metodo paga los impuestos que el desarrollador le debe al gobierno por sus ganancias
      Return: void*/
      public void pagarImpuesto() {
		double m=this.getTarjeta().getSaldo();
		this.getTarjeta().retirar(m*IMPUESTO);
        Dian.getTarjeta1().ingresar(m*IMPUESTO);	
	}
    public void pagarEmpleadoOJuego(){
        for(Videojuego v:videojuegos){
            this.getTarjeta().retirar(v.getPrecio()*0.1);
            Dian.getTarjeta1().ingresar(v.getPrecio()*0.1);
        }

    }
	


}
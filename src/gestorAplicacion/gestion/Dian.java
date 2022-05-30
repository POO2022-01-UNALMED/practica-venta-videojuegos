package gestorAplicacion.gestion;
import java.util.ArrayList;

public abstract class Dian {
	    /*Descrición: La clase Dian es abstracta y de ella se heredan Empresa y Desarrollador
    */
	static private ArrayList<Tarjeta> tarjeta=new ArrayList<Tarjeta>();


	/*Este metodo obliga a la empresa y a los desarrolladores a pagar el impuesto calculado por el gobierno*/
	public abstract void pagarImpuesto();
		
	/*Este metodo obliga a la empresa y a los desarrolladores a pagar el impuesto calculado por sus juegos o empleados*/
	public abstract void pagarEmpleadoOJuego();


	/*Todods los get y set*/
	public static ArrayList<Tarjeta> tarjetal(){
		return tarjeta;
	}
	public static void  tarjetal2(ArrayList<Tarjeta> t){
		tarjeta=t;
	}

	public static Tarjeta getTarjeta1(){
		return tarjeta.get(0);
	}
	public static  void setTarjeta1(Tarjeta tarjeta){
		Dian.tarjeta.set(0, tarjeta);
	}
}
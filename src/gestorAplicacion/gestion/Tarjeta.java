package gestorAplicacion.gestion;
import gestorAplicacion.personas.*;
import java.util.ArrayList;
import java.io.Serializable;
public class Tarjeta implements Serializable {
    private static final long serialVersionUID = 1L;
    private long numero;
    private double saldo;
    public static  ArrayList<Tarjeta> tarjetas= new ArrayList<Tarjeta>();

	/*
	Descripcion: la clase Tarjeta permite la manipulacion y verificacion del dinero
    esta es primordial para todo lo relacionado con la venta hacia clientes y el pago hacia empleados
	*/	
    public Tarjeta(long l){
        this(l,0);
    }
    public Tarjeta(){
        this(0,0);
        }
    
    public Tarjeta(long numero, double saldo) {
        this.numero = numero;
        this.saldo = saldo;
        tarjetas.add(this);}

    /*
	Todos los get y sets de la clase
	*/

    public long getNumero() {
        return numero;}

    public void setNumero(long numero) {
        this.numero = numero;}

    public double getSaldo() {
        return saldo;}

    public void setSaldo(double saldo) {
        this.saldo = saldo;}
    
    /*
	Los metodos ingresar y retirar permiten la manipulacion del saldo de la tarjeta
    con una simplificacion de codigo
	*/

    public void ingresar(double x){
        saldo=saldo+x;}
    public void retirar(double x){
        saldo=saldo-x;}   
    
    /*
	Parametros: Videojuego, Cliente
    Descipcion: el metodo pagarVideojuego permite a un cliente pagar por un videojuego(en caso que tenga el dinero para hacerlo)
    y al comprarlo deposita la comision el la Tarjeta del desarrollador y el resto se deposita en
    la tarjeta de la empresa
    Return: boolean
	*/

    public boolean pagarVideojuego(Videojuego juego,Cliente cliente){
        //si puede pagar el videojuego
        if(juego.getPrecio()<=cliente.getTarjeta().getSaldo()){
            for (Desarrollador d:Empresa.getListaDesarrolladores()){
                if(d.getNombre().equals(juego.getDesarrollador().getNombre())){
                    //el cliente paga
                    cliente.getTarjeta().retirar(juego.getPrecio()*(1-cliente.getRango().getRango()));
                    //se paga al desarrollador su comision
                    juego.getDesarrollador().getTarjeta().ingresar(juego.getDesarrollador().getComision()*juego.getPrecio());
                    //la empresa ingresa el dinero restante
                    Empresa.getTarjeta().ingresar(juego.getPrecio()*(1-cliente.getRango().getRango())-(juego.getDesarrollador().getComision()*juego.getPrecio()));
                    return (true);}
               
                }
            //En caso que el desarrollador no haya pagado a la compañia por vender su videojuego,
            //se depositara todo el dinero que haya pagado el cliente en la Tarjeta de la empresa
            cliente.getTarjeta().retirar(juego.getPrecio()*(1-cliente.getRango().getRango())); 
            Empresa.getTarjeta().ingresar(juego.getPrecio()*(1-cliente.getRango().getRango()));
            return true;
        
                }
        //si no puede pagar el videojuego retorna false
        return false;
        
        

    
    }}
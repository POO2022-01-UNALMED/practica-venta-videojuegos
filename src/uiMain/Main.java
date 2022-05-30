package uiMain;
import java.util.ArrayList;
import gestorAplicacion.gestion.*;
import gestorAplicacion.personas.*;
import gestorAplicacion.gestion.Empresa;

import java.util.Scanner;

import baseDatos.Deserializador;
import baseDatos.Serializador;

import java.io.IOException;
import java.security.spec.DSAGenParameterSpec;

public class Main{
  static Scanner sc = new Scanner(System.in);
    int opcion;

    static int readInt() {
		return sc.nextInt();}
    static String readString() {
		return sc.nextLine();}
	static double readDouble() {
		return sc.nextDouble();}
    static long readLong(){
        return sc.nextLong();}

    
    public static void main(String[] args){
      
    	//cargar();
        deserializar();
        System.out.println("Buenos dias\n");
        int opcion;
        do {
			System.out.println("Que desea hacer?");
            System.out.println(" 0. Extras");
			System.out.println(" 1. Pagar empleados");
			System.out.println(" 2. Realizar bonificacion mensual");
            System.out.println(" 3. Cliente compra videojuego");
            System.out.println(" 4. Cliente califica videojuego");
            System.out.println(" 5. Bonificacion especial a cliente");
			System.out.println(" Opciones alternativas");
			System.out.println(" 6. Mostrar detalles empleados");
			System.out.println(" 7. Mostrar detalles empresa");
            System.out.println(" 8. Mostrar catalogo");
			System.out.println(" 9. Mostrar cliente especifico");
            System.out.println(" 10. Guardar y cerrar");
			System.out.println("Elija una opcion y presione enter: ");

			opcion = (int) readInt();
            switch (opcion) {
                case 0:
                menuextra();
                break;
                case 1:
                    System.out.println("-----------------------------------------------------------------");
                    System.out.println(Empresa.pagarEmpleados());
                    System.out.println("Se lleva pagado a la Dian un total de "+Dian.getTarjeta1().getSaldo());
                    System.out.println("-----------------------------------------------------------------");
                    break;
                case 2:
                    System.out.println("-----------------------------------------------------------------");
                    System.out.println(Empresa.revisionMensual());
                    System.out.println("-----------------------------------------------------------------");
                    break;
                case 3:
                System.out.println("-----------------------------------------------------------------");
                    menuComprarVideojuego();
                    System.out.println("-----------------------------------------------------------------");
                    break;
                case 4:
                System.out.println("-----------------------------------------------------------------");
                    menuCalificarVideojuego();
                    System.out.println("-----------------------------------------------------------------");
                    break;
                case 5:
                System.out.println("-----------------------------------------------------------------");
                rangoEspecial();
                System.out.println("-----------------------------------------------------------------");
                 
                    break;
                case 6:
                System.out.println("-----------------------------------------------------------------");
                    System.out.println(Empresa.revision());
                    System.out.println("-----------------------------------------------------------------");
                    break;
                case 7:
                System.out.println("-----------------------------------------------------------------");
                    menuEmpresa();
                    System.out.println("-----------------------------------------------------------------");
                    break;
                case 8:
                System.out.println("-----------------------------------------------------------------");
                    menuCatalogo();
                    System.out.println("-----------------------------------------------------------------");
                    break;
                case 9:
                System.out.println("-----------------------------------------------------------------");
                revisionCliente();
                System.out.println("-----------------------------------------------------------------");    
                case 10:
              serializar();
                    System.out.println("Vuelve pronto");
                    break;
            }
        }while(opcion !=10);
    }
 /* Menu extra*/
    static void menuextra(){
        int opcion;
        do{
            System.out.println("1: Anadir videojuego");
            System.out.println("2: Contratar empleado");
            System.out.println("3: Ingresar dinero tarjeta");
            System.out.println("4: Volver");
            opcion= (int) readInt();
            switch(opcion){
                case 1:
                System.out.println("-----------------------------------------------------------------");
                anadirvideojuego();
                System.out.println("-----------------------------------------------------------------");
                break;
                case 2:
                System.out.println("-----------------------------------------------------------------");
                contratarempleado();
                System.out.println("-----------------------------------------------------------------");
                break;
                case 3:
                System.out.println("-----------------------------------------------------------------");
                anadirdinero();
                System.out.println("-----------------------------------------------------------------");
                break;
            }
        }while(opcion!=4);
    }

 /* Metodo para anadir un videojuego al ctalogo*/
    static void anadirvideojuego(){ //String genero,String nombre,double precio,String desarrollador,String clasificacion
        Scanner dato1=new Scanner(System.in);
        System.out.println("Por favor ingrese todo lo siguiente en minuscula: ");
        Empleado x=new Empleado();
        System.out.println("Nombre del juego: ");
        String nombre=dato1.nextLine();
        for(Videojuego v:Videojuego.videojuegos){
            if(v.getNombre().equals(nombre)){
                
                System.out.println(x.anadirVideojuegos(v));
                return;
            }
        }
        System.out.println("Clasificacion del juego: ");
        Scanner dato2=new Scanner(System.in);
        String clasi=dato2.nextLine();
        System.out.println("Genero del juego: ");
        String genero=dato1.nextLine();
        System.out.println("Precio del juego: ");
        double precio=dato1.nextDouble();
        System.out.println("Nombre del desarrollador: ");
        String desarro=dato2.nextLine();
       
    
        
        //se verifica que si manejemos la clasificacion estandar de (+18,+16,+12,+7,+3)
        if(clasi.equals("+18") || clasi.equals("+16") || clasi.equals("+12") || clasi.equals("+7") || clasi.equals("+3")){
            Empleado www=new Empleado();
            System.out.println(www.anadirVideojuegos(genero, nombre, precio, desarro, clasi));//se ejecuta el metodo en la clase Empleado

        }
        else{
            System.out.println("Clasificacion no aceptada");
        }

    }
 /* Metodo para contratar empleado*/
    static void contratarempleado(){//String nom,long doc,int edad,double sueldo,long tar, String cargo,int ventas
        Scanner dato1=new Scanner(System.in);
        System.out.println("Ingrese el nombre completo: ");
        String nombre=dato1.nextLine();
        System.out.println("Ingrese la cedula: ");
        long cedula=(long)readLong();
        System.out.println("Ingrese la edad: ");
        int edad=(int)readInt();
        System.out.println("Ingrese el sueldo: ");
        double sueldo=(double)readDouble();

        for(Empleado e:Empresa.getListaEmpleados()){
            if (cedula==e.getDocumento()){
                System.out.println("Esta persona ya esta contratada");
                return;
            }
        }
        System.out.println("Ingrese el numero de la nueva tarjeta");
        long tar=(long)readLong();
        Empresa.contratarEmpleadoEmpleado(nombre, cedula, edad, sueldo, tar, "Vendedor", 0);
        System.out.println("Empleado añadido con exito");


    }

 /* Metodo para anadir el dinero a la tarjeta de un cliente(seria como un cajero), se maneja con dinero fisico*/
    static void anadirdinero(){
        Scanner dato1=new Scanner(System.in);
        System.out.println("Ingrese la cantidad de dinero: ");
        double precio=dato1.nextDouble();
        System.out.println("Ingrese el cliente ");
        long cedula=(long)readLong();

        for(Cliente c: Empresa.getListaClientes()){
            if (c.getDocumento()==cedula){
                c.getTarjeta().setSaldo(c.getTarjeta().getSaldo()+precio);//Se deposita el dinero
                System.out.println("Dinero depositado");
                return;
            }
        }
        System.out.println("Cliente no encontrado");
        return;}

        /* Metodo para comprar un videojuego por parte de un cliente*/
    static void menuComprarVideojuego(){
        System.out.println("Ingrese la cédula del cliente");
        long cedula=(long)readLong();
        System.out.println("Ingrese el nombre del videojuego en minuscula");
        Scanner dato1=new Scanner(System.in);
        String videojuego=dato1.nextLine();
        for(Cliente c:Empresa.getListaClientes()){
            if(c.getDocumento()==cedula){
                System.out.println(c.comprarVideojuego(videojuego));//se llama al metodo de la clase Cliente
                return;}}
        System.out.println("Cliente no encontrado"+"\n");
        return;}

/* Metodo calificar el videojuegoo*/
    static void menuCalificarVideojuego(){
        System.out.println("Ingrese la cédula del cliente");
        long cedula=(long)readLong();
        System.out.println("Ingrese el nombre del videojuego en minuscula");
        Scanner dato1=new Scanner(System.in);
        String videojuego=dato1.nextLine();
        System.out.println("Ingrese la valoracion(numero entero por favor)");
        double calificacion=(double)readDouble();
        for(Cliente c:Empresa.getListaClientes()){
            if(c.getDocumento()==cedula){
                System.out.println(c.calificarVideojuego(videojuego, calificacion));//se llama al metodo de la clase Cliente
                return;}}
        System.out.println("Cliente no encontrado"+"\n");
        return;}

       /* Metodo para ver informacion de un cliente en especifico*/ 
    static void revisionCliente(){
        System.out.print("Ingrese la cedula del cliente: ");
        long cedula=(long)readLong();
        for(Cliente e:Empresa.getListaClientes()){
            if(cedula==e.getDocumento()){
                if(e.getBiblioteca().size()==0){
                    System.out.println("Nombre:b"+e.getNombre()+"\nEdad: "+e.getEdad()+"\nRango: "+e.getRango()+
                    "\nSaldo tarjeta: "+e.getTarjeta().getSaldo()+"\nAun no posee juegos");
                    return;
                }
                System.out.println("Nombre: "+e.getNombre()+"\nEdad: "+e.getEdad()+"\nRango: "+e.getRango()+
                "\nSaldo tarjeta: "+e.getTarjeta().getSaldo()+"\nJuegos "+e.juegos());
            return;}}
        System.out.println("Cliente no encontrado");
    }

 /* Metodo para sasignar el rango especial*/
    static void rangoEspecial(){
        System.out.print("Ingrese la cedula del cliente: ");
        long cedula=(long)readLong();
        Empleado e=new Empleado();//obejto Empleado temporal
        System.out.println(e.descuentoEspecial(cedula));//se llama al metodo del empleado;

    }

     /* Metodo para ver la informacion de la empresa*/
    static void menuEmpresa(){
        System.out.println("Empresa XGames"+"\n"
        +"Saldo global :"+Empresa.getTarjeta().getSaldo()+"\n"+
        "Numero de empleados actuales: "+Empresa.getListaEmpleados().size()+"\n"
        +"Numero de clientes activos: "+Empresa.getListaClientes().size()+"\n"+
        "Numero de desarrolladores actuales: "+Empresa.getListaDesarrolladores().size());}

     /* Metodo para ver el catalogo actual*/
    static void menuCatalogo(){
        Cliente c=new Cliente();
        System.out.print(c.verCatalogo());
        return;}
    
     /* Metodo para serialziar y deserializar las clases*/
    static void serializar(){
        Serializador.serializarTodo();}
    static void deserializar(){
            Deserializador.deserializarTodo();}



    
    static void cargar(){
/* Primera Base de datos, al deserializar se quitara del main el matodo cargar(),
     pero se dejara en la clase como evidencia*/

    
    Tarjeta t1=new Tarjeta(1001,5000);
	Tarjeta t2=new Tarjeta(2378,1233);
	Tarjeta t3=new Tarjeta(7410,2344);
	Tarjeta t4=new Tarjeta(8806,3007);
	Tarjeta t5=new Tarjeta(6960,990);
    Tarjeta tc1=new Tarjeta(9944,5200);
    Tarjeta tc2=new Tarjeta(6960,990);
    Tarjeta tc3=new Tarjeta(3390,1556);
    Tarjeta tc4=new Tarjeta(2012,2000);
    Tarjeta tc5=new Tarjeta(4467,10050);
    Tarjeta td1=new Tarjeta(4400,10000);
    Tarjeta td2=new Tarjeta(5003,25000);
    Tarjeta td3=new Tarjeta(7791,20700);
    Tarjeta dian=new Tarjeta(7891,0);


    

    Tarjeta te=new Tarjeta(1709,10000);
    ArrayList<Tarjeta> dy=new ArrayList<Tarjeta>();
    dy.add(dian);
        Dian.tarjetal2(dy);
    Empresa Xgames=new Empresa();
    ArrayList<Tarjeta> t=new ArrayList<Tarjeta>();
    t.add(te);
    Empresa.setTarjeta(t);
		
	Empleado e1=new Empleado("Juan Carlos Zapata",10101000l,30,t1,100,"Vendedor",25);
	Empleado e2=new Empleado("Tatiana Perea",12101509l,22,t2,100,"Vendedor",40);
	Empleado e3=new Empleado("Oscar suarez",10351022l,37,t3,100,"  Vendedor",0);
    Empleado e4=new Empleado("Pablo Rodriguez",10257622l,40,t4,100,"  Vendedor",50);
    Empleado e5=new Empleado("Gustavo Fring",66078005l,28,t5,100,"  Vendedor",100);
    
    

   
    Cliente c1=new Cliente("Marco Aurelio Gomez",100l,22,tc1,20,  new ArrayList<Videojuego>() );
    Cliente c2=new Cliente("Jeronimo Zapata",200l,16,tc2,15,  new ArrayList<Videojuego>() );
	Cliente c3=new Cliente("Didier Herrera",300l,30,tc3,30,  new ArrayList<Videojuego>() );
    Cliente c4=new Cliente("Miguel Angel Vera",400l,45,tc4,20,  new ArrayList<Videojuego>() );
    Cliente c5=new Cliente("Santiago Marulanda",500l,27,tc5,50,  new ArrayList<Videojuego>() );

    

		
	Desarrollador d1=new Desarrollador("des");
    Desarrollador D1=new Desarrollador("ubisoft", td1, new ArrayList<Videojuego>(),0.3);  
	Desarrollador D2=new Desarrollador("activision", td2, new ArrayList<Videojuego>(),0.45);
    Desarrollador D3=new Desarrollador("mojang", td1, new ArrayList<Videojuego>(),0.1);

    

    Videojuego v1= new Videojuego("Terror","silent hill" ,50.35, 10, D1, "+18",1);
    Videojuego v2= new Videojuego("Aventura","uncharted" ,60.15, 10, D1, "+12",1);
    Videojuego v3= new Videojuego("Carreras","forza horizon" ,35.70, 10, D3, "+7",1);
    Videojuego v4= new Videojuego("Aventura","minecraft" ,45.35, 10, D3, "+3",1);
    Videojuego v5= new Videojuego("Deportes","fifa" ,62.01, 10, D1, "+7",1);
    Videojuego v6= new Videojuego("Accion","call of duty" ,70.15, 10, D2, "+18",1);
    Videojuego v7= new Videojuego("Familiar","los sims" ,20.45, 10, D3, "+3",1);
    Videojuego v8= new Videojuego("Accion","dark souls" ,50.09, 10, D1, "+16",1);
    Videojuego v9= new Videojuego("Aventura","crash bandicoot" ,39.95, 10, D2, "+12",1);
    Videojuego v10= new Videojuego("Accion","gta v" ,70.45, 10, D1, "+18",1);


    D1.getVideojuegos().add(v1);
    D1.getVideojuegos().add(v2);
    D1.getVideojuegos().add(v5);
    D1.getVideojuegos().add(v8);
    D1.getVideojuegos().add(v10);

    D2.getVideojuegos().add(v9);

    D3.getVideojuegos().add(v3);
    D3.getVideojuegos().add(v4);
    D3.getVideojuegos().add(v6);
    D3.getVideojuegos().add(v7);


    ArrayList<Videojuego> catalogo=new ArrayList<Videojuego>();
    catalogo.add(v1);
    catalogo.add(v2);
    catalogo.add(v8);
    catalogo.add(v5);
    catalogo.add(v10);
    Catalogo ci=new Catalogo(catalogo);
    Catalogo.setVideojuegos(catalogo);


    ArrayList<Desarrollador> deses=new ArrayList<Desarrollador>();
    deses.add(D1);
    Empresa.setListaDesarrolladores(deses);


    c1.comprarVideojuego("silent hill");
    c1.comprarVideojuego("uncharted");

    c2.comprarVideojuego("gta v");


    c3.comprarVideojuego("fifa");
    c3.comprarVideojuego("dark souls");




    }
    }
        


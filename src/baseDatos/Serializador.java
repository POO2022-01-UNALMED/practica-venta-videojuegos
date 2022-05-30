package baseDatos;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

import gestorAplicacion.gestion.*;
import gestorAplicacion.personas.*;


/**
 * Se utiliza para serializar todos los objetos creados durante la ejecucion
 * del proyecto
 * 
 */
public class Serializador {
	
	public static <E> void serializar(List<E> lista, String className) {
		FileOutputStream fileOut;

		try {
			String path = System.getProperty("user.dir") + "/src/baseDatos/temp/" + className + ".txt";
			// se crea un fileoutputstream para saber donde serializar los archivos
			fileOut = new FileOutputStream(path);
			// Se crea un objeto output stream para poder escribir en el archivo
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			// Guardamos la lista de objetos
			out.writeObject(lista);
			out.close();
			fileOut.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	/**
	 * Serializamos todas las clases que necesitamos
	 */
	public static void serializarTodo() {
		Serializador.serializar(Catalogo.catalogos, "Catalogos");
		Serializador.serializar(Videojuego.videojuegos, "Videojuegos");
		Serializador.serializar(Empresa.empresas, "Empresas");
		Serializador.serializar(Desarrollador.desarrolladores, "Desarrolladores global");
		Serializador.serializar(Tarjeta.tarjetas, "Tarjetas");
		Serializador.serializar(Empresa.getListaClientes(), "Clientes");
		Serializador.serializar(Empresa.getListaEmpleados(), "Empleados");
		Serializador.serializar(Persona.personas, "Personas");
		Serializador.serializar(Catalogo.getVideojuegos(), "Videojuegos catalogo");
		Serializador.serializar(Empresa.tarjeta(),"Tarjeta empresa");
		Serializador.serializar(Empresa.getListaDesarrolladores(),"Desarrolladores Empresa");
		Serializador.serializar(Dian.tarjetal(),"Tarjeta Dian");
	 
	}
}
package gestorAplicacion.gestion;

public enum Rango{
    /*
	Descripcion: el enum Rango describe los rangos  a los que puede acceder un cliente, estos le otorgan bonos dependiendo
    que tan alto sea el rango
	*/	
    NORMAL(0.0),BRONCE(0.1),PLATA(0.2),ORO(0.25), ESPECIAL(0.3);
    double Rango;
    private Rango(double Rango) {
        this.Rango = Rango;
    }
    /*
	Todos los get y set de los porcentajes
	*/	
    public double getRango(){
        return Rango;
    }
    public void setRango(double rango){
        this.Rango=rango;
    }
    
}
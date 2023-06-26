
import java.util.ArrayList;


public class Caja {
    private double plataInicial;
    private double plataFinal;
    private double fin;
    private ArrayList<Producto> productos;
    
    public Caja(double plataInicial, double plataFinal, double f){
        this.fin = f;
        this.plataInicial = plataInicial;
        this.plataFinal = plataFinal;
        ArrayList productos = new ArrayList();
    }

    public ArrayList<Producto> getProductos() {
        return productos;
    }

    public void setProductos(ArrayList<Producto> productos) {
        this.productos = productos;
    }
    
    public double getPlataInicial() {
        return plataInicial;
    }

    public void setPlataInicial(double plataInicial) {
        this.plataInicial = plataInicial;
    }

    public double getPlataFinal() {
        return plataFinal;
    }

    public void setPlataFinal(double plataFinal) {
        this.plataFinal = plataFinal;
    }

    public double getFin() {
        return fin;
    }

    public void setFin(double fin) {
        this.fin = fin;
    }
    public double calcularTotal(double fin, Producto p){
        fin = 0;
        for(Producto p : productos){
            fin+= p.getPrecio();
        }
        return fin;
    }
    
    public void agregarProducto(Producto p){
        productos.add(p);
    }
    
    public void mostrarDatos(double plataIncial, double plataFinal, double fin){
        System.out.println("inico con: " + this.plataInicial + "finalizo con: " + this.plataFinal + "plata que deberia haber: " + this.fin);
        
    }
        
}

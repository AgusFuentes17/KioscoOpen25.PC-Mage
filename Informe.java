
public class Informe {
    private String fecha;
    private Caja caja;
    private Producto productoVendido;
    
    public Informe(String f, Producto productoVendido, Caja caja){
        this.fecha = f;
        this.productoVendido = productoVendido;
        this.caja = caja;
    }

    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public Caja getCaja() {
        return caja;
    }

    public void setCaja(Caja caja) {
        this.caja = caja;
    }

    public Producto getProductoVendido() {
        return productoVendido;
    }

    public void setProductoVendido(Producto productoVendido) {
        this.productoVendido = productoVendido;
    }    
}

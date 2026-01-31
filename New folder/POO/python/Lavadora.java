public class Lavadora {
    // Atributos privados
    private String nombre;
    private String color;
    private String marca;
    private double precio;
    private int ciclos;
    private boolean encendida;

    // Constructor
    public Lavadora(String nombre, String color, String marca, double precio, int ciclos) {
        this.nombre = nombre;
        this.color = color;
        this.marca = marca;
        this.precio = precio;
        this.ciclos = ciclos;
        this.encendida = false;
    }

    // Métodos adicionales
    public void info() {
        String estado;
        if (encendida) {
            estado = "encendida";
        } else {
            estado = "apagada";
        }
        System.out.println("Lavadora: " + nombre + " | Marca: " + marca + " | Color: " + color + " | Precio: $" + precio
                + " | Ciclos: " + ciclos + " | Estado: " + estado);
    }

    public void encender() {
        if (encendida) {
            System.out.println(nombre + " ya estaba encendida");
        } else {
            encendida = true;
            System.out.println(nombre + " ahora está encendida");
        }
    }

    public void apagar() {
        if (encendida) {
            encendida = false;
            System.out.println(nombre + " ahora está apagada");
        } else {
            System.out.println(nombre + " ya estaba apagada");
        }
    }

    public static void main(String[] args) {
        Lavadora lav1 = new Lavadora("Lavadora Ultra", "Blanco", "Samsung", 8500, 12);

        lav1.info();
        lav1.encender();
        lav1.info();
        lav1.apagar();
        lav1.info();
    }
}

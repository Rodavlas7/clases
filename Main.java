// Clase base (superclase)
class Vehiculo {
    String marca;
    String modelo;
    int año;

    Vehiculo(String marca, String modelo, int año) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
    }

    void mostrarInfo() {
        System.out.println("Vehículo: " + marca + " " + modelo + " (" + año + ")");
    }
}

// Clase hija que hereda de Vehiculo
class Carro extends Vehiculo {
    static int contador = 0; // atributo compartido por todos los carros
    int puertas;

    Carro(String marca, String modelo, int año, int puertas) {
        super(marca, modelo, año); // usamos el constructor de la superclase
        this.puertas = puertas;
        contador++; // cada vez que se crea un carro, aumenta
    }

    // Sobrescribimos el método (polimorfismo)
    @Override
    void mostrarInfo() {
        System.out.println("Carro: " + marca + " " + modelo + " (" + año + ") con " + puertas + " puertas.");
    }

    // Método estático (no necesita objeto para usarse)
    static void mostrarContador() {
        System.out.println("Se han creado " + contador + " carros en total.");
    }
}

// Otra clase hija (ejemplo extra de herencia)
class Moto extends Vehiculo {
    static int motodor = 0;
    boolean cascoIncluido;

    Moto(String marca, String modelo, int año, boolean cascoIncluido) {
        super(marca, modelo, año);
        this.cascoIncluido = cascoIncluido;
        motodor++;
    }

    @Override
    void mostrarInfo() {
        System.out.println("Moto: " + marca + " " + modelo + " (" + año + ") casco incluido: " + cascoIncluido);
    }

    static void mostrarContador() {
        System.out.println("Se han creado " + motodor + " motos en total.");
    }

    static void destruir() {
        motodor--;
    }
}

// Clase principal
public class Main {
    public static void main(String[] args) {
        Carro c1 = new Carro("Toyota", "Corolla", 2020, 4);
        Carro c2 = new Carro("Honda", "Civic", 2021, 2);
        Moto m1 = new Moto("Yamaha", "R6", 2019, true);

        // Mostramos info de cada vehículo
        c1.mostrarInfo();
        c2.mostrarInfo();
        m1.mostrarInfo();

        // Uso del método estático
        Carro.mostrarContador();
        Moto.mostrarContador();

    }
}

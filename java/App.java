public class App {
    public static void main(String[] args) {
        Empleado E1 = new Empleado("Juan", "Perez", 41, 1000);
        Empleado E2 = new Empleado("Misael", "Redondo", 39, 5000);

        E1.info();
        E2.info();

        E1.aumento();
        E2.aumento();

        E2.setEdad(40);

        E1.info();
        E2.info();

        E2.aumento();
    }
}

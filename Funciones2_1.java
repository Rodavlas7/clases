import java.util.Scanner;

public class Funciones2_1 {

    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Ingrese el consumo en kw: ");
        int consumo = scr.nextInt();

        float total = calcularCosto(consumo);

        System.out.println("El total a pagar es: $" + total);

        scr.close();
    }

    public static float calcularCosto(int consumo) {
        float costo;

        if (consumo < 100) {
            costo = consumo * 0.5f;
        } else if (consumo <= 200) {
            costo = consumo * 0.75f;
        } else {
            costo = consumo * 1.2f;
        }

        int rango;
        if (consumo < 100) {
            rango = 1;
        } else if (consumo <= 200) {
            rango = 2;
        } else {
            rango = 3;
        }

        switch (rango) {
            case 1:
                System.out.println("Consumo bajo (menos de 100kw)");
                break;
            case 2:
                System.out.println("Consumo medio (entre 100 y 200kw)");
                break;
            case 3:
                System.out.println("Consumo alto (más de 200kw)");
                break;
        }

        return costo;
    }
}

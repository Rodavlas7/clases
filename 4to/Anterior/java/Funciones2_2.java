import java.util.Scanner;

public class Funciones2_2 {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Ingresa el valor de a: ");
        int a = scr.nextInt();
        System.out.print("Ingresa el valor de b: ");
        int b = scr.nextInt();

        evaluarNumeros(a, b);

        scr.close();
    }

    public static void evaluarNumeros(int a, int b) {
        if (a < 0 && b < 0) {
            System.out.println("Los 2 son negativos");
        } else if (a > 0 && b < 0) {
            System.out.println("a es positivo, b es negativo");
        } else if (a < 0 && b > 0) {
            System.out.println("a es negativo, b es positivo");
        } else if (a > 0 && b > 0) {
            System.out.println("Los 2 son positivos");
        } else {
            if (a == 0 && b == 0) {
                System.out.println("Ambos son cero");
            } else if (a == 0) {
                System.out.println("a es cero");
            } else if (b == 0) {
                System.out.println("b es cero");
            }
        }
    }
}

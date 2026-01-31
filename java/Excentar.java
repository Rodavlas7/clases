import java.util.Scanner;

public class Excentar {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Dame el numero total de elementos: ");
        int n = scr.nextInt();

        System.out.print("Deme el numero de elementos seleccionados: ");
        int r = scr.nextInt();

        if (n >= r) {
            System.out.println("el numero total de combinaciones es " + calculo(n, r));
        } else {
            System.out.println("n debe ser mayor que r");
        }
        scr.close();
    }

    public static int calculo(int n, int r) {
        int tot = 0;

        if (n > 0 && r > 0) {
            tot = (fact(n)) / (fact(r) * fact(n - r));
        } else {
            System.out.println("n y r deben ser numeros naturales");
        }
        return tot;
    }

    public static int fact(int num) {
        int total = 1;

        if (num >= 0) {
            while (num >= 1) {
                total = num * total;
                num--;
            }
        } else {
            System.out.println("El numero debe de ser natural");
        }
        return total;
    }
}
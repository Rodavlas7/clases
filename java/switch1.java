import java.util.Scanner;

public class switch1 {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.println("¿Cuál fue su consumo?:");

        double consumo = scr.nextDouble();
        double total;
        int caso;

        if (consumo < 100) {
            caso = 1;
        } else if (consumo < 200) {
            caso = 2;
        } else {
            caso = 3;
        }

        switch (caso) {
            case 1:
                total = consumo * 0.5;
                break;
            case 2:
                total = consumo * 0.75;
                break;
            case 3:
                total = consumo * 1.2;
                break;
            default:
                total = 0;
                break;
        }

        System.out.println("Tu pago es: " + total);
    }
}


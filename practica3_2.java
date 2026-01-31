import java.util.Scanner;

public class practica3_2 {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Deme el numero de numeros que quiere introducir: ");
        int rep = scr.nextInt();
        int i=0;
        int num;
        int pos = 0;
        int neg = 0;
        int neu = 0;

        while (i<rep) {
            System.out.print("Deme un numero entero: ");
            num = scr.nextInt();
            if (num > 0) {
                pos++;
            } else if (num < 0) {
                neg++;
            } else if (num == 0) {
                neu++;
            }
            i++;
        }

        System.out.println("Me diste " + pos + " numeros positivos, " + neg + " numeros negativos y " + neu + " numeros neutros o cero");

        scr.close();
    }
}

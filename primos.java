import java.util.Scanner;

public class primos {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Ingresa el primer número: ");
        int inicio = scr.nextInt();

        System.out.print("Ingresa el segundo número: ");
        int fin = scr.nextInt();

        if (inicio > fin) {
            int temporal = inicio;
            inicio = fin;
            fin = temporal;
        }

        System.out.print("Números primos entre " + inicio + " y " + fin + ": ");

        

        scr.close();
    }
}

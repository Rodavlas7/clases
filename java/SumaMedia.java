import java.util.Scanner;

public class SumaMedia {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);
        double num, suma = 0;
        int i, contador;

        System.out.print("Deme el número de números que desea ingresar: ");
        i = scr.nextInt();
        contador = i;

        while (i > 0) {
            System.out.print("Dame un número: ");
            num = scr.nextDouble();
            suma += num;
            i--;
        }

        System.out.println(suma + " < Suma || Media > " + (suma / contador));
        
        scr.close();
    }
}

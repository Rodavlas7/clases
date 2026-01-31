import java.util.Scanner;

public class practica2_1 {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        float a;
        float b;

        System.out.println("Deme un numero:");
        a = scr.nextFloat();
        System.out.println("Deme otro numero:");
        b = scr.nextFloat();

        if (a < 0 && b < 0){
            System.out.println(a + " y " + b + " son negativos");
        } else if (a > 0 && b > 0) {
            System.out.println(a + " y " + b + " son positivos");
        } else if (a > 0 && b < 0) {
            System.out.println(a + " es positivo y " + b + " es negativo");
        }else if (a < 0 && b > 0) {
            System.out.println(a + " es negativo y " + b + " es positivo");
        }
        
        scr.close();
    }
}

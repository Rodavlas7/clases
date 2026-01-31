import java.util.Scanner;

public class hipotenusa {

    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Ingrese el cateto A: ");
        float catA = scr.nextFloat();
        System.out.print("Ingresa el cateto B: ");
        float catB = scr.nextFloat();

        System.out.println( "la hipotenusa es " + Math.sqrt(pote(catA, 2) + pote(catB, 2)) );

        scr.close();
    }

    public static float pote(float num, float exponente) {
        float potencia = 1;
        int contador = 1;

        if (exponente == 0) {
            return 1;
        } else if (exponente > 0) {
            while (contador <= exponente) {
                potencia *= num;
                contador++;
            }
            return potencia;
        } else {
            while (contador <= -exponente) {
                potencia *= num;
                contador++;
            }
            return 1 / potencia;
        }
    }

    public static float raiz(float num) {
        
        return num;
    }
}
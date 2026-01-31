import java.util.Scanner;

public class PotenciaFuncion {

    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Ingrese un numero: ");
        float num = scr.nextInt();
        System.out.print("Ingresa el exponente: ");
        float expo = scr.nextInt();

        System.out.println("El resultado de " + num + "^" + expo + " = " + pote(num, expo));

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
}

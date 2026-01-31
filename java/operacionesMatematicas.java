import java.util.Scanner;

public class operacionesMatematicas {
    public static void main(String[] args) {

        Scanner scr = new Scanner(System.in);

        System.out.print("Dame un numero: ");
        Float num1 = scr.nextFloat();
        System.out.print("Dame otro numero: ");
        Float num2 = scr.nextFloat();

        System.out.println("La suma de ambos es " + (sumar(num1, num2)));
        System.out.println("La resta de ambos es " + (restar(num1, num2)));
        System.out.println("La multiplicacion de ambos es " + (multiplicacion(num1, num2)));
        System.out.println("La division de ambos es " + (division(num1, num2)));
        System.out.println("El mod de ambos es " + (mod(num1, num2)));

        scr.close();
    }

    public static float sumar(float a, float b) {
        return (a + b);
    }

    public static float restar(float a, float b) {
        return (a - b);
    }

    public static float multiplicacion(float a, float b) {
        return (a * b);
    }

    public static float division(float a, float b) {
        return (a / b);
    }

    public static float mod(float a, float b) {
        return (a % b);
    }

}
import java.util.Scanner;

public class practica2_2 {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.println("Ingresa una letra de la siguiente lista: q = 1; w = 2; e = 3; r = 4; t = 5;");
        char a = scr.next().charAt(0);

        switch (a) {
              case 'q':
                System.out.println("1");
                break;
            case 'w':
                System.out.println("2");
                break;
            case 'e':
                System.out.println("3");
                break;
            case 'r':
                System.out.println("4");
                break;
            case 't':
                System.out.println("5");
                break;
            default:
                System.out.println("Letra incorrecta");
                break;        }
    }
}

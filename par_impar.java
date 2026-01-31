import java.util.Scanner;

public class par_impar {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        int num;
        int par = 0;
        int inpar = 0;

        for (int i = 1; i <= 5; i++) {
            System.out.print("Dame el numero " + i + ": ");
            num = scr.nextInt();
            if (num % 2 == 0) {
                par++;
            } else {
                inpar++;
            }
        }

        System.out.println(par + " numeros pares");
        System.out.println(inpar + " numeros inpares");

        scr.close();
    }
}

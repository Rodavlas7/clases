import java.util.Scanner;

public class tabla {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("De que numero desea su tabla del 1 al 10: ");
        float num = scr.nextFloat();

        multi(num);

        scr.close();
    }

    public static void multi (float num){
        int cont = 1;

        while (cont <= 10) {
            System.out.println(num + " x " + cont + " = " + (cont*num));
            cont++;
        }
        
    }
}

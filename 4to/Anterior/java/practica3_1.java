import java.util.Scanner;

public class practica3_1 {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Deme un numero natural: ");
        int lim = scr.nextInt();
        int num = 0;
        int i = 0;

        System.out.print("X = " + lim + "; ");

        while (num<lim) {
            num = i + num ;
            i++;
            System.out.print(" " + i);
        } 

        System.out.println("; " + num + "; s mayor igual que " + lim);

        scr.close();
    }
}

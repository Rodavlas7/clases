import java.util.Scanner;

public class MultiplicacionPasoPaso {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);
        System.out.println("Dame a");
        int a = scr.nextInt();
        System.out.println("Dame b");
        int b = scr.nextInt();
        multi(a, b);
        scr.close();
    }

        static int multi(int a, int b) {
        int total = 0;
        if (b==0){
            return total;
        } else if (b > 0) {
            total = (a+multi(a, b-1));
            System.out.println(total);
            return total;
        }
        
        return total;
    }

}

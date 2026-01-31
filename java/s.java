import java.util.Scanner;

/*
 *  𝑒𝑥𝑝𝑜(𝑎^𝑏)={(0,    𝑠𝑖 𝑏=0
    𝑎 ∗ 𝑎^(𝑏−1),      𝑠𝑖 𝑏>0)}
 */

public class s {
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
            System.out.println("oa" + total);
            return total;
        }
        
        return total;
    }

}

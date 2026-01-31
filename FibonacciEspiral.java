import java.util.Scanner;

public class FibonacciEspiral {
    static int fib(int n) {
        if (n <= 1)
            return n;
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);
        while (true) {
            System.out.print("Número de término (1-20, negativo para salir): ");
            int n = scr.nextInt();
            if (n < 0)
                break;
            if (n >= 1 && n <= 20) {
                System.out.println("F(" + n + ") = " + fib(n));
            } else {
                System.out.println("Fuera de rango");
            }
        }
        scr.close();
    }
}

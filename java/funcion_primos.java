import java.util.Scanner;

public class funcion_primos {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);
        
        System.out.print("Ingresa el número final: ");
        int fin = scr.nextInt();

        System.out.println("Números primos hasta " + fin +  ":");

        primillos(fin);

        scr.close();
    }

    public static void primillos(int fin) {

        for (int i = 2; i <= fin; i++){
            
            boolean esPrimo = true;   
            for(int j = 2; j < i; j++){

                esPrimo = true;

                if (i%j == 0){
                    esPrimo=false;
                    break;
                }
            }    
            if (esPrimo){
                System.out.println(i + " es primo");
            }
        
        }

    }
}

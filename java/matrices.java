import java.util.*;

public class matrices {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Ingresa el tamaño de las matrices: ");
        int n = scr.nextInt();

        int[][] A = new int[n][n];
        int[][] B = new int[n][n];
        int[][] suma = new int[n][n];

        System.out.println("\nMatriz A");
        llenarM(A, n, scr);

        System.out.println("\nLlenar Matriz B");
        llenarM(B, n, scr);

        //Suma
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                suma[i][j] = A[i][j] + B[i][j];
            }
        }

        //Imprimir
        System.out.println("\nMatriz A");
        imprimirM(A, n);

        System.out.println("\nMatriz B");
        imprimirM(B, n);

        System.out.println("\nSuma de A + B");
        imprimirM(suma, n);
    }



    public static void llenarM(int[][] matriz, int n, Scanner scr){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                System.out.print("[" + (i+1) + "][" + (j+1) + "]: ");
                matriz[i][j] = scr.nextInt();
            }
        }
    }


    
    public static void imprimirM(int[][] matriz, int n){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
    }
}

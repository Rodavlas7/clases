import java.util.*;

public class tabla_Cal {

    static String[] Alu = {"Gabriela", "Eduardo", "Susana", "Antonio", "Pedro"};
    static String[] Mat = {"Informatica", "Programacion", "Redes"};
    static double[][] Cal = new double[Alu.length][Mat.length];

    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

                for (int i = 0; i < Alu.length; i++) {
            for (int j = 0; j < Mat.length; j++) {
                System.out.print("[" + Alu[i] + "][" + Mat[j] + "]: ");
                double num = scr.nextDouble();
                while (num < 0 || num > 100) {
                    System.out.print("  Valor inválido. Ingresa 0–100: ");
                    num = scr.nextDouble();
                }
                Cal[i][j] = num;
            }
            System.out.println();
        }

        imprimirEncabezado();
        imprimirCal();
        imprimirPromediosPorMateria();
        scr.close();
    }

    static void imprimirEncabezado() {
        System.out.print("Alumno\t\t");
        for (int j = 0; j < Mat.length; j++) {
            System.out.print(Mat[j] + "\t");
        }
        System.out.println("Promedio");
    }

    static void imprimirCal() {
        for (int i = 0; i < Alu.length; i++) {
            System.out.print(Alu[i] + "\t");
            if (Alu[i].length() < 8) System.out.print("\t");

            double suma = 0;
            for (int j = 0; j < Mat.length; j++) {
                System.out.print(Cal[i][j] + "\t");
                suma += Cal[i][j];
            }

            double promedio = Math.round((suma / Mat.length) * 100.0) / 100.0;
            System.out.println(promedio);
        }
    }

    static void imprimirPromediosPorMateria() {
        System.out.print("Promedio\t");
        for (int j = 0; j < Mat.length; j++) {
            double suma = 0;
            for (int i = 0; i < Alu.length; i++) {
                suma += Cal[i][j];
            }
            double promedio = Math.round((suma / Alu.length) * 100.0) / 100.0;
            System.out.print(promedio + "\t");
        }
        System.out.println();
    }
}
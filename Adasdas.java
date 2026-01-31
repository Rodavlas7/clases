import java.util.Scanner;

public class Adasdas {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);
        System.out.print("Cuantos empleados trabajaron? ");
        int empleados = scr.nextInt();
        int i= 1;
        int dias, j, horasDia;
        int total = 0;
        int totalDias = 0;
        int horasEmpleado = 0;
        String texto = "";
        
        while (i <= empleados) {
            
            System.out.print("Cuantos dias trabajo? ");
            dias = scr.nextInt();
            j = dias;
            horasEmpleado = 0;
            while (j > 0) {
                horasDia = 0;
                System.out.print("Cuantas horas trabajo? ");
                horasDia = scr.nextInt();
                horasEmpleado += horasDia;
                j--;
            }
            totalDias += dias;
            total += horasEmpleado;
            texto = texto + "El empleado " + (i) + " gano " + horasEmpleado*100 + " pesos por sus " + total + " horas en sus " + dias + " dias de trabajo \n";
            i++;
        }

        System.out.println(texto + "\n");
        System.out.println("A los " + empleados + " se les pago " + total*100 + " pesos en total, por sus " +  total + " horas en un total de entre todos " + totalDias + " laborables humano");

        scr.close();
    }
}

/* 
 * Sueldo hora 100
 * 
*/
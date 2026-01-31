import java.util.Scanner;

public class practica2_3 {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        float total = 0;
        float cal;

        System.out.print("Deme la primer calificacion: ");
        cal   = scr.nextFloat();
        total = total + cal;

        System.out.print("Deme la segunda calificacion: ");
        cal   = scr.nextFloat();
        total = total + cal;

        System.out.print("Deme la tercer calificacion: ");
        cal   = scr.nextFloat();
        total = total + cal;

        System.out.print("Deme la cuarta calificacion: ");
        cal   = scr.nextFloat();
        total = total + cal;

        total = total/4;

        if (total >= 8){
            System.out.println("El alumno aprobo con un " + total);
        } else {
            System.out.println("El alumno reprobo con un " + total);
        }

        scr.close();
    }
}

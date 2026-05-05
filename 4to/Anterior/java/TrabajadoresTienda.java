import java.util.Scanner;

public class TrabajadoresTienda {
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de repositores: ");
        int rep = scr.nextInt();
        System.out.print("Ingrese la cantidad de cajeros: ");
        int caj = scr.nextInt();
        System.out.print("Ingrese la cantidad de supervisores: ");
        int sup = scr.nextInt();

        System.out.println("\nCosto total de la nómina: $"  + (Repositor(rep) + Cajero(caj) + Supervisor(sup)));

        scr.close();
    }

    public static int Repositor(int rep) {
        if (rep == 0){
            return 0;
        }else{
        int total = rep*2875;
        System.out.println("Los repositores cobran $2500 mas un bono del 15% cada uno.");
        System.out.println("Para " + rep + " repositores, el total es: $" + total + "\n");
        return total;
        }
    }

    public static int Cajero(int caj) {
        if (caj == 0){
            return 0;
        }else{
        int total = caj * 3150;
        System.out.println("Los cajeros cobran $3150 cada uno.");
        System.out.println("Para " + caj + " cajeros, el total es: $" + total + "\n");
        return total;
        }
    }

    public static int Supervisor(int sup) {
        if (sup == 0){
            return 0;
        }else{
        int total = sup * 4050;
        System.out.println("Los supervisores cobran $4500 menos un descuento del 10% por jubilación cada uno.");
        System.out.println("Para " + sup + " supervisores, el total es: $" + total + "\n");
        return total;
        }
    }
}

/*
 * Funciones.
a Un pequeño supermercado desea calcular los sueldos de
sus empleados. Los puestos se dividen en 3 categorias:
1 Repositor 
2 Cajero 
3 Supervisor
a Los repositores cobran 2500 mas un bono del 15%.
a Los cajeros cobran 3150 fijos.
a Los supervisores cobran 4500 menos un descuento del 10% por jubilación.
Realizar un programa que dependiendo del tipo de
empleado calcule y muestre en pantalla el sueldo
correspondiente
 */
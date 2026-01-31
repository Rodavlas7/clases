import java.util.Scanner;

public class PicaFresas {
    public static void main(String[] args) {

        Scanner scr = new Scanner(System.in);

        System.out.print("¿Cuantas picafresas llevara? ");
        int pica = scr.nextInt();
        System.out.print("¿Cuantas Skwincles llevara? ");
        int skw = scr.nextInt();

        if (pica >= 12 && skw >= 12) {
            System.err.println("Se aplico el descuento de mayoreo en ambos productos \n" + " pica = " + (pica * 4.5)
                    + "\n" + " Skwincle = " + (skw * 9) + "\n" + " Total = " + ((pica * 4.5) + (skw * 9)));
        } else if (pica >= 12) {
            System.err.println("Se aplico el descuento de mayoreo en las pica fresas \n" + " pica = " + (pica * 4.5)
                    + "\n" + " Skwincle = " + (skw * 10) + "\n" + " Total = " + ((pica * 4.5) + (skw * 10)));
        } else if (skw >= 12) {
            System.err.println("Se aplico el descuento de mayoreo en los Swincles \n" + " pica = " + (pica * 5)
                    + "\n" + " Skwincle = " + (skw * 9) + "\n" + " Total = " + ((pica * 5) + (skw * 9)));
        }
        scr.close();
    }

}
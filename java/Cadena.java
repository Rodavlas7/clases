import java.util.Scanner;

public class Cadena{
    public static void main(String[] args) {
        Scanner scr = new Scanner(System.in);

        System.out.print("Deme un texto para contar espacios: ");        
        String text = scr.nextLine();


        System.out.println("El texto '" + text + "'' tiene " + contador(text) + " espacios");
        
        scr.close();
    }

    public static int contador (String text){
        
        int cont = 0;
        
        for (int i = 0; i <= (text.length()-1); i++){
            if ((text.charAt(i)) == ' '){
                cont++;
            }
        }

        return cont;
    }
}

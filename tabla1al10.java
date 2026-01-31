public class tabla1al10 {
    public static void main(String[] args) {
        multi();
    }

    public static void multi(){
        int num= 1;
        int cont;

        while (num <= 10) {
            cont = 1;
            while (cont <= 10) {
                System.out.print(num + " x " + cont + " = " + (cont*num) + "\t");
                cont++;
            }
            System.out.println("");
            num++;
        }
    }
}

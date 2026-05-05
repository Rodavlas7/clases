public class cambioDeVariables {
    
    public static void main(String[] args) {
        int var1 = 1;
        int var2 = 2;
        int var3 = 0;

        System.err.println(var1);
        System.out.println(var2);

        var3 = var1;
        var1 = var2;
        var2 = var3;
        
        System.err.println("Cambio");
        System.err.println(var1);
        System.out.println(var2);
    }
}

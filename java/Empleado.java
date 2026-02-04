class Empleado {
    String nombre, apellido;
    double salario;
    int edad;

    Empleado(String nombre, String apellido, int edad, double salario) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.salario = salario;
    }

    void info() {
        System.out.println(
                nombre + " " + apellido + " tiene " + edad + " años de edad y un salarios de " + salario + " monedas");
    }

    void aumento() {
        if (edad >= 40) {
            salario = salario * 1.10;
            System.out.println(nombre + " " + apellido + " obtuvo un aumento del 10% teniendo un sueldo nuevo de "
                    + salario + " monedas");
        } else {
            System.out.println(nombre + " " + apellido + " no es apto para el aumento");
        }
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public int getEdad() {
        return edad;
    }

    public double getSalario() {
        return salario;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}

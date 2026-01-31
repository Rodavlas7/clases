import java.util.Scanner;

public class TiendaDeJuegos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // se utiliza para capturar la entrada del usuario desde la consola

        // cuentas
        String[] usuarios = new String[10]; // arreglo para guardar hasta 10 nombres de usuario registrados
        String[] contrasenas = new String[10]; // arreglo para guardar las contraseñas asociadas a cada usuario
        int totalCuentas = 1; // contador para saber cuántas cuentas han sido creadas, inicia en 1 por la
                              // cuenta por defecto

        // cuenta por defecto
        usuarios[0] = "Desempleado"; // usuario por defecto para poder iniciar sesión sin necesidad de registrarse
        contrasenas[0] = "1234"; // contraseña del usuario por defecto

        // juegos disponibles
        String[] juegos = {
                "1. La Leyenda de Melda - $20",
                "2. Marvel Rivals Teamup - $15",
                "3. CraftMine - $25",
                "4. Galaga - $10",
                "5. Peppa Pig: THE GAME - $18",
                "6. Silk Song - $22"
        }; // arreglo que contiene los juegos disponibles para comprar

        String[] juegosComprados = new String[6]; // arreglo que almacena los juegos comprados por el usuario actual
        int cantidadComprados = 0; // contador que lleva la cantidad de juegos comprados

        // --- menú inicial: iniciar sesión o registrarse ---
        boolean accesoConcedido = false; // bandera para saber si el usuario ha iniciado sesión correctamente
        String usuarioActivo = ""; // guarda el nombre del usuario que ha iniciado sesión

        while (accesoConcedido == false) {
            System.out.println("\n=== Tienda de Juegos ===");
            System.out.println("1. Iniciar sesión");
            System.out.println("2. Crear cuenta");
            System.out.print("Elige una opción: ");
            int inicio = scanner.nextInt(); // variable que guarda la opción seleccionada en el menú inicial
            scanner.nextLine(); // limpiar buffer

            // iniciar sesión
            if (inicio == 1) {
                for (int intentos = 0; intentos < 3; intentos++) { // se permiten hasta 3 intentos para iniciar sesión
                    System.out.print("Usuario: ");
                    String usuario = scanner.nextLine(); // guarda el nombre de usuario ingresado
                    System.out.print("Contraseña: ");
                    String contrasena = scanner.nextLine(); // guarda la contraseña ingresada

                    boolean encontrado = false; // bandera que indica si las credenciales coinciden con alguna cuenta
                                                // registrada
                    for (int i = 0; i < totalCuentas; i++) {
                        if (usuario.equals(usuarios[i]) && contrasena.equals(contrasenas[i])) {
                            accesoConcedido = true; // se permite el acceso si las credenciales son correctas
                            usuarioActivo = usuario; // se guarda el nombre del usuario que inició sesión
                            encontrado = true;
                            break;
                        }
                    }
                    if (encontrado) {
                        break;
                    } else {
                        System.out.println("Credenciales incorrectas. Intenta de nuevo.");
                    }
                }
                if (!accesoConcedido) {
                    System.out.println("Demasiados intentos. Programa terminado.");
                    return; // finaliza el programa si no se logró iniciar sesión
                }

            } else if (inicio == 2) {
                // crear cuenta
                if (totalCuentas >= usuarios.length) {
                    System.out.println("No se pueden crear más cuentas."); // límite de cuentas alcanzado
                } else {
                    System.out.print("Elige un nombre de usuario: ");
                    String nuevoUsuario = scanner.nextLine(); // guarda el nuevo nombre de usuario a registrar

                    // revisar si ya existe
                    boolean yaExiste = false; // bandera para saber si el nombre de usuario ya está en uso
                    for (int i = 0; i < totalCuentas; i++) {
                        if (usuarios[i].equals(nuevoUsuario)) {
                            yaExiste = true;
                            break;
                        }
                    }

                    if (yaExiste) {
                        System.out.println("Ese usuario ya existe. Intenta con otro.");
                    } else {
                        System.out.print("Elige una contraseña: ");
                        String nuevaContrasena = scanner.nextLine(); // guarda la contraseña del nuevo usuario

                        usuarios[totalCuentas] = nuevoUsuario; // asigna el nuevo usuario al arreglo
                        contrasenas[totalCuentas] = nuevaContrasena; // asigna su contraseña
                        totalCuentas++; // incrementa el número total de cuentas registradas

                        System.out.println("Cuenta creada con éxito. ¡Ahora inicia sesión!");
                    }
                }
            } else {
                System.out.println("Opción no válida.");
            }

            // comprueba que los números solicitados sean 1 o 2
            if (inicio != 1 && inicio != 2) {
                accesoConcedido = false;
            }
        }

        // --- menú principal ---
        int opcion; // variable que almacena la opción elegida del menú principal
        do {
            System.out.println("\n--- Menú Principal ---");
            System.out.println("1. Comprar un juego");
            System.out.println("2. Ver juegos comprados");
            System.out.println("3. Salir");
            System.out.print("Selecciona una opción: ");
            opcion = scanner.nextInt(); // guarda la opción seleccionada por el usuario

            switch (opcion) {
                case 1:
                    System.out.println("\n--- Juegos Disponibles ---");
                    for (String juego : juegos) {
                        System.out.println(juego); // muestra la lista de juegos disponibles
                    }
                    System.out.print("Ingresa el número del juego que deseas comprar: ");
                    int compra = scanner.nextInt(); // guarda el número del juego que se desea comprar
                    scanner.nextLine(); // limpiar buffer

                    if (compra >= 1 && compra <= juegos.length) {
                        String juegoSeleccionado = juegos[compra - 1]; // guarda el juego que se ha elegido

                        // verificar si ya se compró
                        boolean yaComprado = false; // bandera que indica si el juego ya fue comprado
                        for (int i = 0; i < cantidadComprados; i++) {
                            if (juegosComprados[i].equals(juegoSeleccionado)) {
                                yaComprado = true;
                                break;
                            }
                        }

                        if (yaComprado) {
                            System.out
                                    .println("Ya has comprado este juego anteriormente. No puedes comprarlo de nuevo.");
                        } else {
                            // ingreso de datos de tarjeta
                            System.out.println("\n--- Ingreso de datos de tarjeta ---");
                            System.out.print("Nombre del titular: ");
                            String nombre = scanner.nextLine(); // guarda el nombre del titular de la tarjeta

                            System.out.print("Número de tarjeta (16 dígitos): ");
                            String numeroTarjeta = scanner.nextLine(); // guarda el número de tarjeta ingresado

                            System.out.print("Fecha de vencimiento (MM/AA): ");
                            String vencimiento = scanner.nextLine(); // guarda la fecha de vencimieno

                            System.out.print("CVV (3 dígitos): ");
                            String cvv = scanner.nextLine(); // guarda el cvv ingresado

                            // validaciones
                            boolean tarjetaValida = numeroTarjeta.matches("\\d{16}"); // verifica que la tarjeta tenga
                                                                                      // 16 dígitos numéricos
                            boolean cvvValido = cvv.matches("\\d{3}"); // verifica que el cvv tenga 3 dígitos numéricos
                            boolean vencimientoValido = vencimiento.matches("\\d{2}/\\d{2}"); // verifica el formato
                                                                                              // correcto de vencimiento

                            if (tarjetaValida && cvvValido && vencimientoValido) {
                                System.out.println("\nProcesando pago...");
                                System.out.println("Pago realizado con éxito. ¡Gracias por tu compra!");
                                juegosComprados[cantidadComprados] = juegoSeleccionado; // se guarda el juego en la
                                                                                        // lista de comprados
                                cantidadComprados++; // se incrementa el contador de juegos comprados
                            } else {
                                System.out.println("\nError en los datos de la tarjeta:");
                                if (!tarjetaValida)
                                    System.out.println("- El número de tarjeta debe tener 16 dígitos.");
                                if (!cvvValido)
                                    System.out.println("- El CVV debe tener 3 dígitos.");
                                if (!vencimientoValido)
                                    System.out.println("- El vencimiento debe estar en formato MM/AA.");
                                System.out.println("La compra no se ha realizado.");
                            }
                        }
                    } else {
                        System.out.println("Opción no válida."); // evita que compre 2 veces
                    }
                    break;

                case 2:
                    System.out.println("\n--- Juegos Comprados ---");
                    if (cantidadComprados == 0) {
                        System.out.println("Aún no has comprado juegos.");
                    } else {
                        for (int i = 0; i < cantidadComprados; i++) {
                            System.out.println(juegosComprados[i]); // muestra los juegos que han sido comprados
                        }
                    }
                    break;

                case 3:
                    System.out.println("Gracias por visitar la tienda. ¡Hasta luego!"); // mensaje de despedida
                    break;

                default:
                    System.out.println("Opción no válida."); // mensaje en caso de ingresar una opción incorrecta
            }

        } while (opcion != 3); // el menú se repite hasta que el usuario elija salir

        scanner.close(); // cierra el objeto scanner para liberar recursos
    }
}

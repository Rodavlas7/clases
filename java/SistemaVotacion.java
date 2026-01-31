import java.util.Scanner;

public class SistemaVotacion {

    // Nombres fijos para los 10 estudiantes (puede cambiarse por entrada manual si
    // se desea)
    static final String[] estudiantes = {
            "001", "002", "003", "004", "005",
            "006", "007", "008", "009", "010"
    };

    // Nombres de los puestos a votar
    static final String[] NOMBRES_PUESTOS = { "Presidente", "Consejero", "Tesorero", "Secretario" };

    // Número máximo de estudiantes y planillas por puesto
    static final int MAX_ESTUDIANTES = estudiantes.length;
    static final int MAX_PLANILLAS = 5;
    static final int TOTAL_PUESTOS = NOMBRES_PUESTOS.length;

    // Matriz de votos [puesto][planilla]
    static int[][] votos = new int[TOTAL_PUESTOS][MAX_PLANILLAS];

    // Lista de nombres de planillas por puesto [puesto][planilla]
    static String[][] planillasPorPuesto = new String[TOTAL_PUESTOS][MAX_PLANILLAS];

    // Cantidad real de planillas registradas por puesto
    static int[] cantidadPlanillasPorPuesto = new int[TOTAL_PUESTOS];

    // Arreglo para saber si un estudiante ya votó en cierto puesto
    // [estudiante][puesto]
    static boolean[][] votosRealizados = new boolean[MAX_ESTUDIANTES][TOTAL_PUESTOS];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean rellenos = false;
        boolean votado = false;
        boolean salir = false;
        String resp;

        // Bucle principal del sistema
        while (!salir) {
            System.out.println("\n===== Sistema de Votaciones =====");
            System.out.println("1. Iniciar sesión como Administrador");
            System.out.println("2. Iniciar sesión como Estudiante");
            System.out.println("3. Ver Resultados");
            System.out.println("4. Salir");
            System.out.print("Opción: ");
            int opcion = verificarInt(sc);

            switch (opcion) {
                case 1:
                    // Iniciar sesión como administrador
                    if (iniciarSesionAdmin(sc)) {
                        if (rellenos) {
                            System.out.println("Estas seguro de sobre escribir las planillas (s/n): ");
                            resp = sc.nextLine();
                            if (resp.equalsIgnoreCase("s")) {
                                reiniciarVotos();
                                registrarPlanillas(sc);
                                votado = false;
                                System.out.println("Planillas y votos reiniciados correctamente.");
                            }
                        } else {
                            registrarPlanillas(sc);
                            rellenos = true;
                        }
                    }
                    break;
                case 2:
                    // Iniciar sesión como estudiante
                    if (rellenos) {
                        int indiceEstudiante = iniciarSesionEstudiante(sc);
                        if (indiceEstudiante != -1) {
                            realizarVotacion(sc, indiceEstudiante);
                        }
                        votado = true;
                    } else {
                        System.out.println("Opcion invalida (no hay planillas registradas)");
                    }
                    break;
                case 3:
                    // Ver resultados
                    if (rellenos && votado) {
                        for (int p = 0; p < TOTAL_PUESTOS; p++) {
                            // Crear arreglos para candidatos y votos de este puesto
                            String[] candidatos = new String[cantidadPlanillasPorPuesto[p]];
                            int[] votosPuesto = new int[cantidadPlanillasPorPuesto[p]];

                            for (int i = 0; i < cantidadPlanillasPorPuesto[p]; i++) {
                                candidatos[i] = planillasPorPuesto[p][i];
                                votosPuesto[i] = votos[p][i];
                            }

                            System.out.println("\nResultados para " + NOMBRES_PUESTOS[p] + ":");
                            mostrarResultados(candidatos, votosPuesto);
                        }
                    } else {
                        System.out.println("Opción inválida (no hay planillas registradas o nadie ha votado)");
                    }
                    break;
                case 4:
                    // Salir del sistema
                    salir = true;
                    break;
                default:
                    System.out.println("Opción inválida.");
            }
        }
        sc.close();

    }

    // Validación simple de sesión para administrador
    static boolean iniciarSesionAdmin(Scanner sc) {
        System.out.print("Contraseña de administrador: ");
        String pass = sc.nextLine();
        return pass.equalsIgnoreCase("1234"); // Puedes cambiar la contraseña aquí
    }

    // Inicia sesión para estudiante comparando con el arreglo de nombres
    static int iniciarSesionEstudiante(Scanner sc) {
        System.out.print("Clave unica de acceso: ");
        String user = sc.nextLine();

        for (int i = 0; i < MAX_ESTUDIANTES; i++) {
            if (estudiantes[i].equalsIgnoreCase(user)) {
                return i; // Devuelve índice del estudiante
            }
        }
        System.out.println("Estudiante no encontrado.");
        return -1;
    }

    // Función para que el admin registre las planillas por cada puesto
    static void registrarPlanillas(Scanner sc) {
        for (int p = 0; p < TOTAL_PUESTOS; p++) {
            System.out.println("\n--- Registro de planillas para " + NOMBRES_PUESTOS[p] + " ---");
            int cantidad;
            do {
                System.out.print("¿Cuántas planillas quieres registrar? (mínimo 2, máximo " + MAX_PLANILLAS + "): ");
                cantidad = verificarInt(sc);
            } while (cantidad < 2 || cantidad > MAX_PLANILLAS);

            cantidadPlanillasPorPuesto[p] = cantidad;

            for (int i = 0; i < cantidad; i++) {
                System.out.print("Nombre de la planilla #" + (i + 1) + ": ");
                planillasPorPuesto[p][i] = sc.nextLine();
            }
        }
    }

    // Función que permite a un estudiante votar en cada puesto
    static void realizarVotacion(Scanner sc, int estudiante) {
        for (int p = 0; p < TOTAL_PUESTOS; p++) {
            if (votosRealizados[estudiante][p]) {
                System.out.println("Ya votaste para " + NOMBRES_PUESTOS[p] + ".");
                continue;
            }

            System.out.println("\nPlanillas para " + NOMBRES_PUESTOS[p] + ":");
            int cantidad = cantidadPlanillasPorPuesto[p];
            for (int i = 0; i < cantidad; i++) {
                System.out.println((i + 1) + ". " + planillasPorPuesto[p][i]);
            }

            int voto;
            do {
                System.out.print("Tu voto (elige el número): ");
                voto = verificarInt(sc);
            } while (voto < 1 || voto > cantidad);

            votos[p][voto - 1]++; // Se suma el voto a la planilla correspondiente
            votosRealizados[estudiante][p] = true; // Marca que ya votó en ese puesto
            System.out.println("Voto registrado correctamente para " + NOMBRES_PUESTOS[p]);
        }
    }

    // Función para mostrar los resultados finales (y detectar empate)
    public static void mostrarResultados(String[] candidatos, int[] votos) {
        System.out.println("\n--- Resultados ---");
        int maxVotos = -1;
        int indiceGanador = -1;
        boolean empate = false;

        // Mostrar votos por cada candidato
        for (int i = 0; i < candidatos.length; i++) {
            System.out.println(candidatos[i] + ": " + votos[i] + " votos");

            if (votos[i] > maxVotos) {
                maxVotos = votos[i];
                indiceGanador = i;
                empate = false;
            } else if (votos[i] == maxVotos) {
                empate = true;
            }
        }

        // Determinar si hay empate
        if (empate) {
            System.out.println("Empate detectado entre los siguientes candidatos:");
            for (int i = 0; i < candidatos.length; i++) {
                if (votos[i] == maxVotos) {
                    System.out.println("- " + candidatos[i] + " (" + votos[i] + " votos)");
                }
            }
        } else {
            System.out.println("Ganador: " + candidatos[indiceGanador] + " con " + maxVotos + " votos.");
        }
    }

    // Reinicia los votos y el historial de votos realizados
    static void reiniciarVotos() {
        for (int p = 0; p < TOTAL_PUESTOS; p++) {
            for (int i = 0; i < MAX_PLANILLAS; i++) {
                votos[p][i] = 0; // Reinicia votos
            }
        }

        for (int e = 0; e < MAX_ESTUDIANTES; e++) {
            for (int p = 0; p < TOTAL_PUESTOS; p++) {
                votosRealizados[e][p] = false; // Marca que nadie ha votado
            }
        }
    }

    static int verificarInt(Scanner sc) {
        boolean primer = true;
        int num = 0;

        while (true) {
            if (primer) {
                primer = false;
            } else {
                System.out.println("Introduzca un numero entero por favor: ");
            }

            if (sc.hasNextInt()) {
                num = sc.nextInt();
                sc.nextLine();
                return num;
            } else {
                sc.nextLine();
                primer = false;
            }
        }
    }

}
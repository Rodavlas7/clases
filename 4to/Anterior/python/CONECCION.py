import mysql.connector

def conectar_y_consultar(config, consulta_sql):
    try:
        conexion = mysql.connector.connect(**config)

        cursor = conexion.cursor(dictionary=True)
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()
        return resultados

    except mysql.connector.Error as error:
        print(f"Error de conexión o consulta: {error}")

configuracion = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'almacen3c',
    'charset': 'utf8mb4',
    'connect_timeout': 10
}

consulta = "SELECT * FROM SUCURSAL"
resultados = conectar_y_consultar(configuracion, consulta)

print("\n--- TABLA: SUCURSAL ---")
print(f"{'Código':<8}{'Nombre':<25}{'Calle':<25}{'Número':<10}{'Colonia':<25}{'Ciudad':<10}")
print("-" * 90)

for row in resultados:
    print(f"{row['codigo']:<8}{row['nombre']:<15}{row['dirCalle']:<25}{row['dirNum']:<10}{row['dirColonia']:<25}{row['ciudad']:<10}")

consulta = "SELECT * FROM CLIENTE"
resultados = conectar_y_consultar(configuracion, consulta)

print("\n--- TABLA: CLIENTE ---")
print(f"{'Num':<5}{'Nombre Fiscal':<35}{'Contacto Nombre':<20}{'Primer Apell.':<20}{'Segundo Apell.':<20}{'Teléfono':<18}{'Límite Cred.':<15}{'Crédito Disp.':<15}")
print("-" * 160)

for row in resultados:
    print(f"{row['num']:<5}{row['nombreFiscal']:<35}{row['contNombre']:<20}{row['contPrimerApell']:<20}{row['contSegApell'] or '':<20}{row['numTel']:<18}{row['limCredito']:<15}{row['creditoDisponible']:<15}")

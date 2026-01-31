<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

include("conexion.php");

/* Validar envío por POST */
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    die("Acceso no permitido");
}

/* Recibir datos */
$nombre = $_POST['nombre'] ?? '';
$correo = $_POST['correo'] ?? '';
$clave = $_POST['clave'] ?? '';
$edad = $_POST['edad'] ?? null;
$genero = $_POST['genero'] ?? '';
$comentarios = $_POST['comentarios'] ?? '';

/* Validar obligatorios */
if ($nombre === '' || $correo === '' || $clave === '') {
    die("❌ Faltan datos obligatorios");
}

/* Encriptar contraseña */
$clave_segura = password_hash($clave,
 PASSWORD_DEFAULT);

/* Preparar consulta */
$stmt = $conexion->prepare(
    "INSERT INTO usuarios (nombre, correo, clave,
    edad, genero, comentarios)
     VALUES (?, ?, ?, ?, ?, ?)"
);

$stmt->bind_param(
    "sssiss",
    $nombre,
    $correo,
    $clave_segura,
    $edad,
    $genero,
    $comentarios
);

/* Ejecutar */
if ($stmt->execute()) {
    echo "✅ Datos guardados correctamente";
} else {
    echo "❌ Error al guardar: " . $stmt->error;
}

$stmt->close();
$conexion->close();
?>
<?php
$servidor = "localhost";
$usuario = "root";
$clave = "";
$base_datos = "formulairio_db";

$conexion = new mysqli(hostname: $servidor, username: $usuario, password: $clave, database: $base_datos);

if ($conexion->connect_error) {
    die("Fallo la conexion: " . $conexion->connect_error);
}
?>


-- Active: 1762888131509@@127.0.0.1@3306@formulairio_db
CREATE DATABASE IF NOT EXISTS formulairio_db;

CREATE Table usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    clave VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    genero VARCHAR(50) NOT NULL,
    comentarios TEXT
);
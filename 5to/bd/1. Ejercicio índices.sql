-- Active: 1762888131509@@127.0.0.1@3306@biblos
CREATE DATABASE IF NOT EXISTS rbeIndices;
USE rbeIndices;

-- TABLA 1: marca
-- Se crea SIN índices ni llaves

CREATE TABLE marca (
    numero INT,
    nombre VARCHAR(30),
    pais VARCHAR(30),
    fundador VARCHAR(50),
    anioFundacion INT,
    telefono VARCHAR(15)
);

-- Agregar PRIMARY KEY con ALTER TABLE

ALTER TABLE marca
ADD CONSTRAINT pk_marca
PRIMARY KEY (numero);

-- Crear índice UNIQUE para el nombre

CREATE UNIQUE INDEX idx_unique_nombre
ON marca(nombre);

-- Crear índice NO ÚNICO para país

CREATE INDEX idx_pais
ON marca(pais);

-- Insertar registros de prueba

INSERT INTO marca VALUES
(1, 'Mercedes-Benz', 'Alemania', 'Karl Benz', 1926, '5551111111'),
(2, 'Volvo', 'Suecia', 'Assar Gabrielsson', 1927, '5552222222'),
(3, 'Scania', 'Suecia', 'Gustaf Erikson', 1891, '5553333333'),
(4, 'MAN', 'Alemania', 'Rudolf Diesel', 1758, '5554444444'),
(5, 'Irizar', 'España', 'José Antonio Irizar', 1889, '5555555555');

-- Mostrar índices de la tabla

SHOW INDEX FROM marca;


--======================
-- TABLA 2: tipo_pago
-- Se crea con:
-- PK
-- índice UNIQUE
-- índice NO ÚNICO
--======================


CREATE TABLE tipo_pago (
    numero INT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(50) NOT NULL,
    banco VARCHAR(40),
    telefono VARCHAR(15),

    UNIQUE INDEX idx_unique_nombre_pago(nombre),

    INDEX idx_banco(banco)
);

-- Insertar registros de prueba

INSERT INTO tipo_pago VALUES
(1, 'Efectivo', 'Pago en efectivo', 'Ninguno', '5551000001'),
(2, 'Tarjeta Visa', 'Pago con tarjeta Visa', 'BBVA', '5551000002'),
(3, 'MasterCard', 'Pago con MasterCard', 'Santander', '5551000003'),
(4, 'PayPal', 'Pago electrónico PayPal', 'PayPal Bank', '5551000004'),
(5, 'Transferencia', 'Pago por SPEI', 'Banorte', '5551000005');

-- Mostrar índices de la tabla

SHOW INDEX FROM tipo_pago;
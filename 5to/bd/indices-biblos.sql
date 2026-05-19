-- Active: 1762888131509@@127.0.0.1@3306@biblos
---------Indices en MYSQL
-- 1. Creac la bd y activarla

CREATE DATABASE if NOT EXISTS biblos;
use biblos;

--2 crear tabla
CREATE Table alumnos(
    matricula CHAR(4),
    documento CHAR(8),
    apellido VARCHAR(30),
    nombre VARCHAR(30),
    notaFinal DECIMAL(4,2) 
);

--3. Ponerle info

INSERT INTO alumnos values
('A123','22222222','Perez','Patricia',5.50),
('A234','33333333','Lopez','Ana',9.0),
('A345','24444444','Garcia','Carlos',8.50),
('A348','25555555','Perez','Daniela',7.85),
('A457','26666666','Perez','Fabian',3.20),
('A589','27777777','Gomez','Gaston',6.90);

SELECT * FROM alumnos;


-- Crear indices

--4. crear indice unico para el campo apellido
CREATE UNIQUE INDEX IUK_alumnos_apellido
ON alumnos(apellido); -- Da error por que como la tabla tiene datos que se repiten no permite crear el indice pq el valor ya se repite

-- 5 Crear un indice no unico para el campo apellido
CREATE INDEX INU_alumnos_apellido
ON alumnos(apellido);

-- 6. Ver indices de la tabla
SHOW INDEX FROM alumnos;

-- 7. Establecer la PK al campo matricula
alter Table alumnos
add constraint PK_alumnos_matricula
PRIMARY KEY(matricula);
alter Table alumnos
add PRIMARY KEY(matricula);

-- 8 Crear un indice no unico para el campo documento
CREATE UNIQUE INDEX IUK_alumnos_documento
ON alumnos(documento);

-- 9 intentar agregar un registro con un documento repetido
INSERT INTO alumnos values
('A098','22222222','Perez','Patricia',5.50);-- no se puede agregar por el indice repetido en el documento

-- 10 intentar agregar un registro con un documento diferente
INSERT INTO alumnos values
('A690','28888888','Lopez','Santiago',7.50); -- si deja pa pq no repite

-- 11 crear un indice compuesto para el campo apellido
CREATE INDEX I_alumnos_apellidoNombre
on alumnos(apellido, nombre);

-- 12 crear un indice desde la creacion de la tabla

CREATE Table departamento(
    codigo VARCHAR(4) PRIMARY KEY,
    nombre VARCHAR(15) NOT NULL UNIQUE
)

-- 13. Ver indices de la tabla
SHOW INDEX FROM departamento;

-------------------------
--- ELIMINAR INDICES
-------------------------

--- Los indices creados con create indes se eliminan con drop index
-- sintaxis base
DROP INDEX I_alumnos_apellidoNombre on alumnos;

-- lo indices que se crean automaticamente no pueden eliminarse con drop index, se eliminan cuando quitamos la restricciones alterando la tabla
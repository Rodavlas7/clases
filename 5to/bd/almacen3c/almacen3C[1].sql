-- Active: 1762888131509@@127.0.0.1@3306@almacen3c
-- Creacion de la base de datos ALMACEN
use almacen3C;

-- crear las tablas
create table ciudad(
    codigo varchar(5) PRIMARY KEY,
    nombre varchar(15) not null unique
);

create table producto(
    codigo varchar(5) PRIMARY KEY, 
    nombre varchar(20) not null, 
    descripcion varchar(90) not null, 
    precio float not null
);

create table concepto_pago(
    codigo varchar(5) PRIMARY KEY, 
    nombre varchar(15) not null unique
);

create table edo_pedido(
    codigo varchar(4) PRIMARY KEY, 
    descripcion varchar(15) not null unique
);

create table cliente(
    num int PRIMARY KEY auto_increment, 
    nombreFiscal varchar(50) not null,
    contNombre varchar(30) not null, 
    contPrimerApell varchar(30) not null, 
    contSegundoApell varchar(30) , 
    numTel varchar(15) not null, 
    limCredito float not null,
    creditoDisponible float not null
);

create table sucursal(
    codigo varchar(5) PRIMARY KEY, 
    nombre varchar(30) not null unique, 
    dirCalle varchar(30) not null, 
    dirNum varchar(10) not null, 
    dirColonea varchar(30) not null, 
    ciudad varchar(5) not null, 
    Foreign Key (ciudad) REFERENCES ciudad(codigo)
);

create table rep_vtas(
    num int PRIMARY KEY auto_increment,
    nombre varchar(30) not null, 
    primerApell varchar(30) not null,
    segApell varchar(30), 
    fechaContrato date not null, 
    director int, 
    sucursal varchar(5) not null,
    Foreign Key (sucursal) REFERENCES sucursal(codigo)
)

alter table rep_vtas
add constraint FK_rv_director
Foreign Key (director) REFERENCES rep_vtas(num);

create table almacen(
    sucursal varchar(5) not null, 
    productos varchar(5) not null, 
    stock int not null, 
    PRIMARY KEY (sucursal, productos),
    Foreign Key (sucursal) REFERENCES sucursal(codigo),
    Foreign Key (productos) REFERENCES producto(codigo)
);

create table meta(
    num int PRIMARY KEY auto_increment,
    fechaInicio date not null,
    fechaFinal date not null, 
    montoMeta float not null,
    montoVentas float,
    sucursal varchar(5),
    repVtas int,
    Foreign Key (sucursal) REFERENCES sucursal(codigo), 
    Foreign Key (repVtas) REFERENCES rep_vtas(num)
);

create table pedido(
    num int PRIMARY KEY auto_increment,
    fecha date not null,
    contTotalProd int,
    subtotal float,
    IVA float,
    total float,
    totalConInt float,
    sucursal varchar(5) not null,
    rep_vtas int  not null,
    cliente int not null,
    estado varchar(4) not null,
    Foreign Key (sucursal) REFERENCES sucursal(codigo),
    Foreign Key (rep_vtas) REFERENCES rep_vtas(num),
    Foreign Key (cliente) REFERENCES cliente(num),
    Foreign Key (estado) REFERENCES edo_pedido(codigo)
);

create table ped_prod(
    pedido int,
    producto varchar(5),
    cantidad int not null,
    importe float,
    Foreign Key (pedido) REFERENCES pedido(num),
    Foreign Key (producto) REFERENCES producto(codigo)
)

alter table ped_prod
add PRIMARY KEY (pedido, producto);

create table pago(
    numero int PRIMARY KEY auto_increment,
    fecha date not null,
    numPago int,
    montoPago float not null,
    saldo float,
    concepto varchar(5) not null,
    pedido int not null,
    Foreign Key (concepto) REFERENCES concepto_pago(codigo),
    Foreign Key (pedido) REFERENCES pedido(num)
);

-- agregar satos a la tabla ciudad 
-- solo  cuando quieres agregar un registro
insert into `ciudad` 
values('MEX','Mexicali');

select * from ciudad;

insert into ciudad values
('ROS', 'Rosarito'),
('TIJ', 'Tijuana'),
('ENS', "Ensenada");

--agregar datos a la tabla sucursal

insert into sucursal values 
('DIMIR','Díaz Mirón','Calle 4ta','8050','Centro','TIJ'),
('STAFE','Santa Fe','Oriente','7002 int 8','Santa Fe','TIJ'),
('CACHA','Cachanilla','Blvd. López Mateos','218','Industrial','MEX'),
('PABEN','Pabellón','Tijuana-Rosarito','300','Parcelas','TIJ'),
('QUICA','Quintas campestre','Blvd. Real de Baja California','23911','San Francisco','TIJ'),
('BAHIA','Bahía','Av. Reforma','124 int 4','Reforma','ENS'),
('STALU','Santa Lucía','Carr. Transpeninsular','135','Santa Lucía','ROS'),
('CETRO','Centro','Av. Ruíz','328','Centro','MEX'),
('PLCIO','Palacio','Av. López Mateos','1504 int 12','Zona Centro','ENS'),
('RESDL','Residencial','Blvd. Anahuac','1301','Fracc. Villa Residencial','MEX'),
('LPINS','Los Pinos','Blvd. Díaz Ordaz','303','Los Pinos','TIJ');

select * from sucursal;

-- consultas basicas 

-- 1. Desplegar codigo, nombre y ciudad de una sucursal 
SELECT codigo, nombre, ciudad
FROM sucursal;

-- 2. Desplegar la ciudad y el nombre de la sucursal ordenado por ciudad 
SELECT ciudad, nombre
FROM `sucursal` 
order by ciudad;

-- 3. Nombre y direccion de las sucursales en una columna de las sucursales 
SELECT nombre as Sucursal,
CONCAT(dirCalle, ' ', dirNum, ' ', dirColonea) as Direccion,
ciudad as Ciudad
FROM sucursal;

-- 4. Nombre y direccion de las sucursales en una columna de las sucursales 
SELECT ciudad as Ciudad, nombre as Sucursal,
CONCAT(dirCalle, ' ', dirNum, ' ', dirColonea) as Direccion
from `sucursal`
where ciudad = 'ENS';

-- 5. sucursales de la ciudad de enseada y mexicali con la direccion en una columna 
SELECT ciudad as Ciudad, nombre as Sucursal,
CONCAT(dirCalle, ' ', dirNum, ' ', dirColonea) as Direccion
from `sucursal`
where ciudad = 'ENS' or ciudad = 'MEX'
order by ciudad ;

-- 6. Datos de una sucursal con la direccion en una columna
SELECT codigo as Codigo, nombre as Sucursal,
CONCAT(dirCalle, ' ', dirNum, ' ', dirColonea) as Direccion,
ciudad as Ciudad
from `sucursal`
where codigo = 'STAFE'
order by ciudad ;

SELECT * FROM `rep_vtas`;

--insert de la tabla rep_vtas 

INSERT INTO rep_vtas VALUES
(1, 'David Alejandro', 'Zepeda', 'Urias', '2020-01-15', NULL, 'RESDL'),
(2, 'Fernando', 'Uriarte', 'Sosa', '2020-01-23', NULL, 'QUICA'),
(5, 'Alejandra', 'Jara', 'Granados', '2020-12-10', NULL, 'BAHIA'),
(6, 'Diana Angeles', 'Garcia', 'Cruz', '2021-02-15', NULL, 'DIMIR'),
(8, 'Humberto', 'Lopez', 'Avalos', '2021-08-25', NULL, 'PABEN'),
(10, 'Ruben', 'Acedo', 'Lopez', '2022-08-25', NULL, 'CACHA'),
(19, 'Jorge', 'Espinoza', 'Guzman', '2024-12-29', NULL, 'STAFE'),
(20, 'Ismael', 'Reyes', 'Ramos', '2024-03-08', NULL, 'STALU'),
(21, 'Luis Manuel', 'Piña', 'Ramirez', '2024-06-12', NULL, 'CETRO'),
(22, 'Carolina', 'Cervantes', 'Rivera', '2024-07-05', NULL, 'PLCIO'),
(23, 'Liliana', 'Ramos', 'Cardenas', '2024-11-16', NULL, 'LPINS'),
(3, 'Carlos', 'Salgado', 'Ortegon', '2020-05-03', 2, 'QUICA'),
(4, 'Eduardo', 'Martinez', 'Lopez', '2020-09-01', 1, 'RESDL'),
(7, 'Abel', 'Chino', 'Chavez', '2021-04-30', 1, 'RESDL'),
(9, 'Daniela Esmeralda', 'Garcia', 'Salcido', '2021-08-25', 6, 'DIMIR'),
(11, 'Jose Francisco Franklin', 'Chavarria', 'Mendoza', '2022-10-02', 6, 'DIMIR'),
(12, 'Alexis', 'Olvera', 'Zavala', '2022-10-27', 5, 'BAHIA'),
(13, 'Israel', 'Chan', 'Posadas', '2022-12-05', 6, 'DIMIR'),
(14, 'Jesus Antonio', 'Nava', 'Aguirre', '2023-02-06', 6, 'DIMIR'),
(15, 'Jose Luis', 'Vazquez', 'Gomez', '2023-02-27', 5, 'BAHIA'),
(16, 'Maria Isabel', 'Morales', 'Vazquez', '2023-05-08', 8, 'PABEN'),
(17, 'Ana Patricia', 'Vazquez', 'Mendoza', '2023-08-05', 5, 'BAHIA'),
(18, 'Alberto', 'Hernandez', 'Vazquez', '2023-12-05', 2, 'QUICA'),
(24, 'Pedro', 'Martinez', 'Gonzalez', '2025-03-06', 10, 'CACHA'),
(25, 'Alonso', 'Tamayo', 'Alborez', '2025-03-17', 8, 'PABEN'),
(26, 'Cecilia', 'Lopez', 'Leon', '2025-07-07', 10, 'CACHA');

select * from `meta`;

--insert de la tabla meta 

INSERT INTO meta VALUES
(1, '2025-01-01', '2025-01-31', 30000, 0, NULL, 6),
(2, '2025-01-01', '2025-01-31', 40000, 12837.036, NULL, 9),
(3, '2025-01-01', '2025-01-31', 36000, 11526.6225, NULL, 11),
(4, '2025-01-01', '2025-01-31', 27000, 0, NULL, 13),
(5, '2025-01-01', '2025-01-31', 38000, 12141.102, NULL, 14),
(6, '2025-01-01', '2025-01-31', 171000, 0, 'DIMIR', NULL),
(7, '2025-01-01', '2025-01-31', 25000, 0, 'STAFE', NULL),
(8, '2025-01-01', '2025-01-31', 23000, 0, 'CACHA', NULL),
(9, '2025-01-01', '2025-01-31', 35000, 0, 'PABEN', NULL),
(10, '2025-01-01', '2025-01-31', 83000, 0, NULL, 2),
(11, '2025-01-01', '2025-01-31', 35000, 2409.25, NULL, 3),
(12, '2025-01-01', '2025-01-31', 25000, 652.947, NULL, 15),
(13, '2025-01-01', '2025-01-31', 43000, 0, 'QUICA', NULL),
(14, '2025-01-01', '2025-01-31', 45000, 0, NULL, 5),
(15, '2025-01-01', '2025-01-31', 25000, 4962.5375, NULL, 12),
(16, '2025-01-01', '2025-01-31', 37000, 0, 'BAHIA', NULL),
(17, '2025-01-01', '2025-01-31', 45000, 0, 'STALU', NULL),
(18, '2025-01-01', '2025-01-31', 35000, 0, 'CETRO', NULL),
(19, '2025-01-01', '2025-01-31', 45000, 0, 'PLCIO', NULL),
(20, '2025-01-01', '2025-01-31', 50000, 0, NULL, 1),
(21, '2025-01-01', '2025-01-31', 42000, 19598.415, NULL, 4),
(22, '2025-01-01', '2025-01-31', 23000, 5288.8155, NULL, 7),
(23, '2025-01-01', '2025-01-31', 15000, 0, 'RESDL', NULL),
(24, '2025-01-01', '2025-01-31', 35000, 0, 'LPINS', NULL),
(25, '2025-02-01', '2025-02-28', 25000, 11018.771, NULL, 21),
(26, '2025-02-01', '2025-02-28', 25000, 9799.909, NULL, 24),
(27, '2025-02-01', '2025-02-28', 45000, 0, NULL, 11),
(28, '2025-02-01', '2025-02-28', 35000, 0, NULL, 13),
(29, '2025-02-01', '2025-02-28', 27000, 0, NULL, 14),
(30, '2025-02-01', '2025-02-28', 17000, 0, 'DIMIR', NULL);

--7. mostar los nombres de los clientes y sus contactos
-- forma 1 
select nombreFiscal, 
contNombre, contPrimerApell, contSegundoApell
from `cliente`;

-- forma 2 
select nombreFiscal,
concat(contNombre,' ' ,contPrimerApell,' ' ,contSegundoApell) 
as Contacto
from `cliente`;

-- forma 3 , cuando aparece null en el resultado
select nombreFiscal,
concat(contNombre,' ' ,contPrimerApell,' ' ,
        ifnull(contSegApell), ' ') 
as Contacto
from cliente;

-- 8. mostar el numeor del pedido, la fecha y el total
-- forma 1 
select num as Numero, fecha as Fecha, total as totalConInt
from pedido;

--forma 2
select num as Numero, Date_Format(fecha, "%d-%m-%y") as fecha,
totalConInt as total
from pedido;

-- 9. Mostrar los nombres de los clientes cuyo limite de credito sea 
--    mayor o igual a 40,000.
select nombreFiscal as Cliente, limCredito as Credito 
from cliente 
where limCredito >= 40000 ;

-- 10. lista de sucursales con sus metas, mostrar el  
--     el nombre de la sucursal y su meta 
select s.nombre as Sucursal, m.montoMeta as Meta
from sucursal as s
inner join meta as m on m.sucursal = s.codigo ;

-- 11. lista de sucursales con sus metas del mes de enero 
select Date_Format(m.fechaInicio, "%d-%m-%y") as fecha, 
s.nombre as Sucursal, m.montoMeta as Meta
from sucursal as s
inner join meta as m on m.sucursal = s.codigo 
where m.fechaInicio = "2025-02-01" ;

-- 12. Nombres de los rep_vtas que tienen registradas ventas en las metas 

select 
concat (rv.nombre, ' ', rv.primerApell, ' ', rv.segApell)
as "Representante de Ventas",
m.montoVentas as Ventas 
from rep_vtas as rv 
inner join meta as m on m.repVtas = rv.num
where montoVentas > 0;

-- 13.  Nombres de las sucursales que tienen metas registradas
--      colocar la fecha de inicio de cada meta y la meta  

select s.nombre as Nombre, m.montoMeta as Meta,
Date_Format(m.fechaInicio, "%d-%m-%y") as Fecha
from sucursal as s 
inner join meta as m on m.sucursal = s.codigo
-- la llave foranea es igual a la llave primaria de la otra tabla 
where m.montoMeta > 0 ;

-- 14. Mostrar los datos de los pedidos de UN mes  del mes (febrero)
--     numero del pedido 
--     fecha del pedido 
--     nombre del cliente 
--     total con intereses 

select p.num as Numero, 
date_format(p.fecha, "%d-%m-%y") as Fecha,
c.nombreFiscal as Nombre, 
p.totalConInt as Total
from pedido as p
inner join cliente as c on p.cliente = c.num
where month(p.fecha) = 2;
-- month es una funcion asi que hay una para cada opcion
-- month, year, day

-- 15. Lista de pedidos de un rp_vtas (9)
--     nombre completo del rp  
--     fecha del pedido 
--     nombre del cliente  
--     total con intereses 

select concat(rv.nombre, ' ', rv.primerApell, ' ', rv.segApell) as Nombre,
date_format(p.fecha, "%d-%m-%y") as Fecha, 
c.nombreFiscal as cliente,
p.totalConInt as Total 
from rep_vtas as rv
inner join pedido as p on p.rep_vtas = rv.num
inner join cliente as c on p.cliente = c.num
where p.rep_vtas = 9 ;

-- 16. Lista de los pedidos de una sucursal 
-- nombre de la sucursal 
-- numero del pedido 
-- fecha del pedido 
-- nombre del rep_vtas (completo)
-- nombre del cliente 
-- moto total con intereses 
use almacen3c;

select s.nombre as Nombre,
p.num as Numero,
date_format(p.fecha, "%d-%m-%a") as Fecha,
concat(rv.nombre, ' ', rv.primerApell, ' ', rv.segApell) 
as "Nombre Representante", 
c.nombreFiscal as Cliente,
p.totalConInt as Monto 
from sucursal as s 
inner join pedido as p on p.sucursal = s.codigo 
inner join cliente as c on p.cliente = c.num 
inner join rep_vtas as rv on p.rep_vtas = rv.num;


-- 17. Un pedido completo
-- Numero del pedido, 
-- fecha del pedido, 
-- nombre de la sucursal, 
-- nombre de la ciudad donde se encuentra la sucursal, 
-- nombre del representante de ventas, 
-- la cantidad de cada producto, 
-- nombre del producto, 
-- precio unitario, 
-- importe, subtotal, 
-- total, 
-- iva, 
-- total con intereses y 
-- cantidad total de productos
SELECT 
    p.num as Numero_Pedido,
    DATE_FORMAT(p.fecha, "%d/%m/%Y") AS Fecha,
    s.nombre AS Sucursal,
    c.nombre AS Ciudad,
    cl.nombreFiscal AS Cliente,
    CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell, '')) AS Representante_Ventas,
    pp.cantidad AS Cantidad,
    prod.codigo AS Codigo_Producto,
    prod.nombre AS Producto,
    prod.precio AS Precio_Unitario,
    pp.importe AS Importe,
    p.subtotal AS SubTotal,
    p.total AS Total,
    p.totalConInt AS Total_con_Intereses,
    p.IVA as IVA,
    p.cantTotalProd as Cantidad_Productos
FROM pedido AS p
INNER JOIN sucursal AS s ON p.sucursal = s.codigo
INNER JOIN ciudad AS c ON s.ciudad = c.codigo
INNER JOIN rep_vtas AS rv ON p.rep_vtas = rv.num
INNER JOIN ped_prod AS pp ON pp.pedido = p.num
INNER JOIN producto AS prod ON prod.codigo = pp.producto
INNER JOIN cliente AS cl ON cl.num = p.cliente
WHERE p.num = 1;

-- Cuando se pida una consulta que requiera una lista, vamos a buscar que minimo halla 3 tuplas, nunca enseñar al frontend la consulta tal como sale, hay que darle formato

-- 18 Monstrar los clientes que tienen un limite de credito entre 20mil y 40mil
-- Nombre del cliente
-- Limite de credito

--Forma 1
SELECT 
    nombreFiscal as Nombre,
    limCredito as Limite_de_Credito
FROM cliente
WHERE limCredito >= 2000 AND limCredito <= 40000;

-- Forma 2
SELECT 
    nombreFiscal as Nombre,
    limCredito as Limite_de_Credito
FROM cliente
WHERE limCredito BETWEEN 20000 AND 40000;

-- 19 Mostrar los vendedores que tienen metas por debajo de 30mil o mayores a 40mil
-- Nombre completo del RV en una columna
-- Monto de la meta
--Forma 1
SELECT 
CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell,'')) AS Representante_Ventas,
m.montoMeta AS Meta
FROM rep_vtas AS rv
INNER JOIN meta AS m ON rv.num = m.repVtas
WHERE m.montoMeta < 30000 OR m.montoMeta > 40000;
--Forma 2
SELECT 
CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell,'')) AS Representante_Ventas,
m.montoMeta AS Meta
FROM rep_vtas AS rv
INNER JOIN meta AS m ON rv.num = m.repVtas
WHERE m.montoMeta NOT BETWEEN 30000 AND 40000;

-- 20 MOstrar a los vendedores que trabjan en las sucursales QUICA o REDL
    -- Nombre de la sucursal
    -- Nombre completo del RV en una columna
-- Forma 1
SELECT 
s.nombre AS Sucursal,
CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell,'')) AS Representante_Ventas
FROM rep_vtas AS rv
INNER JOIN sucursal AS s ON rv.sucursal = s.codigo
WHERE s.codigo = 'QUICA' OR s.codigo = 'RESDL';
-- Forma 2
SELECT 
s.nombre AS Sucursal,
CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell,'')) AS Representante_Ventas
FROM rep_vtas AS rv
INNER JOIN sucursal AS s ON rv.sucursal = s.codigo
WHERE s.codigo IN ('QUICA', 'RESDL');

-- 21 Mostrar a los vendedore cuyo primer apellido comienza con M

SELECT 
CONCAT(primerApell, ' ', IFNULL(segApell,''), ' ',nombre) AS Representante_Ventas
FROM rep_vtas
WHERE primerApell LIKE 'G%';

-- 22 Mostrar lo clientes cuya razon social incluye un Y en su nombre, y tambien mostrar su limite de credito
SELECT
nombreFiscal as Cliente,
limCredito as Credito
FROM cliente
WHERE nombreFiscal LIKE '%y%';

-- 23 Mostrar las sucursales cuyos nombres terminan con la letra a
-- Nombre de la sucursal
-- Nombre de la ciudad en la que se encuentra

SELECT 
s.nombre as Sucursal, 
c.nombre as ciudad
FROM sucursal as s
INNER JOIN ciudad as c on s.ciudad = c.codigo
WHERE s.nombre LIKE '%a';

-- 24 Mostrar los nombres de la ciudades que tengan las letras e y a en su nombre en ese orden
-- forma 1
SELECT
nombre
FROM ciudad
WHERE nombre LIKE '%e%' and nombre LIKE '%a%';
-- forma 1
SELECT
nombre
FROM ciudad
WHERE nombre LIKE '%e%a%';

-- 25 Mostrar la lista de directores de cada sucursal
    -- NOmbre de la sucursal
    --Nombre completo del directo
SELECT 
CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell,'')) AS Representante_Ventas,
s.nombre as Sucursal
FROM sucursal as s
INNER join rep_vtas as rv on rv.sucursal = s.codigo
WHERE rv.director is NULL;

-- 26 Mostrar la lista de lo RV de una sucursal
    --Nombre de la sucursal
    --Nomber completo del RV

SELECT 
s.nombre as Sucursal,
CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell,'')) AS Representante_Ventas
FROM sucursal as s
INNER join rep_vtas as rv on rv.sucursal = s.codigo
WHERE s.codigo = 'QUICA';

-- FUNCIONES DE AGREGACION

-- 27 indicar la venta promedio de todos lo vendedoress

SELECT 
TRUNCATE(avg(montoVEntas), 2) as Promedio_Ventas
FROM meta;

-- 28 Mostrar la suma total de las ventas de todos lo vendedores

SELECT 
TRUNCATE(sum(montoVEntas), 2) as SumaTotal
FROM meta;

-- 29 Mostrar el mayor y menor monto de metas de los vendedores

SELECT
Max(montoMeta) as Meta_Maxima,
min(montoMeta) as Meta_Minima
FROM meta;

-- 30 Mostrar el numero de clientes que existen

SELECT
COUNT(nombreFiscal) as Total_CLientes
FROM cliente;

-- 31
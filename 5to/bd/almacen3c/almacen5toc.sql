-- Active: 1762888131509@@127.0.0.1@3306@almacen3c
--- CONSULTAS BÁSICAS PARA LA BD ALMACEN
-- 1. Mostrar los nombres de los clientes y sus contactos.
--      Nombre del cliente
--      Nombre completo del contacto, en una columna

create view v_cte_contacto as
select nombreFiscal as cliente,
concat(contNombre,' ' ,contPrimerApell,' ' ,ifnull(contSegApell, '')) as contacto
from cliente;


-- consultar todos los campos de la vista

select cliente, contacto
from v_cte_contacto;

select contacto
from v_cte_contacto
where cliente = 'Baby Ley';

-- 2. Mostrar el número de pedido, la fecha (con formato) y
--    el total de todos los pedidos

select num as Numero,
DATE_FORMAT(fecha, '%d/%m/%Y') as Fecha,
total
from pedido;

create view v_tolaXpedido as
select num as Numero,
fecha as Fecha,
total as Total
from pedido;

-- consultas de la vista

select numero, fecha, total
from v_tolaXpedido;


select 
    DATE_FORMAT(fecha, "%d/%m/%Y") as Fecha,
    numero,
    total
from v_tolaxpedido
where MONTH(fecha) = 2 ;

select 
    DATE_FORMAT(fecha, "%d/%m/%Y") as Fecha,
    numero,
    total
from v_tolaxpedido
where total > 5000 ;

select 
    DATE_FORMAT(fecha, "%d/%m/%Y") as Fecha,
    numero,
    total
from v_tolaxpedido
where numero = 8 ;





-- 3. Mostrar la lista de sucursales con sus metas de enero.
--      Nombre de la sucursal
--      Monto de la meta

SELECT 
    s.nombre AS " Nombre la sucursal\",
    m.montoMeta AS "Monto de la meta""
FROM meta m
JOIN sucursal s 
    ON m.sucursal = s.codigo
WHERE MONTH(m.fechaInicio) = 1;


-- 4. Mostrar la lista de vendedores de la  sucursal con código DIMIR:
--     Nombre de la sucursal
--     Nombre completo del vendedor, en una columna


-- 5. Lista de sucursales de la diudad de Tijuana
-- Nombre de la ciudad
-- Nombre de la sucursal

SELECT s.nombre
FROM sucursal as s
WHERE s.ciudad = 'TIJ' ;


-- 6. Nombre, monto de metas, monto de ventas y
-- sus fechas de inicio y fin del vendedor número 6.

SELECT 
    CONCAT(rv.nombre,' ' ,rv.primerApell,' ' ,ifnull(rv.segApell, '')) as Vendedor,
    m.montoMeta,
    m.montoVentas,
    DATE_FORMAT(m.fechaInicio,'%d/%m/%y') as FechaInicio,
    DATE_FORMAT(m.`fechaFinal`,'%d/%m/%y') as FechaInicio
FROM rep_vtas as rv
INNER JOIN sucursal as s ON rv.sucursal = s.codigo
INNER JOIN meta as m on m.`repVtas` = rv.num
WHERE m.repVtas = 6;

-- 7. Nombre de los vendedores que superan las ventas a 10000

SELECT 
    CONCAT(rv.nombre,' ' ,rv.primerApell,' ' ,ifnull(rv.segApell, '')) as Vendedor,
    m.`montoVentas`
FROM rep_vtas as rv
INNER JOIN meta AS m ON  rv.num = m.repVtas
WHERE m.montoVentas > 10000;

-- 8. Mostrar la lista de productos de la sucursal
-- con código "CACHA"

SELECT
    p.nombre as Producto,
    s.nombre as Sucursal
FROM producto as p
INNER JOIN almacen as a on p.codigo = a.producto
INNER JOIN sucursal as s on a.sucursal = s.codigo
WHERE s.codigo = 'CACHA';

/*

    9. Desplegar los datos del pedido número 5:
    -- Número del pedido
    -- Fecha
    -- Nombre de la sucursal
    -- Nombre de la ciudad
    -- Nombre del cliente
    -- Nombre del representante de ventas
    -- Código del producto
    -- Nombre del producto
    -- Precio unitario
    -- Cantidad de cada producto
    -- Importe por cada producto
    -- Subtotal
    -- IVA
    -- Total

*/

SELECT 
    p.num as Numero_Pedido,
    DATE_FORMAT(p.fecha, "%d/%m/%Y") AS Fecha,
    s.nombre AS Sucursal,
    c.nombre AS Ciudad,
    cl.nombreFiscal AS Cliente,
    CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell, '')) AS Representante_Ventas,
    prod.codigo AS Codigo_Producto,
    prod.nombre AS Producto,
    prod.precio AS Precio_Unitario,
    pp.importe AS Importe,
    pp.cantidad AS Cantidad,
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
WHERE p.num = 5;


-- TODAS LAS COLUMNAS DE LAS VISTAS DEBEN TENER UN ALIAS (NOMBRE)
-- EN UNA VISTA SE PUEDE COLOCAR TODO LO QUE SE PUEDE PONER EN UN SELECT
-- NO PUEDE INCLUIR UN ORDER BY, COMPUTE BY, etc.




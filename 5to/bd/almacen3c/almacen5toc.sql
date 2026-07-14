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


-- agregar codigo sucursal, codigo de ciudad y numero de representante de ventas a

drop view if exists v_clave;
create view v_clave as
SELECT 
    p.num as Numero_Pedido,
    p.fecha as Fecha,
    s.codigo as Codigo_Sucursal,
    s.nombre AS Sucursal,
    c.codigo as Codigo_Ciudad,
    c.nombre AS Ciudad,
    cl.num as Numero_Cliente,
    cl.nombreFiscal AS Cliente,
    rv.num as Numero_Representante_Ventas,
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
INNER JOIN cliente AS cl ON cl.num = p.cliente;

-- realizar 10 consultas de la vista

-- 1. Mostrar todos los datos de un pedido específico
SELECT Numero_Pedido, 
    date_format(Fecha, '%d/%m/%Y') as Fecha,
    Sucursal, 
    Ciudad, 
    Cliente, 
    Representante_Ventas, 
    Producto, 
    Precio_Unitario, 
    Importe, 
    SubTotal, 
    IVA, 
    Total, 
    Cantidad_Productos
FROM v_clave
WHERE Numero_Pedido = 5;

-- 2. Listar los pedidos realizados en un rango de fechas
SELECT Numero_Pedido, 
    date_format(Fecha, '%d/%m/%Y') as Fecha,
    Sucursal, 
    Ciudad, 
    Cliente,
    Representante_Ventas, 
    Producto, 
    Precio_Unitario, 
    Importe, 
    SubTotal, 
    IVA, 
    Total, 
    Cantidad_Productos
FROM v_clave
WHERE Fecha BETWEEN '2025-01-01' AND '2025-02-28'
ORDER BY Fecha;

--3. Mostrar todos los pedidos de un representante de ventas específico
SELECT Numero_Pedido, 
    date_format(Fecha, '%d/%m/%Y') as Fecha,
    Sucursal, 
    Ciudad, 
    Cliente, 
    Numero_Representante_Ventas,
    Representante_Ventas,
    Producto, 
    Precio_Unitario, 
    Total, 
    Cantidad_Productos
FROM v_clave
WHERE Numero_Representante_Ventas = 7;

--4. Mostrar todos los pedidos de un cliente
SELECT Numero_Pedido, 
    date_format(Fecha, '%d/%m/%Y') as Fecha,
    Sucursal, 
    Cliente, 
    Representante_Ventas,
    Producto, 
    Precio_Unitario, 
    Importe, 
    SubTotal, 
    IVA, 
    Total, 
    Cantidad_Productos
FROM v_clave
WHERE Cliente = 'El almendro';

--5. Mostrar el total de ventas por sucursal
SELECT Sucursal,    
    SUM(Total) AS Total_Ventas
FROM v_clave
GROUP BY Sucursal
ORDER BY Total_Ventas DESC;

-- 6. mostrar el numero de pedidos por cliente
SELECT Cliente, 
    COUNT(Numero_Pedido) AS Numero_Pedidos
FROM v_clave
GROUP BY Cliente
ORDER BY Numero_Pedidos DESC;

-- 7. Mostrar el total de ventas por representante de ventas
SELECT Representante_Ventas,    
    SUM(Total) AS Total_Ventas
FROM v_clave
GROUP BY Representante_Ventas
ORDER BY Total_Ventas DESC;

-- 8. Mostrar el total de ventas por ciudad
select Ciudad,    
    SUM(Total) AS Total_Ventas
FROM v_clave
GROUP BY Ciudad
ORDER BY Total_Ventas DESC;

-- 9. Mostrar el total de ventas por producto por ciudad
SELECT Producto, Ciudad,    
    SUM(cantidad) AS cantidad_vendida,
    Precio_Unitario
FROM v_clave
GROUP BY Producto, Ciudad
ORDER BY cantidad_vendida DESC;

-- 10. Mostrar el total de ventas por mes de una sucursal específica
SELECT 
    MONTH(Fecha) AS Mes,
    Sucursal,
    SUM(Total) AS Total_Ventas
FROM v_clave
WHERE Codigo_Sucursal = 'BAHIA'
GROUP BY Mes
ORDER BY Mes;


--Subconsutas
-- 1. Datos de los pedidos comprados por el mismo cliente, haciendo la busqueda por el nombre del cliente
-- Numero del pedido
-- Decha del pedido
-- Nombre de la sucursal
-- Nombre de la ciudad
-- Monto total de la compra

SELECT 
    p.num AS Numero_Pedido,
    DATE_FORMAT(p.fecha, '%d/%m/%Y') AS Fecha_Pedido,
    s.nombre AS Nombre_Sucursal,
    c.nombre AS Nombre_Ciudad,
    p.total AS Monto_Total
FROM pedido AS p
INNER JOIN sucursal AS s ON p.sucursal = s.codigo
INNER JOIN ciudad AS c ON s.ciudad = c.codigo
WHERE p.cliente IN (
    SELECT num 
    FROM cliente 
    WHERE nombreFiscal = 'El almendro'
);

-- 2. Sucursales de la ciudad de TIjuana
-- Nombre de la sucursal
-- Direccion en una columna

SELECT 
    s.nombre AS Nombre_Sucursal,
    CONCAT( s.dirCalle, ' #', s.dirNum, ', Col. ',  s.dirColonia) AS Direccion
FROM sucursal AS s
WHERE s.ciudad = (
    SELECT codigo 
    FROM ciudad 
    WHERE nombre = 'Tijuana'
);

-- 3. vendedores que tienen ventas menores al promedio
-- Nombre del vendedor
-- Monto de ventas

SELECT
    s.nombre AS Nombre_Sucursal,
    CONCAT(
        s.dirCalle,
        ' #', s.dirNum,
        ', Col. ',
        s.dirColonia
    ) AS Direccion
FROM sucursal AS s
WHERE s.ciudad = (
    SELECT codigo
    FROM ciudad
    WHERE nombre = 'Tijuana'
);



-- 3. Vendedores que tienen ventas menores al promedio
-- Nombre del vendedor
-- Monto de ventas

SELECT 
    CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell, '')) AS Nombre_Vendedor,
    m.montoVentas AS Monto_Ventas
FROM rep_vtas AS rv
INNER JOIN meta AS m ON rv.num = m.repVtas
WHERE m.montoVentas < (
    SELECT AVG(montoVentas) 
    FROM meta
);


-- 4. Representantes de ventas de la ciudad de Mexicali
-- Nombre de la sucursal
-- Nombre del representante de ventas

SELECT 
    s.nombre AS Nombre_Sucursal,
    CONCAT(rv.nombre, ' ', rv.primerApell, ' ', IFNULL(rv.segApell, '')) AS Nombre_Representante
FROM rep_vtas AS rv
INNER JOIN sucursal AS s ON rv.sucursal = s.codigo
WHERE s.ciudad = (
    SELECT codigo 
    FROM ciudad 
    WHERE nombre = 'Mexicali'
);

-- 5. Clientes que NO han realizado pedidos
-- Nombre del cliente
-- Límite de crédito

SELECT
    nombreFiscal AS Nombre_Cliente,
    limCredito AS Limite_Credito
FROM cliente
WHERE num NOT IN (
    SELECT cliente
    FROM pedido
);

-- 6. Productos que NO han sido vendidos
-- Código
-- Nombre
-- Descripción
-- Precio de venta

SELECT
    codigo AS Codigo,
    nombre AS Nombre,
    descripcion AS Descripcion,
    precio AS Precio_Venta
FROM producto
WHERE codigo NOT IN (
    SELECT producto
    FROM ped_prod
);

-- 7. Datos de las sucursales que han tenido pedidos
-- Nombre de la sucursal
-- Ciudad donde se encuentra
-- Director de la sucursal

SELECT
    s.nombre AS Nombre_Sucursal,
    c.nombre AS Ciudad,
    CONCAT(
        rv.nombre, ' ',
        rv.primerApell, ' ',
        IFNULL(rv.segApell, '')
    ) AS Director_Sucursal
FROM sucursal AS s
INNER JOIN ciudad AS c
    ON s.ciudad = c.codigo
INNER JOIN rep_vtas AS rv
    ON rv.num = (
        SELECT DISTINCT director
        FROM rep_vtas
        WHERE sucursal = s.codigo
          AND director IS NOT NULL
        LIMIT 1
    )
WHERE s.codigo IN (
    SELECT sucursal
    FROM pedido
);

delimiter $$
create or REPLACE TRIGGER tg_verificar_fecha_pago
before insert on pago
for each row
begin
    if new.fecha > curdate() or new.fecha = curdate() then
        signal sqlstate '45000' set message_text = 'La fecha de pago no puede ser posterior a la fecha actual';
    end if;
end $$
DELIMITER;

/*
    2. inicializar los campos calculados
*/

DELIMITER $$

CREATE or REPLACE trigger tg_inicializar_pedido
BEFORE INSERT on pedido
for each ROW
begin
    set new.fecha = CURRENT_TIMESTAMP;
    set new.subtotal = 0;
    set new.IVA = 0;
    set new.total = 0;
    set new.cantTotalProd = 0;
    set new.totalConInt = 0;
    set new.estado = "enpr";
end $$

DELIMITER;

SELECT * FROM edo_pedido;
SELECT * FROM pedido;

# Prueba
INSERT into pedido(sucursal, rep_vtas, cliente)
VALUES("QUICA",3,7);
/*
    Trigger para la tabla ped_prod

    Calcular el importe de cada producto en un pedido
        ANTES de realizar el registro del producto:
        --Verificar que el producto no existe en la sucursal
          enviar mensaje de error.
            -- Si el prodictp mp exoste en la sucursal,
               enviar mensaje de error
    -- si el producto existe en la sucursal, verificar que haya stock suficiente
    -- si no hay stock suficiennte, no se realizar el registro y enviar el mensaje correspondiente
    -- si hay stock suficiente, calcular el importe
*/
DELIMITER $$

CREATE OR REPLACE TRIGGER tg_verificar_existencias_producto
BEFORE INSERT ON ped_prod
FOR EACH ROW
BEGIN

    DECLARE vSucursal VARCHAR(5);
    DECLARE vStock INT;
    DECLARE vPrecio FLOAT;

    -- Obtener la sucursal
    SELECT sucursal
    INTO vSucursal
    FROM pedido
    WHERE num = NEW.pedido;

    -- Verificar que el producto exista
    IF NOT EXISTS(
        SELECT *
        FROM almacen
        WHERE sucursal = vSucursal
          AND productos = NEW.producto
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El producto no existe en la sucursal';
    END IF;

    -- Obtener existencias
    SELECT stock
    INTO vStock
    FROM almacen
    WHERE sucursal = vSucursal
      AND productos = NEW.producto;

    -- Verificar stock
    IF vStock < NEW.cantidad THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No hay existencias suficientes del producto para el pedido';
    END IF;

    -- Obtener precio
    SELECT precio
    INTO vPrecio
    FROM producto
    WHERE codigo = NEW.producto;

    -- Calcular importe
    SET NEW.importe = NEW.cantidad * vPrecio;

END$$
DELIMITER;


-- Para saber que productos no se encuentran en una sucursal específica
select 
    a.producto as producto,
    p.nombre as nombre,
    p.precio as precio
from almacen as a
inner join producto as p on a.producto = p.codigo 
where p.codigo not in (
    select 
        producto 
    from almacen 
    WHERE sucursal = 'QUICA')
GROUP BY producto;



/*

    4. Realizar el trigger para que se actualice el stock
        despues de que se registre un producto en un pedido

*/

DELIMITER $$
CREATE OR REPLACE TRIGGER tg_acualizar_stock_en_pedido
AFTER INSERT ON ped_prod
FOR EACH ROW
BEGIN
    UPDATE almacen
    SET stock = stock - NEW.cantidad
    WHERE sucursal = (
        SELECT sucursal
        FROM pedido
        WHERE num = NEW.pedido
    )
    AND productos = NEW.producto;
END$$
DELIMITER ;



-- Para saber que productos no se encuentran en una sucursal específica
select 
    sucursal as sucursal,
    producto as producto,
    sum(stock) as stock
from almacen
where sucursal = 'QUICA'
group by sucursal, producto;

insert INTO ped_prod(pedido, producto, cantidad) 
VALUES (21, 'mabe', 10);

/*
    5. Calcular los campos calculado de la tabla pedido despues de que se agregue un producto a un pedido
        -- Subtotal
        -- IVA
        -- Total
*/
DELIMITER $$
CREATE OR REPLACE TRIGGER tg_calcular_campos_pedido
AFTER INSERT ON ped_prod
FOR EACH ROW
BEGIN

    declare importeProductos float;
    declare candtidadProductos;

    SELECT 
        SUM(importe) into importeProductos,
        SUM(cantidad) into candtidadProductos
    FROM ped_prod 
    WHERE pedido = NEW.pedido;

    UPDATE pedido
    SET cantTotalProd = candtidadProductos,
        subtotal = importeProductos,
        iva = importeProductos * 0.16,
        total = importeProductos * 1.16,
        totalConInt = importeProductos * 1.16 * 1.10
    WHERE num = NEW.pedido;

end$$
DELIMITER;


DELIMITER $$
CREATE OR REPLACE TRIGGER tg_calcular_campos_pedido
AFTER INSERT ON ped_prod
FOR EACH ROW
BEGIN

    UPDATE pedido
    SET cantTotalProd = cantTotalProd + new.cantidad,
        total = total + new.importe*1.16,
        iva = total * 0.16
        subtotal = total - iva
        totalConInt = total * 1.10
    WHERE num = NEW.pedido;

end$$
DELIMITER;

/*

    Trigger tabla pago
    - Actualizar el numero de pago
    - Actualizar el saldo verificando si es el primero o en base a los pagos que se han realizado
    - Actualizar el estado del pedido a pagado si el saldo es 0

*/

DELIMITER $$
CREATE OR REPLACE TRIGGER tg_calcular_verificar_pago
BEFORE INSERT ON PAGO
FOR EACH ROW
BEGIN


    declare CantidadPagos INT;

    SELECT 
        COUNT(*) into CantidadPagos 
    from pago 
    where pedido = NEW.pedido;
    
    SET new.fecha = CURRENT_TIMESTAMP;

    if new.montoPago <= 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El monto del pago debe ser mayor a 0';
    END IF;

    if CantidadPagos = 0 THEN
        SET new.saldo = (SELECT totalConInt from pedido where num = NEW.pedido);
        SET new.numPago = 1;
    else
        SET new.saldo = (Select saldo from pago WHERE pedido = new.pedido and numPago = CantidadPagos);
        SET new.numPago = CantidadPagos + 1;
    END IF;

    if new.montoPago > new.saldo THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'El monto del pago no puede ser mayor al saldo del pedido';
    ELSE
        SET new.saldo = new.saldo - new.montoPago;
    END IF;

end$$
DELIMITER;




UPDATE pedido p
JOIN (
    SELECT
        pedido,
        SUM(cantidad) AS total_productos,
        SUM(importe) AS subtotal
    FROM ped_prod
    GROUP BY pedido
) pp
ON p.num = pp.pedido
SET
    p.cantTotalProd = pp.total_productos,
    p.subtotal = pp.subtotal,
    p.IVA = pp.subtotal * 0.16,
    p.total = pp.subtotal * 1.16;
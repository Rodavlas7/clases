-- Active: 1762888131509@@127.0.0.1@3306@almacen3c

/*

1. Cantidad de pedidos realizados a cada cliente
- nombre del cliente
- cantidad de pedidos realizados

*/

drop PROCEDURE sp_cantidad_pedidos_cliente_inner;
DELIMITER $$

CREATE PROCEDURE sp_cantidad_pedidos_cliente_inner()
BEGIN
    SELECT
        c.nombreFiscal AS cliente,
        COUNT(p.num) AS cantidad_pedidos
    FROM cliente c
    INNER JOIN pedido p ON c.num = p.cliente
    GROUP BY c.num, c.nombreFiscal
    ORDER BY cliente;
END $$

DELIMITER ;

call sp_cantidad_pedidos_cliente_inner();


/*


*/


DELIMITER $$
create Procedure sp_prodxsucursal(in suc varchar(5))
begin

    select
        p.nombre as Producto,
        p.precio as Precio,
        a.stock as Cantidad

    from almacen a
    inner join producto as p on p.codigo = a.producto
    WHERE suc = a.sucursal;

end $$

DELIMITER;

call sp_prodxsucursal('CACHA');

SELECT codigo from sucursal;


/*
Cantidad de ventas de un vendedor
nombre del vendedor
cantidad de ventas
*/


SELECT 
CONCAT(rv.nombre, ' ', rv.`primerApell`, ' ', IFNULL(rv.`segApell`, "")) as Vendedor,
COUNT(*) as Ventas
FROM pedido as p
INNER JOIN rep_vtas as rv on p.rep_vtas = rv.num
where p.rep_vtas = 3
;

DROP PROCEDURE IF EXISTS sp_ventasxvendedor;
DELIMITER $$

    CREATE PROCEDURE sp_ventasxvendedor
    (
        in numVendedor INTEGER,
        out nombreVend VARCHAR(92),
        out numVentas INTEGER
    )
        SELECT 
            CONCAT(rv.nombre, ' ', rv.`primerApell`, ' ', IFNULL(rv.`segApell`, "")),
            COUNT(*)
            into nombreVend, numVentas
        FROM pedido as p
        INNER JOIN rep_vtas as rv on p.rep_vtas = rv.num
        where p.rep_vtas = numVendedor;
    END$$

DELIMITER;
call sp_ventasxvendedor(3, @vendedor, @numeroVentas);
SELECT @vendedor AS NombreVendedor, @numeroventas AS NumeroVentas;


SELECT * from edo_pedido;
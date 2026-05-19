-- Active: 1762888131509@@127.0.0.1@3306@almacen3c
CREATE TABLE `almacen` (
  `sucursal` varchar(5) NOT NULL,
  `producto` varchar(5) NOT NULL,
  `stock` int(11) NOT NULL,
  PRIMARY KEY (`sucursal`,`producto`),
  KEY `producto` (`producto`),
  CONSTRAINT `almacen_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`),
  CONSTRAINT `almacen_ibfk_2` FOREIGN KEY (`producto`) REFERENCES `producto` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `ciudad` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `cliente` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `nombreFiscal` varchar(50) NOT NULL,
  `contNombre` varchar(30) NOT NULL,
  `contPrimerApell` varchar(30) NOT NULL,
  `contSegApell` varchar(30) DEFAULT NULL,
  `numTel` varchar(15) NOT NULL,
  `limCredito` float NOT NULL,
  `creditoDisponible` float DEFAULT NULL,
  PRIMARY KEY (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `concepto_pago` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `edo_pedido` (
  `codigo` varchar(4) NOT NULL,
  `descripcion` varchar(15) NOT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE KEY `descripcion` (`descripcion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `meta` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `fechaInicio` date NOT NULL,
  `fechaFinal` date NOT NULL,
  `montoMeta` float NOT NULL,
  `montoVentas` float DEFAULT NULL,
  `sucursal` varchar(5) DEFAULT NULL,
  `repVtas` int(11) DEFAULT NULL,
  PRIMARY KEY (`num`),
  KEY `sucursal` (`sucursal`),
  KEY `repVtas` (`repVtas`),
  CONSTRAINT `meta_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`),
  CONSTRAINT `meta_ibfk_2` FOREIGN KEY (`repVtas`) REFERENCES `rep_vtas` (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `pago` (
  `numero` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `numPago` int(11) DEFAULT NULL,
  `montoPago` float NOT NULL,
  `saldo` float DEFAULT NULL,
  `concepto` varchar(5) NOT NULL,
  `pedido` int(11) NOT NULL,
  PRIMARY KEY (`numero`),
  KEY `concepto` (`concepto`),
  KEY `pedido` (`pedido`),
  CONSTRAINT `pago_ibfk_1` FOREIGN KEY (`concepto`) REFERENCES `concepto_pago` (`codigo`),
  CONSTRAINT `pago_ibfk_2` FOREIGN KEY (`pedido`) REFERENCES `pedido` (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `pedido` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `cantTotalProd` int(11) DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `IVA` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `totalConInt` float DEFAULT NULL,
  `sucursal` varchar(5) NOT NULL,
  `rep_vtas` int(11) NOT NULL,
  `cliente` int(11) NOT NULL,
  `estado` varchar(4) NOT NULL,
  PRIMARY KEY (`num`),
  KEY `sucursal` (`sucursal`),
  KEY `rep_vtas` (`rep_vtas`),
  KEY `cliente` (`cliente`),
  KEY `estado` (`estado`),
  CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`),
  CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`rep_vtas`) REFERENCES `rep_vtas` (`num`),
  CONSTRAINT `pedido_ibfk_3` FOREIGN KEY (`cliente`) REFERENCES `cliente` (`num`),
  CONSTRAINT `pedido_ibfk_4` FOREIGN KEY (`estado`) REFERENCES `edo_pedido` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `ped_prod` (
  `pedido` int(11) NOT NULL,
  `producto` varchar(5) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `importe` float DEFAULT NULL,
  PRIMARY KEY (`pedido`,`producto`),
  KEY `producto` (`producto`),
  CONSTRAINT `ped_prod_ibfk_1` FOREIGN KEY (`pedido`) REFERENCES `pedido` (`num`),
  CONSTRAINT `ped_prod_ibfk_2` FOREIGN KEY (`producto`) REFERENCES `producto` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `producto` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(90) NOT NULL,
  `precio` float NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `rep_vtas` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `primerApell` varchar(30) NOT NULL,
  `segApell` varchar(30) DEFAULT NULL,
  `fechaContrato` date NOT NULL,
  `director` int(11) DEFAULT NULL,
  `sucursal` varchar(5) NOT NULL,
  PRIMARY KEY (`num`),
  KEY `sucursal` (`sucursal`),
  KEY `FK_rv_director` (`director`),
  CONSTRAINT `FK_rv_director` FOREIGN KEY (`director`) REFERENCES `rep_vtas` (`num`),
  CONSTRAINT `rep_vtas_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `sucursal` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `dirCalle` varchar(30) NOT NULL,
  `dirNum` varchar(10) NOT NULL,
  `dirColonia` varchar(30) NOT NULL,
  `ciudad` varchar(5) NOT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `ciudad` (`ciudad`),
  CONSTRAINT `sucursal_ibfk_1` FOREIGN KEY (`ciudad`) REFERENCES `ciudad` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- Active: 1762888131509@@127.0.0.1@3306@test
-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 27, 2025 at 04:08 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE almacen3c;
use almacen3c;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `almacen3c`
--

-- --------------------------------------------------------

--
-- Table structure for table `almacen`
--

CREATE TABLE `almacen` (
  `sucursal` varchar(5) NOT NULL,
  `producto` varchar(5) NOT NULL,
  `stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `almacen`
--

INSERT INTO `almacen` (`sucursal`, `producto`, `stock`) VALUES
('BAHIA', 'adol', 82),
('BAHIA', 'aetil', 72),
('BAHIA', 'anem', 52),
('BAHIA', 'cdeco', 50),
('BAHIA', 'jdeto', 79),
('BAHIA', 'paphi', 65),
('BAHIA', 'pdeco', 52),
('BAHIA', 'sadem', 90),
('BAHIA', 'sprov', 80),
('BAHIA', 'thum', 56),
('BAHIA', 'vblac', 62),
('CACHA', 'aoxi', 66),
('CACHA', 'apera', 99),
('CACHA', 'asbay', 66),
('CACHA', 'bbasu', 63),
('CACHA', 'bdes', 95),
('CACHA', 'cdeco', 57),
('CACHA', 'cloma', 77),
('CACHA', 'deant', 88),
('CACHA', 'deli', 59),
('CACHA', 'felav', 69),
('CACHA', 'julim', 89),
('CACHA', 'kitar', 70),
('CACHA', 'matin', 78),
('CACHA', 'peta4', 74),
('CACHA', 'plama', 89),
('CACHA', 'subbi', 60),
('CACHA', 'tabef', 60),
('CETRO', 'aliga', 89),
('CETRO', 'apera', 50),
('CETRO', 'asbay', 74),
('CETRO', 'cloma', 76),
('CETRO', 'plama', 57),
('CETRO', 'shape', 75),
('CETRO', 'tabef', 86),
('DIMIR', 'adol', 69),
('DIMIR', 'amzu', 92),
('DIMIR', 'anem', 70),
('DIMIR', 'aveh', 57),
('DIMIR', 'avv', 66),
('DIMIR', 'caso', 87),
('DIMIR', 'hter', 90),
('DIMIR', 'mabe', 95),
('LPINS', 'aliga', 71),
('LPINS', 'amzu', 69),
('LPINS', 'aoxi', 85),
('LPINS', 'arega', 50),
('LPINS', 'asbay', 71),
('LPINS', 'aveh', 52),
('LPINS', 'avv', 59),
('LPINS', 'bdes', 76),
('LPINS', 'cdeco', 54),
('LPINS', 'cpaya', 81),
('LPINS', 'cupro', 72),
('LPINS', 'deli', 92),
('LPINS', 'hocar', 96),
('LPINS', 'hter', 70),
('LPINS', 'jugeo', 53),
('LPINS', 'mabe', 64),
('LPINS', 'peta4', 69),
('LPINS', 'shape', 92),
('LPINS', 'subbi', 94),
('LPINS', 'thum', 88),
('PABEN', 'aliga', 79),
('PABEN', 'arega', 53),
('PABEN', 'bosur', 51),
('PABEN', 'cpaya', 70),
('PABEN', 'gobo', 58),
('PABEN', 'hocar', 82),
('PABEN', 'ladhe', 87),
('PABEN', 'lapam', 72),
('PABEN', 'sakid', 89),
('PABEN', 'shape', 72),
('PLCIO', 'arega', 58),
('PLCIO', 'aveh', 93),
('PLCIO', 'avv', 100),
('PLCIO', 'bosur', 85),
('PLCIO', 'cpaya', 94),
('PLCIO', 'cupro', 60),
('PLCIO', 'gobo', 63),
('PLCIO', 'hocar', 59),
('PLCIO', 'hter', 78),
('PLCIO', 'jugeo', 65),
('PLCIO', 'ladhe', 67),
('PLCIO', 'lapam', 69),
('PLCIO', 'sakid', 58),
('QUICA', 'amzu', 94),
('QUICA', 'aveh', 77),
('QUICA', 'avv', 99),
('QUICA', 'caso', 81),
('QUICA', 'cupro', 100),
('QUICA', 'hter', 75),
('QUICA', 'jugeo', 89),
('QUICA', 'mabe', 71),
('RESDL', 'adol', 50),
('RESDL', 'aetil', 91),
('RESDL', 'amzu', 86),
('RESDL', 'anem', 84),
('RESDL', 'caso', 78),
('RESDL', 'jdeto', 91),
('RESDL', 'mabe', 100),
('RESDL', 'paphi', 96),
('RESDL', 'pdeco', 90),
('RESDL', 'sadem', 81),
('RESDL', 'sprov', 58),
('RESDL', 'vblac', 59),
('STAFE', 'adol', 100),
('STAFE', 'aetil', 71),
('STAFE', 'cdeco', 97),
('STAFE', 'jdeto', 93),
('STAFE', 'paphi', 87),
('STAFE', 'pdeco', 73),
('STAFE', 'sadem', 80),
('STAFE', 'sprov', 69),
('STAFE', 'thum', 81),
('STAFE', 'vblac', 69),
('STALU', 'aoxi', 62),
('STALU', 'bbasu', 59),
('STALU', 'bdes', 88),
('STALU', 'deant', 74),
('STALU', 'deli', 92),
('STALU', 'felav', 87),
('STALU', 'julim', 81),
('STALU', 'kitar', 81),
('STALU', 'matin', 67),
('STALU', 'peta4', 52),
('STALU', 'subbi', 71);

-- --------------------------------------------------------

--
-- Table structure for table `ciudad`
--

CREATE TABLE `ciudad` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ciudad`
--

INSERT INTO `ciudad` (`codigo`, `nombre`) VALUES
('ENS', 'Ensenada'),
('MEX', 'Mexicali'),
('ROS', 'Rosarito'),
('TIJ', 'Tijuana');

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `num` int(11) NOT NULL,
  `nombreFiscal` varchar(50) NOT NULL,
  `contNombre` varchar(30) NOT NULL,
  `contPrimerApell` varchar(30) NOT NULL,
  `contSegApell` varchar(30) DEFAULT NULL,
  `numTel` varchar(15) NOT NULL,
  `limCredito` float NOT NULL,
  `creditoDisponible` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`num`, `nombreFiscal`, `contNombre`, `contPrimerApell`, `contSegApell`, `numTel`, `limCredito`, `creditoDisponible`) VALUES
(1, 'Los Carreño', 'Gina', 'Córdoba', 'Liszt', '(664)125 48 97', 20000, 0),
(2, 'Abarrotes GranDecito', 'Joana', 'Mar', '', '(664)854 97 56', 20000, 0),
(3, 'Chedrauito cuesta menos', 'Manuel', 'Méndez', 'Hernández', '(664)624 10 37', 15000, 0),
(4, 'Baby Ley', 'José ', 'Pérez', 'Salas', '(664)548 67 00', 65000, 0),
(5, 'Las Güeritas', 'Jesús', 'Vázquez', 'Arce', '(664)810 47 11', 25000, 0),
(6, 'El almendro', 'Paola', 'Marín', 'Ceballos', '(664)487 12 94', 35000, 0),
(7, 'Esquina de la calle', 'Martha', 'Castro', 'Carreño', '(664)485 62 78', 32000, 0),
(8, 'Junior Hnos.', 'Jorge', 'Carrasco', 'Martínez', '(664)421 69 37', 28000, 0),
(9, 'Tienda Máximo', 'Juan Antonio', 'López', 'García', '(664)458 13 79', 23000, 0),
(10, 'Calidad Máxima', 'Marco', 'Solano', 'Fernández', '(664)547 92 01', 25000, 0),
(11, 'Mercado Downtown', 'Raul', 'Lucio', 'Váldez', '(664)210 34 78', 48000, 0),
(12, 'Tarifa Familiar', 'Yadira', 'Valdéz', 'Medina', '(664)541 26 71', 12000, 0),
(13, 'Lo Mejor Está Aquí', 'Israel', 'González ', 'Niebla', '(664)520 13 97', 14000, 0),
(14, 'Despensa De Comida Dorada', 'Noe', 'Rivas', 'Gutierrez', '(664)217 95 04', 15000, 0),
(15, 'Mercado Del Ayuntamiento', 'Andrés ', 'Espinoza', 'Manzano', '(664)630 14 75', 20000, 0),
(16, 'Tiendas De Referencia', 'Selene', 'Orozco', 'Bracamontes', '(664)952 13 42', 15000, 0),
(17, 'Ahorros Para Ti ', 'Rogelio', 'Velazco', 'Campos', '(664)120 94 21', 32000, 0),
(18, 'Tienda Keymart ', 'Angeles', 'Mayen', 'Padua', '(664)951 35 70', 16000, 0),
(19, 'Carrito De Compras ', 'Jonathan', 'Rabelero', 'Aguilar', '(664)456 25 87', 25000, 0),
(20, 'Abarrotes Generales Silver Creek', 'Enrique', 'Díaz', 'Zavala', '(664)521 63 79', 20000, 0),
(21, 'Tiendas Smartmart', 'Teresa', 'Martínez', 'Franco', '(664)589 20 17', 20000, 0);

-- --------------------------------------------------------

--
-- Table structure for table `concepto_pago`
--

CREATE TABLE `concepto_pago` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `concepto_pago`
--

INSERT INTO `concepto_pago` (`codigo`, `nombre`) VALUES
('abon', 'Abono'),
('liqui', 'Liquidación'),
('pagun', 'Pago único'),
('pripa', 'Primer pago');

-- --------------------------------------------------------

--
-- Table structure for table `edo_pedido`
--

CREATE TABLE `edo_pedido` (
  `codigo` varchar(4) NOT NULL,
  `descripcion` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edo_pedido`
--

INSERT INTO `edo_pedido` (`codigo`, `descripcion`) VALUES
('canc', 'Cancelado'),
('devo', 'Devolución'),
('enpr', 'En proceso'),
('term', 'Terminado');

-- --------------------------------------------------------

--
-- Table structure for table `meta`
--

CREATE TABLE `meta` (
  `num` int(11) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFinal` date NOT NULL,
  `montoMeta` float NOT NULL,
  `montoVentas` float DEFAULT NULL,
  `sucursal` varchar(5) DEFAULT NULL,
  `repVtas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `meta`
--

INSERT INTO `meta` (`num`, `fechaInicio`, `fechaFinal`, `montoMeta`, `montoVentas`, `sucursal`, `repVtas`) VALUES
(1, '2025-01-01', '2025-01-31', 30000, 0, NULL, 6),
(2, '2025-01-01', '2025-01-31', 40000, 12837, NULL, 9),
(3, '2025-01-01', '2025-01-31', 36000, 11526.6, NULL, 11),
(4, '2025-01-01', '2025-01-31', 27000, 0, NULL, 13),
(5, '2025-01-01', '2025-01-31', 38000, 12141.1, NULL, 14),
(6, '2025-01-01', '2025-01-31', 171000, 0, 'DIMIR', NULL),
(7, '2025-01-01', '2025-01-31', 25000, 0, 'STAFE', NULL),
(8, '2025-01-01', '2025-01-31', 23000, 0, 'CACHA', NULL),
(9, '2025-01-01', '2025-01-31', 35000, 0, 'PABEN', NULL),
(10, '2025-01-01', '2025-01-31', 83000, 0, NULL, 2),
(11, '2025-01-01', '2025-01-31', 35000, 2409.25, NULL, 3),
(12, '2025-01-01', '2025-01-31', 25000, 652.947, NULL, 15),
(13, '2025-01-01', '2025-01-31', 43000, 0, 'QUICA', NULL),
(14, '2025-01-01', '2025-01-31', 45000, 0, NULL, 5),
(15, '2025-01-01', '2025-01-31', 25000, 4962.54, NULL, 12),
(16, '2025-01-01', '2025-01-31', 37000, 0, 'BAHIA', NULL),
(17, '2025-01-01', '2025-01-31', 45000, 0, 'STALU', NULL),
(18, '2025-01-01', '2025-01-31', 35000, 0, 'CETRO', NULL),
(19, '2025-01-01', '2025-01-31', 45000, 0, 'PLCIO', NULL),
(20, '2025-01-01', '2025-01-31', 50000, 0, NULL, 1),
(21, '2025-01-01', '2025-01-31', 42000, 19598.4, NULL, 4),
(22, '2025-01-01', '2025-01-31', 23000, 5288.82, NULL, 7),
(23, '2025-01-01', '2025-01-31', 15000, 0, 'RESDL', NULL),
(24, '2025-01-01', '2025-01-31', 35000, 0, 'LPINS', NULL),
(25, '2025-02-01', '2025-02-28', 25000, 11018.8, NULL, 21),
(26, '2025-02-01', '2025-02-28', 25000, 9799.91, NULL, 24),
(27, '2025-02-01', '2025-02-28', 45000, 0, NULL, 11),
(28, '2025-02-01', '2025-02-28', 35000, 0, NULL, 13),
(29, '2025-02-01', '2025-02-28', 27000, 0, NULL, 14),
(30, '2025-02-01', '2025-02-28', 17000, 0, 'DIMIR', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pago`
--

CREATE TABLE `pago` (
  `numero` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `numPago` int(11) DEFAULT NULL,
  `montoPago` float NOT NULL,
  `saldo` float DEFAULT NULL,
  `concepto` varchar(5) NOT NULL,
  `pedido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pedido`
--

CREATE TABLE `pedido` (
  `num` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cantTotalProd` int(11) DEFAULT NULL,
  `subtotal` float DEFAULT NULL,
  `IVA` float DEFAULT NULL,
  `total` float DEFAULT NULL,
  `totalConInt` float DEFAULT NULL,
  `sucursal` varchar(5) NOT NULL,
  `rep_vtas` int(11) NOT NULL,
  `cliente` int(11) NOT NULL,
  `estado` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pedido`
--

INSERT INTO `pedido` (`num`, `fecha`, `cantTotalProd`, `subtotal`, `IVA`, `total`, `totalConInt`, `sucursal`, `rep_vtas`, `cliente`, `estado`) VALUES
(1, '2025-01-12', 22, 7327.5, 1172.4, 8499.9, 9774.89, 'DIMIR', 11, 6, 'term'),
(2, '2025-01-03', 1, 85.34, 13.66, 99, 113.85, 'RESDL', 4, 12, 'term'),
(3, '2025-01-19', 10, 873.02, 139.68, 1012.7, 1164.61, 'DIMIR', 9, 2, 'term'),
(4, '2025-01-07', 4, 1027.59, 164.41, 1192, 1370.8, 'QUICA', 3, 18, 'term'),
(5, '2025-01-28', 22, 2468.73, 395, 2863.73, 3293.29, 'BAHIA', 12, 5, 'term'),
(6, '2025-01-06', 17, 6516.79, 1042.69, 7559.48, 8693.4, 'DIMIR', 9, 11, 'term'),
(7, '2025-01-03', 8, 458.55, 73.37, 531.92, 611.71, 'RESDL', 7, 1, 'term'),
(8, '2025-01-05', 3, 537.05, 85.93, 622.98, 716.43, 'DIMIR', 9, 2, 'term'),
(9, '2025-01-04', 1, 602.59, 96.41, 699, 803.85, 'DIMIR', 9, 20, 'term'),
(10, '2025-01-07', 7, 8190.95, 1310.55, 9501.5, 10926.7, 'RESDL', 4, 8, 'term'),
(11, '2025-01-09', 3, 489.47, 78.31, 567.78, 652.95, 'BAHIA', 15, 17, 'term'),
(12, '2025-01-09', 7, 778.45, 124.55, 903, 1038.45, 'QUICA', 3, 3, 'term'),
(13, '2025-01-24', 13, 1313.15, 210.1, 1523.25, 1751.74, 'DIMIR', 11, 15, 'term'),
(14, '2025-01-02', 8, 1093.52, 174.96, 1268.48, 1458.75, 'DIMIR', 9, 9, 'term'),
(15, '2025-01-10', 11, 1251.31, 200.21, 1451.52, 1669.25, 'BAHIA', 12, 2, 'term'),
(16, '2025-01-13', 19, 9101.28, 1456.2, 10557.5, 12141.1, 'DIMIR', 14, 11, 'term'),
(17, '2025-02-05', 17, 3506.08, 560.97, 4067.05, 4677.11, 'RESDL', 7, 14, 'term'),
(18, '2025-02-06', 9, 6415.17, 1026.43, 7441.6, 8557.84, 'RESDL', 4, 5, 'term'),
(19, '2025-02-18', 27, 8259.95, 1321.59, 9581.54, 11018.8, 'CETRO', 21, 19, 'term'),
(20, '2025-02-28', 34, 7346.26, 1175.4, 8521.66, 9799.91, 'CACHA', 24, 8, 'term');

-- --------------------------------------------------------

--
-- Table structure for table `ped_prod`
--

CREATE TABLE `ped_prod` (
  `pedido` int(11) NOT NULL,
  `producto` varchar(5) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `importe` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ped_prod`
--

INSERT INTO `ped_prod` (`pedido`, `producto`, `cantidad`, `importe`) VALUES
(1, 'aveh', 10, 1176.4),
(1, 'avv', 2, 333.5),
(1, 'caso', 10, 6990),
(2, 'vblac', 1, 99),
(3, 'anem', 10, 1012.7),
(4, 'cupro', 4, 1192),
(5, 'aetil', 7, 507.64),
(5, 'pdeco', 6, 1497.6),
(5, 'sadem', 1, 66.49),
(5, 'vblac', 8, 792),
(6, 'adol', 8, 1268.48),
(6, 'caso', 9, 6291),
(7, 'sadem', 8, 531.92),
(8, 'hter', 3, 622.98),
(9, 'caso', 1, 699),
(10, 'amzu', 5, 511.5),
(10, 'mabe', 10, 8990),
(11, 'thum', 3, 567.78),
(12, 'jugeo', 7, 903),
(13, 'amzu', 10, 1023),
(13, 'avv', 3, 500.25),
(14, 'adol', 8, 1268.48),
(15, 'anem', 6, 607.62),
(15, 'sprov', 5, 843.9),
(16, 'adol', 8, 1268.48),
(16, 'caso', 3, 2097),
(16, 'mabe', 8, 7192),
(17, 'aetil', 3, 217.56),
(17, 'anem', 5, 506.35),
(17, 'paphi', 9, 3343.14),
(18, 'mabe', 8, 7192),
(18, 'pdeco', 1, 249.6),
(19, 'aliga', 1, 506.38),
(19, 'apera', 8, 5192),
(19, 'asbay', 4, 609.68),
(19, 'cloma', 10, 2148.2),
(19, 'tabef', 4, 1125.28),
(20, 'aoxi', 7, 280),
(20, 'apera', 5, 3245),
(20, 'asbay', 4, 609.68),
(20, 'cdeco', 9, 1118.61),
(20, 'deli', 4, 1125.24),
(20, 'julim', 3, 1580.49),
(20, 'tabef', 2, 562.64);

-- --------------------------------------------------------

--
-- Table structure for table `producto`
--

CREATE TABLE `producto` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(90) NOT NULL,
  `precio` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `producto`
--

INSERT INTO `producto` (`codigo`, `nombre`, `descripcion`, `precio`) VALUES
('adol', 'Atún en agua', 'Atún en Agua Dolores 8 pzas de 140 g c/u', 158.56),
('aetil', 'Alcohol Etílico', 'Alcohol Etílico Zuum con Dosificador 2 pzas con 420 ml', 72.52),
('aliga', 'Alimento para gato', 'Alimento para Gato Whiskas Sabor Carne 10 kg', 506.38),
('amzu', 'Azúcar morena Zulka', 'Azúcar morena Zulka 4 kg', 102.3),
('anem', 'Agua natural', 'Agua Natural Bonafont 12 pzas de 1.2 L', 101.27),
('aoxi', 'Agua ixigenada', 'Agua Oxigenada Dermocleen 2 pzas de 960 ml', 40),
('apera', 'Alimento para perro ', 'Alimento Seco para Perro Purina Mainstay Adultos 24 kg', 649),
('arega', 'Arena para gatos', 'Arena para Gatos Fresh Step con 4 pzas de 4.98 Kg', 612.76),
('asbay', 'Aspirina ', 'Aspirina Bayer 3 Cajas de 40 Tabletas c/u', 152.42),
('aveh', 'Avena en hojuelas', 'Avena Member\'s Mark Old Fashioned 4 kg', 117.64),
('avv', 'Arroz Verde Valle', 'Arroz Blanco Verde Valle Súper Extra 5 pzas de 1 kg', 166.75),
('bbasu', 'Bolsas para Basura', 'Bolsas para Basura Costalitos Grandes 72 x 76 cm 200 pzas', 380.03),
('bdes', 'Bicarbonato de sodio', 'Bicarbonato de Sodio Puro Racel 1 kg', 70.57),
('bosur', 'Boligrafos surtidos', 'Bolígrafos Bic Cristal Mediano + Ultrafino Tintas Surtidas 73 pzas', 247.57),
('caso', 'Café soluble', 'Nescafé Clásico Café Soluble de 1.2 kg', 699),
('cdeco', 'Cepillo dental', 'Cepillo Dental Colgate Premier Clean 6 pzas', 124.29),
('cloma', 'Cloralex Mascotas', 'Limpiador Desinfectante Cloralex Mascotas 10 lt', 214.82),
('cpaya', 'Contenedores para Ag', 'kit de Contenedores para Agua y Alimento Fancy Pets 2 pzas', 438.86),
('cupro', 'Cuaderno profesional', 'Cuaderno Profesional Ferrini 120 Hojas 56 Grs 6 Pzas Doble Argolla Unicolor (Raya)', 298),
('deant', 'Desinfectante en aer', 'Desinfectante Antibacterial en Aerosol Lysol para Superficies 3 pzas de 354 g', 291.54),
('deli', 'Detergente líquido p', 'Detergente líquido Mas Color 10Lt', 281.31),
('felav', 'Fibra esponja lavatr', 'Fibra Scotch Brite Esponja 10 pzas', 231.18),
('gobo', 'Goma de borrar', 'Pelikan Goma De Borrar Strike con 40 Piezas', 258),
('hocar', 'Hojas tamaño carta', 'Hojas de Papel Xerox Carta 97% Blancura 10 paq con 500 pzas c/u', 814.31),
('hter', 'Harina de trigo El R', 'Harina de Trigo El Rosal 10 pzas de 1 kg c/u', 207.66),
('jdeto', 'Jabón de tocador', 'Jabón en Barra Palmolive Naturals Lavanda y Crema 8 pzas de 120 g', 157.52),
('jugeo', 'Juego de geometría', 'THJOPOKEEL Juego de 5 piezas de geometría de metal', 129),
('julim', 'Juego de Limpieza ', 'Juego de Limpieza Lordon con Cubeta y Trapeador', 526.83),
('kitar', 'Kit Aromatizantes', 'Kit Aromatizantes de Ambiente Glade SC Johnson Difusor + 3 Repuestos de 270 ml c/u', 380.02),
('ladhe', 'Lápiz Adhesivo ', 'Lápiz Adhesivo Pritt Original 8 pzas de 11 g c/u', 126.84),
('lapam', 'Lápices', 'Paper Mate 1734378 Lápiz Mirado Triangular #2 1/2, Caja de 36, amarillo', 179.89),
('mabe', 'Miel de abeja', 'Miel de abeja San Ignacio Liquida Multifloral Cubeta (5 kg)', 899),
('matin', 'Mata insectos', 'Raid Casa & Jardin 3 pzas de 430 ml c/u', 209.69),
('paphi', 'Papel Higiénico', 'Papel Higiénico Kleenex Mega Jumbo 48 Rollos de 500 Hojas c/u', 371.46),
('pdeco', 'Pasta dental', 'Pasta Dental Colgate Máxima Protección Anticaries 6 pzas de 100 ml c/u', 249.6),
('peta4', 'Pañales etapa 4', 'Pañales Huggies Supreme Protección Delicada Etapa 4 con 90 pzas', 506.38),
('plama', 'Platos para Mascotas', 'Platos para Mascotas Member\'s Mark Acero Inoxidable Gris 2 pzas', 510.46),
('sadem', 'Sal de mesa', 'Sal de Mesa La Fina Yodada 3 pzas de 1 kg', 66.49),
('sakid', 'Sacapuntas', 'KIDMEN Sacapuntas manual, 2 agujeros, compacto, con tapa, paquete de 12', 143.88),
('shape', 'Shampoo para Perro ', 'Shampoo para Perro Dog-O-Chew con Avena 10 lt', 592.28),
('sprov', 'Shampoo', 'Shampoo Pantene Pro-V Control Caída 1 L', 168.78),
('subbi', 'Subsalicilato de Bis', 'Tabletas Masticables Pepto Bismol Subsalicilato de Bismuto Sabor Original 100 pzas', 377.48),
('tabef', 'Tabletas Efervescent', 'Tabletas Efervescentes Alka-Seltzer 100 pzas', 281.32),
('thum', 'Toallitas Húmedas ', 'Toallitas Húmedas Huggies 6 Paquetes con 80 pzas c/u', 189.26),
('vblac', 'Vinagre blanco', 'La Costeña Vinagre Blanco de Alcohol de Caña 3.8 L', 99);

-- --------------------------------------------------------

--
-- Table structure for table `rep_vtas`
--

CREATE TABLE `rep_vtas` (
  `num` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `primerApell` varchar(30) NOT NULL,
  `segApell` varchar(30) DEFAULT NULL,
  `fechaContrato` date NOT NULL,
  `director` int(11) DEFAULT NULL,
  `sucursal` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rep_vtas`
--

INSERT INTO `rep_vtas` (`num`, `nombre`, `primerApell`, `segApell`, `fechaContrato`, `director`, `sucursal`) VALUES
(1, 'David Alejandro', 'Zepeda', 'Urias', '2020-01-15', NULL, 'RESDL'),
(2, 'Fernando', 'Uriarte', 'Sosa', '2020-01-23', NULL, 'QUICA'),
(3, 'Carlos', 'Salgado', 'Ortegón', '2020-05-03', 2, 'QUICA'),
(4, 'Eduardo', 'Martínez', 'López', '2020-09-01', 1, 'RESDL'),
(5, 'Alejandra', 'Jara', 'Granados', '2020-12-10', NULL, 'BAHIA'),
(6, 'Diana Angeles', 'García', 'Cruz', '2021-02-15', NULL, 'DIMIR'),
(7, 'Abel', 'Chino', 'Chávez', '2021-04-30', 1, 'RESDL'),
(8, 'Humberto', 'López', 'Avalos', '2021-08-25', NULL, 'PABEN'),
(9, 'Daniela Esmeralda', 'García', 'Salcido', '2021-08-25', 6, 'DIMIR'),
(10, 'Rubén', 'Acedo', 'López', '2022-08-25', NULL, 'CACHA'),
(11, 'José Francisco Franklin', 'Chavarría', 'Mendoza', '2022-10-02', 6, 'DIMIR'),
(12, 'Alexis', 'Olvera', 'Zavala', '2022-10-27', 5, 'BAHIA'),
(13, 'Israel', 'Chan', 'Posadas', '2022-12-05', 6, 'DIMIR'),
(14, 'Jesús Antonio', 'Nava', 'Aguirre', '2023-02-06', 6, 'DIMIR'),
(15, 'Jose Luis', 'Vazquez', 'Gomez', '2023-02-07', 5, 'BAHIA'),
(16, 'Maria Isabel', 'Morales', 'Vazquez', '2023-05-08', 8, 'PABEN'),
(17, 'Ana Patricia', 'Vazquez', 'Mendoza', '2023-08-05', 5, 'BAHIA'),
(18, 'Alberto', 'Hernández', 'Vázquez', '2023-12-05', 2, 'QUICA'),
(19, 'Jorge', 'Espinoza', 'Guzmán', '2024-12-29', NULL, 'STAFE'),
(20, 'Ismael', 'Reyes', 'Ramos', '2024-03-08', NULL, 'STALU'),
(21, 'Luis Manuel', 'Piña', 'Ramírez', '2024-06-12', NULL, 'CETRO'),
(22, 'Carolina', 'Cervantes', 'Rivera', '2024-07-05', NULL, 'PLCIO'),
(23, 'Liliana', 'Ramos', 'Cárdenas', '2024-11-16', NULL, 'LPINS'),
(24, 'Pedro', 'Martinez', 'Gonzalez', '2025-03-06', 10, 'CACHA'),
(25, 'Alonso', 'Tamayo', 'Alborez', '2025-03-17', 8, 'PABEN'),
(26, 'Cecilia', 'Lopez', 'Leon', '2025-07-07', 10, 'CACHA');

-- --------------------------------------------------------

--
-- Table structure for table `sucursal`
--

CREATE TABLE `sucursal` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `dirCalle` varchar(30) NOT NULL,
  `dirNum` varchar(10) NOT NULL,
  `dirColonia` varchar(30) NOT NULL,
  `ciudad` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sucursal`
--

INSERT INTO `sucursal` (`codigo`, `nombre`, `dirCalle`, `dirNum`, `dirColonia`, `ciudad`) VALUES
('BAHIA', 'Bahía', 'Av. Reforma', '124 int 4', 'Reforma', 'ENS'),
('CACHA', 'Cachanilla', 'Blvd. López Mateos', '218', 'Industrial', 'MEX'),
('CETRO', 'Centro', 'Av. Ruíz', '328', 'Centro', 'MEX'),
('DIMIR', 'Díaz Mirón', 'Calle 4ta', '8050', 'Centro', 'TIJ'),
('LPINS', 'Los Pinos', 'Blvd. Díaz Ordaz', '303', 'Los Pinos', 'TIJ'),
('PABEN', 'Pabellón', 'Tijuana-Rosarito', '300', 'Parcelas', 'TIJ'),
('PLCIO', 'Palacio', 'Av. López Mateos', '1504 int 1', 'Zona Centro', 'ENS'),
('QUICA', 'Quintas campestre', 'Blvd. Real de Baja California', '23911', 'San Francisco', 'TIJ'),
('RESDL', 'Residencial', 'Blvd. Anahuac', '1301', 'Fracc. Villa Residencial', 'MEX'),
('STAFE', 'Santa Fe', 'Oriente', '7002 int 8', 'Santa Fe', 'TIJ'),
('STALU', 'Santa Lucía', 'Carr. Transpeninsular', '135', 'Santa Lucía', 'ROS');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `almacen`
--
ALTER TABLE `almacen`
  ADD PRIMARY KEY (`sucursal`,`producto`),
  ADD KEY `producto` (`producto`);

--
-- Indexes for table `ciudad`
--
ALTER TABLE `ciudad`
  ADD PRIMARY KEY (`codigo`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`num`);

--
-- Indexes for table `concepto_pago`
--
ALTER TABLE `concepto_pago`
  ADD PRIMARY KEY (`codigo`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indexes for table `edo_pedido`
--
ALTER TABLE `edo_pedido`
  ADD PRIMARY KEY (`codigo`),
  ADD UNIQUE KEY `descripcion` (`descripcion`);

--
-- Indexes for table `meta`
--
ALTER TABLE `meta`
  ADD PRIMARY KEY (`num`),
  ADD KEY `sucursal` (`sucursal`),
  ADD KEY `repVtas` (`repVtas`);

--
-- Indexes for table `pago`
--
ALTER TABLE `pago`
  ADD PRIMARY KEY (`numero`),
  ADD KEY `concepto` (`concepto`),
  ADD KEY `pedido` (`pedido`);

--
-- Indexes for table `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`num`),
  ADD KEY `sucursal` (`sucursal`),
  ADD KEY `rep_vtas` (`rep_vtas`),
  ADD KEY `cliente` (`cliente`),
  ADD KEY `estado` (`estado`);

--
-- Indexes for table `ped_prod`
--
ALTER TABLE `ped_prod`
  ADD PRIMARY KEY (`pedido`,`producto`),
  ADD KEY `producto` (`producto`);

--
-- Indexes for table `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`codigo`);

--
-- Indexes for table `rep_vtas`
--
ALTER TABLE `rep_vtas`
  ADD PRIMARY KEY (`num`),
  ADD KEY `sucursal` (`sucursal`),
  ADD KEY `FK_rv_director` (`director`);

--
-- Indexes for table `sucursal`
--
ALTER TABLE `sucursal`
  ADD PRIMARY KEY (`codigo`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `ciudad` (`ciudad`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cliente`
--
ALTER TABLE `cliente`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `meta`
--
ALTER TABLE `meta`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `pago`
--
ALTER TABLE `pago`
  MODIFY `numero` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pedido`
--
ALTER TABLE `pedido`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `rep_vtas`
--
ALTER TABLE `rep_vtas`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `almacen`
--
ALTER TABLE `almacen`
  ADD CONSTRAINT `almacen_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`),
  ADD CONSTRAINT `almacen_ibfk_2` FOREIGN KEY (`producto`) REFERENCES `producto` (`codigo`);

--
-- Constraints for table `meta`
--
ALTER TABLE `meta`
  ADD CONSTRAINT `meta_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`),
  ADD CONSTRAINT `meta_ibfk_2` FOREIGN KEY (`repVtas`) REFERENCES `rep_vtas` (`num`);

--
-- Constraints for table `pago`
--
ALTER TABLE `pago`
  ADD CONSTRAINT `pago_ibfk_1` FOREIGN KEY (`concepto`) REFERENCES `concepto_pago` (`codigo`),
  ADD CONSTRAINT `pago_ibfk_2` FOREIGN KEY (`pedido`) REFERENCES `pedido` (`num`);

--
-- Constraints for table `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`),
  ADD CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`rep_vtas`) REFERENCES `rep_vtas` (`num`),
  ADD CONSTRAINT `pedido_ibfk_3` FOREIGN KEY (`cliente`) REFERENCES `cliente` (`num`),
  ADD CONSTRAINT `pedido_ibfk_4` FOREIGN KEY (`estado`) REFERENCES `edo_pedido` (`codigo`);

--
-- Constraints for table `ped_prod`
--
ALTER TABLE `ped_prod`
  ADD CONSTRAINT `ped_prod_ibfk_1` FOREIGN KEY (`pedido`) REFERENCES `pedido` (`num`),
  ADD CONSTRAINT `ped_prod_ibfk_2` FOREIGN KEY (`producto`) REFERENCES `producto` (`codigo`);

--
-- Constraints for table `rep_vtas`
--
ALTER TABLE `rep_vtas`
  ADD CONSTRAINT `FK_rv_director` FOREIGN KEY (`director`) REFERENCES `rep_vtas` (`num`),
  ADD CONSTRAINT `rep_vtas_ibfk_1` FOREIGN KEY (`sucursal`) REFERENCES `sucursal` (`codigo`);

--
-- Constraints for table `sucursal`
--
ALTER TABLE `sucursal`
  ADD CONSTRAINT `sucursal_ibfk_1` FOREIGN KEY (`ciudad`) REFERENCES `ciudad` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

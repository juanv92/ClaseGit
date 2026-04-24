-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-03-2026 a las 21:16:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `la_colmenita`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL,
  `nombre_categoria` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `nombre_categoria`) VALUES
(1, 'Herramientas manuales'),
(2, 'Herramientas electricas'),
(3, 'Medicion'),
(4, 'Accesorios de perforacion'),
(5, 'Tornilleria y fijaciones');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre_producto` varchar(100) DEFAULT NULL,
  `descrip_producto` varchar(100) DEFAULT NULL,
  `marca` varchar(100) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre_producto`, `descrip_producto`, `marca`, `id_categoria`) VALUES
(1, 'Martillo de carpintero', 'Martillo de cabeza de acero', 'Stanley', 1),
(2, 'Llave inglesa ajustable', 'Llave ajustable para tuercas', 'Truper', 1),
(3, 'Taladro inal?mbrico', 'Taladro a bater?a 18V', 'Bosch', 2),
(4, 'Sierra circular el?ctrica', 'Sierra para cortes precisos', 'Makita', 2),
(5, 'Calibrador digital', 'Medidor digital de precisi?n', 'Mitutoyo', 3),
(6, 'Mult?metro digital', 'Medidor el?ctrico y voltaje', 'Fluke', 3),
(7, 'Broca para metal', 'Broca de acero para perforar', 'Dewalt', 4),
(8, 'Disco de corte', 'Disco para amoladora', 'Bosch', 4),
(9, 'Tornillo autorroscante', 'Tornillo para madera de 3cm', 'Grip-Rite', 5),
(10, 'Juego de fijaciones mixtas', 'Kit de tornillos y clavos', 'Fischer', 5);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_categoria` (`id_categoria`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

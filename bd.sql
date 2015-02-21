-- phpMyAdmin SQL Dump
-- http://www.phpmyadmin.net
--
-- Servidor: 127.5.119.2:3306
-- Tiempo de generación: 21-02-2015 a las 09:59:31
-- Versión del servidor: 5.5.41
-- Versión de PHP: 5.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `prometheusinwatch`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `log`
--

CREATE TABLE IF NOT EXISTS `log` (
  `id` float NOT NULL,
  `user` float NOT NULL,
  `is_ok` tinyint(1) NOT NULL,
  `day` date NOT NULL,
  `smokedCigars` int(11) NOT NULL,
  `savedMoney` float NOT NULL,
  `unsmokedCigars` int(11) NOT NULL,
  `savedTime` float NOT NULL,
  PRIMARY KEY (`id`,`user`),
  KEY `usuario` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tips`
--

CREATE TABLE IF NOT EXISTS `tips` (
  `id` int(11) NOT NULL,
  `text` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` float NOT NULL,
  `email` varchar(100) NOT NULL,
  `cigarsPerDay` int(11) NOT NULL,
  `cigarsPerPacket` int(11) NOT NULL,
  `pricePerPacket` float NOT NULL,
  `stopSmokingDate` date NOT NULL,
  `totalUnsmokedCigars` int(11) NOT NULL,
  `totalMoneySaved` float NOT NULL,
  `totalTimeSaved` float NOT NULL,
  `totalDaysClean` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `log`
--
ALTER TABLE `log`
  ADD CONSTRAINT `usuario` FOREIGN KEY (`user`) REFERENCES `user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

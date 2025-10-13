-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2025 at 06:20 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vegecommerce`
--

-- --------------------------------------------------------

--
-- Table structure for table `buyerregister`
--

CREATE TABLE `buyerregister` (
  `name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `area` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `contact_number` varchar(15) NOT NULL,
  `address` varchar(20) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buyerregister`
--

INSERT INTO `buyerregister` (`name`, `gender`, `area`, `district`, `contact_number`, `address`, `image_path`, `password`) VALUES
('kamala kannan', 'Male', 'Downtown', 'District 1', '6379007560', 'trichy', 'uploads/user.jpg', '1234'),
('abdul', 'Male', 'Downtown', 'District 1', '9012345678', 'trichy', 'static/uploads/user.jpg', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `price` varchar(10) NOT NULL,
  `image_path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_name` varchar(100) DEFAULT NULL,
  `seller_name` varchar(100) DEFAULT NULL,
  `shop_name` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `image_path` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_name`, `seller_name`, `shop_name`, `price`, `image_path`) VALUES
('tomato', 'kannan', 'kannan shop', '24', 'static/uploads/tomato.jpg'),
('Apple', 'kiruthika', 'kiruthika super market', '25', 'static/uploads/apple.jpg'),
('spinach', 'rahul', 'rahul shop', '10', 'static/uploads/spinach.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `sellerregister`
--

CREATE TABLE `sellerregister` (
  `name` varchar(100) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `area` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `contact_number` varchar(15) NOT NULL,
  `address` varchar(50) NOT NULL,
  `shop_name` varchar(100) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `password` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sellerregister`
--

INSERT INTO `sellerregister` (`name`, `gender`, `area`, `district`, `contact_number`, `address`, `shop_name`, `image_path`, `password`) VALUES
('kamala kannan', 'Male', 'Chatram', 'Trichy', '6379007560', 'trichy', 'krish infotech', 'static/uploads/user.jpg', '1234'),
('kiruthika', 'Female', 'Uraiyur', 'Trichy', '9876543210', 'trichy', 'kiruthika super market', 'static/uploads/women.jpg', '1234'),
('Rahul', 'Male', 'KK Nagar', 'Perambalur', '9877965451', 'permbalur', 'rahul shop', 'static/uploads/user.jpg', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buyerregister`
--
ALTER TABLE `buyerregister`
  ADD UNIQUE KEY `contact_number` (`contact_number`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sellerregister`
--
ALTER TABLE `sellerregister`
  ADD UNIQUE KEY `contact_number` (`contact_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

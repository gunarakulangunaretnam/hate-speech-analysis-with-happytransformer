-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 15, 2022 at 09:57 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `without_knowledgebase_hate_speech_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `processed_data`
--

CREATE TABLE `processed_data` (
  `auto_id` int(200) NOT NULL,
  `target_data` mediumtext NOT NULL,
  `analyzed_date` date NOT NULL,
  `analyzed_time` varchar(100) NOT NULL,
  `result` varchar(100) NOT NULL,
  `probability_score` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `processed_data`
--

INSERT INTO `processed_data` (`auto_id`, `target_data`, `analyzed_date`, `analyzed_time`, `result`, `probability_score`) VALUES
(226, 'I hate u i like u', '2022-03-15', '01:51:06 PM', 'HATE', '62.041181325912476');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `processed_data`
--
ALTER TABLE `processed_data`
  ADD PRIMARY KEY (`auto_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `processed_data`
--
ALTER TABLE `processed_data`
  MODIFY `auto_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=227;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

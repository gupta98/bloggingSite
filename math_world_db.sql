-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2022 at 06:33 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `math_world_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

CREATE TABLE `authors` (
  `AID` int(11) NOT NULL,
  `NAME` text NOT NULL,
  `EMAIL` text NOT NULL,
  `PHONE` varchar(10) NOT NULL,
  `USERNAME` text NOT NULL,
  `PASSWORD` text NOT NULL,
  `DESCRIPTION` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`AID`, `NAME`, `EMAIL`, `PHONE`, `USERNAME`, `PASSWORD`, `DESCRIPTION`) VALUES
(1, 'Admin', 'admin@gmail.com', 'admin', 'Admin', 'admin', NULL),
(2, 'Debtanu Gupta', 'dg@g', '7980060644', 'debtanugupta', '1234', NULL),
(3, 'Gebtanu Dupta', 'gd@g', '4781236872', 'gebtanuDupta', '1234', NULL),
(4, 'Ajitava Sarkar', 'as@g', '7980060644', 'sishu', '1234', NULL),
(5, 'Prasun Jyoti Debnath', 'pjd@g', '4781236872', 'rosun', '1234', NULL),
(6, 'GSN', 'gsn@g', '4764379381', 'gsn', '1234', NULL),
(9, 'GSN3', 'gsn3@g', '4764379381', 'gsn3', '1234', NULL),
(10, 'GSN4', 'gsn4@g', '4764379381', 'gsn4', '1234', NULL),
(11, 'GSN10', 'gsn10@g', '4764379381', 'gsn10', '1234', NULL),
(15, 'GSN2', 'gsn2@g', '4764379381', 'gsn2', '1234', 'Ore majhi mera sajan hain uspar!');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `CID` int(20) NOT NULL,
  `NAME` text NOT NULL,
  `EMAIL` text NOT NULL,
  `PHONE` text DEFAULT NULL,
  `MESSAGE` text NOT NULL,
  `DATE` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`CID`, `NAME`, `EMAIL`, `PHONE`, `MESSAGE`, `DATE`) VALUES
(1, '[value-2]', '[value-3]', '[value-4]', '[value-5]', '2022-09-14 15:41:46'),
(2, '1', '2@2', '2', 'asdasd', '2022-09-14 16:14:10'),
(3, 'Debtanu Gupta', 'debtanu1998gupta3@gmail.com', '7980060644', 'খুব ভালো সাইট। কিন্তু আরও ভালো করতে হবে।', '2022-09-14 18:46:23'),
(4, 'Debtanu Gupta', 'debtanu1998gupta3@gmail.com', '7980060644', 'খুব ভালো সাইট। কিন্তু আরও ভালো করতে হবে।', '2022-09-14 18:48:16');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `PID` int(20) UNSIGNED NOT NULL,
  `TITLE` text NOT NULL,
  `FIRST30LETTERS` varchar(30) NOT NULL,
  `SLUG` text NOT NULL,
  `IMAGEURL` text NOT NULL DEFAULT 'default.jpg',
  `AID` int(11) NOT NULL,
  `DATE` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`PID`, `TITLE`, `FIRST30LETTERS`, `SLUG`, `IMAGEURL`, `AID`, `DATE`) VALUES
(2, 'What is pi?', 'pi is a great constant and it', 'What-is-pi', 'default.jpg', 2, '2022-09-15 15:58:12'),
(3, 'Leonhard Euler', 'Leonhard Euler (15 April 1707 ', 'Leonhard-Euler', 'default.jpg', 1, '2022-09-15 22:50:35'),
(4, 'অক্ষৌহিণী', 'প্রাচীন ভারতীয় রাজ্যসমূহে বা হ', 'অক্ষৌহিণী', '4.jpg', 3, '2022-09-15 22:55:30'),
(14, 'asd  etruy 4  i6 wd sdf 3e', 's f awe y567 4 3q2 v125df g we', 'asd--etruy-4--i6-wd-sdf-3e', 'default.jpg', 9, '2022-09-19 11:49:47'),
(15, 'KALYANAM VAIVOGAM', 'ANANDARAGALA SHUBHAYOGAM', 'KALYANAM-VAIVOGAM', 'KALYANAM-VAIVOGAM.jpg', 9, '2022-09-19 11:51:31'),
(16, 'This is testing post!! Are you excited?', 'My blog is my blog. None\r\nOf y', 'This-is-testing-post-Are-you-excited', 'This-is-testing-post-Are-you-excited.jpg', 15, '2022-09-19 19:36:02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`AID`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`CID`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`PID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authors`
--
ALTER TABLE `authors`
  MODIFY `AID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `CID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `PID` int(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

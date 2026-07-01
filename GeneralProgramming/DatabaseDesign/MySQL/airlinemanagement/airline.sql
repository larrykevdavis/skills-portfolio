-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2024 at 04:29 PM
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
-- Database: `airline`
--

-- --------------------------------------------------------

--
-- Table structure for table `aircraft`
--

CREATE TABLE `aircraft` (
  `aircraft_id` int(11) NOT NULL,
  `airline_id` int(11) NOT NULL,
  `aircraft_name` varchar(1000) NOT NULL,
  `first_class_capacity` int(11) NOT NULL,
  `business_class_capacity` int(11) NOT NULL,
  `economy_class_capacity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aircraft`
--

INSERT INTO `aircraft` (`aircraft_id`, `airline_id`, `aircraft_name`, `first_class_capacity`, `business_class_capacity`, `economy_class_capacity`) VALUES
(3, 1, 'Boeing 748', 11, 12, 30);

-- --------------------------------------------------------

--
-- Table structure for table `airlines`
--

CREATE TABLE `airlines` (
  `airline_id` int(11) NOT NULL,
  `airline_name` varchar(1000) NOT NULL,
  `country_of_origin` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airlines`
--

INSERT INTO `airlines` (`airline_id`, `airline_name`, `country_of_origin`) VALUES
(1, 'Turkish Airlines', 'Turkiye');

-- --------------------------------------------------------

--
-- Table structure for table `airport_worker`
--

CREATE TABLE `airport_worker` (
  `worker_id` int(11) NOT NULL,
  `worker_name` varchar(1000) NOT NULL,
  `worker_email` varchar(1000) NOT NULL,
  `worker_phonenumber` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airport_worker`
--

INSERT INTO `airport_worker` (`worker_id`, `worker_name`, `worker_email`, `worker_phonenumber`) VALUES
(3400, 'Kylin Kon', 'kk@m.com', 12343546);

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `booking_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `flight_id` int(11) NOT NULL,
  `class` varchar(1000) NOT NULL,
  `traveller_type` varchar(1000) NOT NULL,
  `rating` int(11) NOT NULL,
  `review_title` varchar(1000) NOT NULL,
  `review` varchar(2000) NOT NULL,
  `value_for_money` int(11) NOT NULL,
  `recommended` int(11) NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT 'booked'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

CREATE TABLE `flights` (
  `flight_id` int(11) NOT NULL,
  `aircraft_id` int(11) NOT NULL,
  `route_id` int(11) NOT NULL,
  `flight_date` date NOT NULL,
  `flight_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`flight_id`, `aircraft_id`, `route_id`, `flight_date`, `flight_time`) VALUES
(2, 3, 1, '2024-05-07', '09:40:20');

-- --------------------------------------------------------

--
-- Table structure for table `routes`
--

CREATE TABLE `routes` (
  `route_id` int(11) NOT NULL,
  `route_name` varchar(1000) NOT NULL,
  `route_type` varchar(1000) NOT NULL,
  `route_source` varchar(1000) NOT NULL,
  `route_destination` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `routes`
--

INSERT INTO `routes` (`route_id`, `route_name`, `route_type`, `route_source`, `route_destination`) VALUES
(1, 'Birmingham to Newcastle', 'domestic', 'Birmingham', 'Newcastle');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL,
  `staff_name` varchar(1000) NOT NULL,
  `staff_age` int(11) NOT NULL,
  `staff_location` varchar(1000) NOT NULL,
  `staff_email` varchar(1000) NOT NULL,
  `staff_phonenumber` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `staff_name`, `staff_age`, `staff_location`, `staff_email`, `staff_phonenumber`) VALUES
(1090, 'Johnstone Cargally', 30, 'Brisbanee', 'jcar@newcastle.com', '2877661991'),
(1095, 'John Kim', 32, 'mei', 'jk@g.com', '123244'),
(1098, '11', 11, '11', '11', '111233'),
(1099, '11', 11, '11', '11', '111233'),
(1100, 'ff', 11, '11', 'ff', '1111'),
(1101, 'f1', 111, '1', '1', '1223'),
(1103, 'ff', 111, '11', '11', '111233');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `student_name` varchar(1000) NOT NULL,
  `student_email` varchar(1000) NOT NULL,
  `student_age` int(11) NOT NULL,
  `student_phonenumber` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `student_name`, `student_email`, `student_age`, `student_phonenumber`) VALUES
(2100, 'John Cam', 'm@gmai.com', 111, '111233');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(1000) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `category` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `category`) VALUES
(1090, 'teststaff@emp.com', '1234', 'staff'),
(1091, 'testadmin@emp.com', '1234', 'admin'),
(1092, 'testworker@emp.com', '1234', 'worker');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aircraft`
--
ALTER TABLE `aircraft`
  ADD PRIMARY KEY (`aircraft_id`),
  ADD KEY `aircrafttoairline` (`airline_id`);

--
-- Indexes for table `airlines`
--
ALTER TABLE `airlines`
  ADD PRIMARY KEY (`airline_id`);

--
-- Indexes for table `airport_worker`
--
ALTER TABLE `airport_worker`
  ADD PRIMARY KEY (`worker_id`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `bookingstouser` (`user_id`),
  ADD KEY `bookingstoflight` (`flight_id`);

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`flight_id`),
  ADD KEY `flightstoaircraft` (`aircraft_id`),
  ADD KEY `flightstoroute` (`route_id`);

--
-- Indexes for table `routes`
--
ALTER TABLE `routes`
  ADD PRIMARY KEY (`route_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aircraft`
--
ALTER TABLE `aircraft`
  MODIFY `aircraft_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `airlines`
--
ALTER TABLE `airlines`
  MODIFY `airline_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `flights`
--
ALTER TABLE `flights`
  MODIFY `flight_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `routes`
--
ALTER TABLE `routes`
  MODIFY `route_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `aircraft`
--
ALTER TABLE `aircraft`
  ADD CONSTRAINT `aircrafttoairline` FOREIGN KEY (`airline_id`) REFERENCES `airlines` (`airline_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `bookings`
--
ALTER TABLE `bookings`
  ADD CONSTRAINT `bookingstoflight` FOREIGN KEY (`flight_id`) REFERENCES `flights` (`flight_id`),
  ADD CONSTRAINT `bookingstouser` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `flights`
--
ALTER TABLE `flights`
  ADD CONSTRAINT `flightstoaircraft` FOREIGN KEY (`aircraft_id`) REFERENCES `aircraft` (`aircraft_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `flightstoroute` FOREIGN KEY (`route_id`) REFERENCES `routes` (`route_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

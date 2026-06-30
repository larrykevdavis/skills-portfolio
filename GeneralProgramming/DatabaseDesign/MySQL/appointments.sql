-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2024 at 12:35 PM
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
-- Database: `appointments`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `status` varchar(1000) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`appointment_id`, `date`, `time`, `status`, `patient_id`, `employee_id`) VALUES
(6, '2024-05-23', '11:23:00', 'active', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `diagnosis`
--

CREATE TABLE `diagnosis` (
  `diagnosis_id` int(11) NOT NULL,
  `appointment_id` int(11) NOT NULL,
  `diagnosis` varchar(1000) NOT NULL,
  `prescription` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL,
  `employee_name` varchar(1000) NOT NULL,
  `employee_category` varchar(1000) NOT NULL,
  `employee_age` varchar(1000) NOT NULL,
  `employee_email` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `employee_name`, `employee_category`, `employee_age`, `employee_email`) VALUES
(1, 'John Kim', 'doctor', '30', 'admin@admin.com');

-- --------------------------------------------------------

--
-- Table structure for table `heart_clinical_tests`
--

CREATE TABLE `heart_clinical_tests` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `chest_pain_type` varchar(1000) NOT NULL,
  `resting_blood_pressure` int(11) NOT NULL,
  `serum_cholestrol` int(11) NOT NULL,
  `fasting_blood_sugar` varchar(255) NOT NULL,
  `resting_electrocardiographic_results` varchar(255) NOT NULL,
  `max_heart_rate` int(11) NOT NULL,
  `exercise_induced_angina` varchar(255) NOT NULL,
  `st_depression_induced_by_exercise` int(11) NOT NULL,
  `st_segment_slope` varchar(255) NOT NULL,
  `colored_major_vessels` int(11) NOT NULL,
  `thalassemia` varchar(255) NOT NULL,
  `presence` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `heart_clinical_tests`
--

INSERT INTO `heart_clinical_tests` (`id`, `user_id`, `chest_pain_type`, `resting_blood_pressure`, `serum_cholestrol`, `fasting_blood_sugar`, `resting_electrocardiographic_results`, `max_heart_rate`, `exercise_induced_angina`, `st_depression_induced_by_exercise`, `st_segment_slope`, `colored_major_vessels`, `thalassemia`, `presence`) VALUES
(1, 1, 'typical angina', 145, 233, 'TRUE', 'lv hypertrophy', 150, 'FALSE', 2, 'downsloping', 0, 'fixed defect', 0);

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `user_id` int(11) NOT NULL,
  `message_content` varchar(1000) NOT NULL,
  `status` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `patient_id` int(11) NOT NULL,
  `patient_name` varchar(1000) NOT NULL,
  `patient_age` varchar(1000) NOT NULL,
  `patient_gender` varchar(1000) NOT NULL,
  `patient_location` varchar(1000) NOT NULL,
  `patient_email` varchar(1000) NOT NULL,
  `info_sharing` int(11) NOT NULL DEFAULT 0,
  `tests_sharing` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patient_id`, `patient_name`, `patient_age`, `patient_gender`, `patient_location`, `patient_email`, `info_sharing`, `tests_sharing`) VALUES
(1, '1 1', '1', 'male', '1', '1', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `category` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `email`, `password`, `category`) VALUES
(1, 'patient@patient.com', '1234', 'patient'),
(11, 'admin@admin.com', '1234', 'admin'),
(12, 'test@lab.com', '1234', 'lab');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`appointment_id`);

--
-- Indexes for table `diagnosis`
--
ALTER TABLE `diagnosis`
  ADD PRIMARY KEY (`diagnosis_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employee_id`);

--
-- Indexes for table `heart_clinical_tests`
--
ALTER TABLE `heart_clinical_tests`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`patient_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `appointment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `diagnosis`
--
ALTER TABLE `diagnosis`
  MODIFY `diagnosis_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `heart_clinical_tests`
--
ALTER TABLE `heart_clinical_tests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `patient_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

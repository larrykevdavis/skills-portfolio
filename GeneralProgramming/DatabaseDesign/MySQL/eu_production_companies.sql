-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2023 at 02:43 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eu_production_companies`
--

-- --------------------------------------------------------

--
-- Table structure for table `application`
--

CREATE TABLE `application` (
  `application_id` int(11) NOT NULL,
  `grant_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `application_date` date NOT NULL,
  `desired_amount` double NOT NULL,
  `outcome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `application`
--

INSERT INTO `application` (`application_id`, `grant_id`, `company_id`, `application_date`, `desired_amount`, `outcome`) VALUES
(2, 1, 1, '2023-12-05', 38777, '');

-- --------------------------------------------------------

--
-- Table structure for table `compensation`
--

CREATE TABLE `compensation` (
  `faction_id` int(11) NOT NULL,
  `hourly_pay` double NOT NULL,
  `daily_bonus` double NOT NULL,
  `scene_bonus` double NOT NULL,
  `shooting_bonus` double NOT NULL,
  `monthly_wage` double NOT NULL,
  `working_hours` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `compensation`
--

INSERT INTO `compensation` (`faction_id`, `hourly_pay`, `daily_bonus`, `scene_bonus`, `shooting_bonus`, `monthly_wage`, `working_hours`) VALUES
(1, 0, 0, 0, 0, 15000, 6),
(2, 0, 0, 0, 0, 18000, 6),
(4, 200, 0, 0, 3000, 0, 0),
(5, 55, 0, 0, 1200, 0, 0),
(6, 50, 50, 0, 600, 0, 0),
(7, 35, 0, 0, 450, 0, 0),
(8, 30, 0, 0, 300, 0, 0),
(9, 20, 0, 0, 1000, 0, 0),
(10, 15, 0, 0, 356, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `contactinformation`
--

CREATE TABLE `contactinformation` (
  `info_id` int(11) NOT NULL,
  `employee_ID_no` int(11) NOT NULL,
  `tel_number` varchar(255) NOT NULL,
  `description` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contactinformation`
--

INSERT INTO `contactinformation` (`info_id`, `employee_ID_no`, `tel_number`, `description`) VALUES
(1, 8834, '+449577443191', 'Primary Number'),
(2, 8834, '+448063289297', 'Alternate Number'),
(3, 8835, '+445803698296', 'Primary Number'),
(4, 8835, '+448040159011', 'Alternate Number'),
(5, 8836, '+442606702225', 'Primary Number'),
(6, 8836, '+446024024960', 'Alternate Number'),
(7, 8837, '+442607079036', 'Primary Number'),
(8, 8837, '+445417226919', 'Alternate Number'),
(9, 8838, '+449049172256', 'Primary Number'),
(10, 8838, '+443360985583', 'Alternate Number'),
(11, 8839, '+448585378927', 'Primary Number'),
(12, 8839, '+448560813768', 'Alternate Number'),
(13, 8840, '+449520403460', 'Primary Number'),
(14, 8840, '+446579657489', 'Alternate Number'),
(15, 8841, '+449803848338', 'Primary Number'),
(16, 8841, '+446821344631', 'Alternate Number'),
(17, 8842, '+443307161902', 'Primary Number'),
(18, 8842, '+444698205570', 'Alternate Number'),
(19, 8843, '+443195782735', 'Primary Number'),
(20, 8843, '+444090750249', 'Alternate Number');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL,
  `dept_name` varchar(255) NOT NULL,
  `building` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`dept_id`, `dept_name`, `building`, `address`) VALUES
(2, 'Human Resource', 'HR house', '9257 Harrison Street'),
(3, 'Advertising', 'Ad Loc', '35724 5th Street North'),
(6, 'Accounting', 'House ac', '688 Main Street East'),
(7, 'Branding', 'Brand Center', '15 4th Street'),
(8, 'Budget', 'Budgetary Planet', '77 Elm Street'),
(9, 'Operations', 'Op Houaw', '2208 Grant Street'),
(10, 'Sales', 'House de sales', '966 Railroad Avenue'),
(11, 'Analysts', 'Overview cleak', '29 4th Street North'),
(12, 'Content Moderation', 'Content tower', '3610 Clinton Street'),
(13, 'Strategy Formulation', 'Tower strategies', '7270 Central Avenue'),
(14, 'Planning Management', 'Planning house', '2175 King Street'),
(15, 'Budgetary affairs', 'House of budget', '29 4th Street North'),
(16, 'Crew', 'None', 'None');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `employee_ID_no` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `faction_id` int(11) NOT NULL,
  `given_name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `email_address` varchar(255) NOT NULL,
  `commencement_date` date NOT NULL,
  `date_of_birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_ID_no`, `company_id`, `faction_id`, `given_name`, `surname`, `middle_name`, `email_address`, `commencement_date`, `date_of_birth`) VALUES
(8834, 1, 2, 'Christopher', 'Howard', 'Moore', 'christopher.a@ymail.com', '2012-12-05', '1992-12-06'),
(8835, 1, 2, 'Justin', 'Flores', 'Lewis', 'justin_flores99@yahoo.com', '2012-12-19', '1992-03-28'),
(8836, 1, 3, 'Andrew', 'Howard', 'Morgan', 'andrewchoward6@outlook.com', '2015-10-21', '1980-06-21'),
(8837, 1, 3, 'Olivia', 'Gray', 'Lewis', 'o.gray@gmail.com', '2016-09-08', '1968-08-04'),
(8838, 1, 4, 'Joshua', 'Bailey', 'Miller', 'jgbailey@hotmail.com', '2015-12-19', '1989-09-04'),
(8839, 1, 5, 'Stephanie', 'Ward', 'Davis', 'slward70@hotmail.com', '2023-01-10', '1993-03-03'),
(8840, 1, 6, 'Jeremy', 'Davis', 'Sanders', 'jeremy.davis@ymail.com', '2010-10-10', '1995-02-26'),
(8841, 1, 7, 'Alexander', 'Flores', 'Coleman', 'alexander.flores28@hotmail.com', '2020-02-03', '1997-12-16'),
(8842, 1, 8, 'Abigail', 'Torres', 'Davis', 'abigail.margaret.torres@live.com', '2022-06-06', '1999-08-26'),
(8843, 1, 9, 'Olivia', 'Gray', 'Nelson', 'ogray@aol.com', '2023-12-12', '2001-09-24'),
(9008, 3, 3, 'Elizabeth', 'Collins', 'Young', 'elizabeth.collins@hotmail.com', '2023-12-18', '1970-12-11'),
(9009, 3, 4, 'Owen', 'Rogers', 'Phillips', 'o.e@ymail.com', '2023-12-02', '1945-06-04');

-- --------------------------------------------------------

--
-- Table structure for table `faction`
--

CREATE TABLE `faction` (
  `faction_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `dept_id` int(11) NOT NULL,
  `faction_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faction`
--

INSERT INTO `faction` (`faction_id`, `group_id`, `dept_id`, `faction_name`) VALUES
(1, 1, 6, 'Accounting Manager'),
(2, 1, 2, 'HR manager'),
(3, 2, 16, 'Actor'),
(4, 2, 16, 'Director'),
(5, 2, 16, 'Producer'),
(6, 2, 16, 'Editor'),
(7, 2, 16, 'Production Designer'),
(8, 2, 16, 'Costume Designer'),
(9, 2, 16, 'Composer'),
(10, 2, 16, 'Sound Engineer');

-- --------------------------------------------------------

--
-- Table structure for table `film`
--

CREATE TABLE `film` (
  `movie_code` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `first_release_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`movie_code`, `company_id`, `title`, `year`, `first_release_date`) VALUES
(202, 1, '12 Angry Men', '2002', '0000-00-00'),
(203, 1, '13 Lakes', '2003', '2003-12-19'),
(204, 1, '42nd Street', '2004', '2004-12-03'),
(304, 9, 'Adam’s Rib', '2020', '2020-01-01');

-- --------------------------------------------------------

--
-- Table structure for table `grants`
--

CREATE TABLE `grants` (
  `grant_id` int(11) NOT NULL,
  `official_title` varchar(255) NOT NULL,
  `funding_org` varchar(255) NOT NULL,
  `max_monetary_value` double NOT NULL,
  `proposal_deadline` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `grants`
--

INSERT INTO `grants` (`grant_id`, `official_title`, `funding_org`, `max_monetary_value`, `proposal_deadline`) VALUES
(1, 'Movie of the Year', 'Cohesion Fund', 100000, '2023-12-05'),
(2, 'Creative movies', 'Creative Europe', 3746689, '2023-12-04'),
(3, 'Creativity Impact', 'European Social Fund', 900000, '2023-12-19');

-- --------------------------------------------------------

--
-- Table structure for table `personnelgroup`
--

CREATE TABLE `personnelgroup` (
  `group_id` int(11) NOT NULL,
  `group_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `personnelgroup`
--

INSERT INTO `personnelgroup` (`group_id`, `group_name`) VALUES
(1, 'Staff'),
(2, 'Crew');

-- --------------------------------------------------------

--
-- Table structure for table `productioncompany`
--

CREATE TABLE `productioncompany` (
  `company_id` int(11) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `zip_code` varchar(5) NOT NULL,
  `city` varchar(255) NOT NULL,
  `nation` varchar(255) NOT NULL,
  `org_kind` varchar(255) NOT NULL,
  `no_employees` int(11) NOT NULL,
  `total_asset_value` double NOT NULL,
  `total_liabilities_value` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `productioncompany`
--

INSERT INTO `productioncompany` (`company_id`, `company_name`, `address`, `zip_code`, `city`, `nation`, `org_kind`, `no_employees`, `total_asset_value`, `total_liabilities_value`) VALUES
(1, 'Magic Light Pictures', '293 Cedar Lane', '52590', 'San Rafael', 'United Kingdom', 'Non-profit', 200, 150000, 10000),
(2, 'Magma Pictures', '41 Buckingham Drive', '27856', 'Nashville', 'United Kingdom', 'Private Commpany', 100, 4507897, 180000),
(3, 'Mancunian Films', '52 Hilltop Road', '38366', 'Pinson', 'United Kingdom', 'Private company', 1000, 1200000, 304889),
(4, 'Films Noirs', '29 King Street', '94991', 'San Rafael', 'Germany', 'Non Profit', 478, 8977272, 112356),
(5, 'Framestore', '73 Green Street', '49783', 'Sault Sainte Marie', 'Greece', 'Public Company', 500, 123489, 122489),
(6, 'Eros Films', '339 Cambridge Drive', '95655', 'Mather', 'Hungary', 'Non profit', 1300, 2349000, 12359),
(7, 'AbbottVision', '78 Division Street', '12441', 'Highmount', 'Ireland', 'Public company', 230, 59968820, 278839),
(8, 'Glory Film Co.', '29 College Avenue', '50627', 'Little York', 'Latvia', 'Non profit', 2353, 478859, 123445),
(9, 'Bolexbrothers', '7892 High Street', '55306', 'Burnsville', 'Latvia', 'Public Company', 123, 83541676, 46655475),
(11, 'Patronage', '86 Jefferson Avenue', '5602', 'Montpelier', 'Belgium', 'Public Company', 1000, 499999, 19990);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `company_id` int(11) NOT NULL,
  `local_govt_name` varchar(255) NOT NULL,
  `registration_date` date NOT NULL,
  `registration_fee` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`company_id`, `local_govt_name`, `registration_date`, `registration_fee`) VALUES
(1, 'Companies house', '2015-08-11', 12),
(2, 'Companies house', '2012-08-11', 12),
(3, 'Companies house', '2011-07-11', 12),
(4, 'Bundesanzeiger', '2019-12-08', 30),
(5, 'Hellenic', '2019-12-11', 30),
(6, 'Hungarian court of registration', '2020-10-18', 23),
(7, 'Companies Registration Office', '2011-01-25', 14),
(8, 'Register of Enterprises of the Republic of Latvia', '2022-10-30', 19),
(9, 'Register of Enterprises of the Republic of Latvia', '2023-02-03', 19);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `movie_code` int(11) NOT NULL,
  `role` varchar(255) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `employee_ID_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `shareholder`
--

CREATE TABLE `shareholder` (
  `shareholder_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `shareholdername` varchar(255) NOT NULL,
  `place_of_birth` varchar(255) NOT NULL,
  `mother_maiden_name` varchar(255) NOT NULL,
  `father_first_name` varchar(255) NOT NULL,
  `personal_tel_no` varchar(255) NOT NULL,
  `national_insurance_no` varchar(255) NOT NULL,
  `passport_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shareholder`
--

INSERT INTO `shareholder` (`shareholder_id`, `company_id`, `shareholdername`, `place_of_birth`, `mother_maiden_name`, `father_first_name`, `personal_tel_no`, `national_insurance_no`, `passport_no`) VALUES
(1, 1, 'Joshua Henderson', 'Carlotta', 'Allen', 'Joshua', '+4418720344832', 'DD446670C', 913710591),
(2, 1, 'Brian Hugehe', 'Nashville', 'Brittany', 'Bell', '+449150208298', 'WZ752373M', 625956125),
(3, 2, 'Melissa Parker', 'Pinson', 'Audrey', 'James', '+446066572161', 'XQ564032V', 726476816),
(4, 2, 'Danielle Williams', 'San Rafael', 'Austin', 'Rivera', '+449147188773', 'ZO735894W', 362963126),
(5, 2, 'Patrick Thomas', 'Sault Sainte Marie', 'Amanda', 'Rivera', '+449207382088', 'YT353131B', 853455106),
(6, 3, 'Stephanie Perez', 'Mather', 'Alexis', 'Cooper', '+443303542252', 'FZ362605B', 329233571),
(7, 3, 'Alicia Ham', 'Oconto', 'Baker', 'Jeremy', '+448572020274', 'WE495795G', 945948565),
(9, 3, 'William Ward', 'Burnsville', 'Collins', 'Ethan', '+445702989554', 'RE916026M', 782765649),
(10, 4, 'Haley Barnes', 'Eldora', 'Anna', 'Thomas', '+494258622726', 'ZM618487E', 430536707),
(11, 4, 'Matthew Russel', 'Taconic', 'Jose', 'Rogers', '+499150433174', 'HM499709E', 116934430),
(12, 4, 'Kimberly Barnes', 'Blue Ridge', 'Hannah', 'Diaz', '+495624051810', 'GI342134O', 779530775),
(13, 4, 'Henry Hernandez', 'Columbia', 'Rachel', 'Flores', '+494242815158', 'KV745888E', 237094534),
(14, 4, 'Brianna Hall', 'Miamie', 'Megan', 'Rodriguez', '+492246997772', 'VW086492S', 570965822),
(15, 5, 'Victoria Clark', 'Savoonga', 'Lillian', 'Price', '+306607769482', 'XX394638K', 325073685),
(16, 5, 'Natalie Butler', 'Mathiston', 'David', 'Mitchell', '+305049555158', 'QK254507L', 262037140),
(17, 5, 'Heather Patterson', 'Sherborn', 'Courtney', 'Perez', '+309064212553', 'UR852567G', 266634639),
(18, 5, 'Sophia Torres', 'Red Ash', 'Maria', 'Hayes', '+308355443941', 'UL262925O', 507621519),
(19, 5, 'Nicholas Allen', 'Denham Springs', 'Danielle', 'Diaz', '+306199263250', 'FF313985K', 757439163),
(20, 5, 'Adam Jackson', 'Austina', 'Jennifer', 'Simmons', '+308603434451', 'DG528958O', 258051736),
(21, 6, 'Rachel Florres', 'Questa', 'Jessica', 'Phillips', '+363044397853', 'LH927804I', 767661153),
(22, 6, 'Amelia Mitchel', 'Jacksonville', 'Stephen', 'Wilson', '+366093602652', 'YF994444F', 318124464),
(23, 7, 'David Hill', 'South Lake Tahoe', 'Jonathan', 'Taylor', '+3537729925256', 'US542480Y', 287296359),
(24, 7, 'David King', 'Princeton', 'Mary', 'Coleman', '+3532767287592', 'WJ229395F', 527482704),
(25, 7, 'Theodore Morgan', 'Vancouver', 'Stephen', 'Kelly', '+3534324439892', 'KN468708V', 541873317),
(26, 7, 'John Diaz', 'Calipatria', 'Patrick', 'Howard', '+3539071426488', 'CL191100X', 864492211),
(27, 8, 'Steven Lee', 'Flint', 'Haley', 'Peterson', '+3716303090503', 'AQ722270G', 238001397),
(28, 8, 'Katherine Miller', 'Kellyton', 'Joseph', 'Barnes', '+3712532227986', 'YG684305U', 365784049),
(29, 8, 'Oliver Bill', 'Maple Plain', 'Jose', 'Howard', '18164018104', 'UT598339Y', 115671071),
(30, 9, 'Aaron Campbell', 'Stockton', 'Samuel', 'Young', '+3716052742947', 'BT462979R', 303872580),
(31, 9, 'Ryan Jackson', 'Spokane', 'Amber', 'Coleman', '+3719292000980', 'SP275340H', 385358634),
(35, 2, 'Jeremy Flores', 'Milbank', 'Erin', 'Bennett', '+444647285809', 'WY390641C', 492065041);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `application`
--
ALTER TABLE `application`
  ADD PRIMARY KEY (`application_id`),
  ADD KEY `applicationcompany` (`company_id`),
  ADD KEY `applicationgrant` (`grant_id`);

--
-- Indexes for table `compensation`
--
ALTER TABLE `compensation`
  ADD PRIMARY KEY (`faction_id`);

--
-- Indexes for table `contactinformation`
--
ALTER TABLE `contactinformation`
  ADD PRIMARY KEY (`info_id`),
  ADD KEY `contactemployee` (`employee_ID_no`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`dept_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employee_ID_no`),
  ADD KEY `employeecompany` (`company_id`),
  ADD KEY `employeefaction` (`faction_id`);

--
-- Indexes for table `faction`
--
ALTER TABLE `faction`
  ADD PRIMARY KEY (`faction_id`),
  ADD KEY `factiondepartment` (`dept_id`),
  ADD KEY `factiongroup` (`group_id`);

--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`movie_code`),
  ADD KEY `filmcompany` (`company_id`);

--
-- Indexes for table `grants`
--
ALTER TABLE `grants`
  ADD PRIMARY KEY (`grant_id`);

--
-- Indexes for table `personnelgroup`
--
ALTER TABLE `personnelgroup`
  ADD PRIMARY KEY (`group_id`);

--
-- Indexes for table `productioncompany`
--
ALTER TABLE `productioncompany`
  ADD PRIMARY KEY (`company_id`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`company_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`),
  ADD KEY `roleemployee` (`employee_ID_no`),
  ADD KEY `rolefilm` (`movie_code`);

--
-- Indexes for table `shareholder`
--
ALTER TABLE `shareholder`
  ADD PRIMARY KEY (`shareholder_id`),
  ADD KEY `shareholdingcompany` (`company_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `application`
--
ALTER TABLE `application`
  MODIFY `application_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `compensation`
--
ALTER TABLE `compensation`
  MODIFY `faction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `contactinformation`
--
ALTER TABLE `contactinformation`
  MODIFY `info_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `dept_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `faction`
--
ALTER TABLE `faction`
  MODIFY `faction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `grants`
--
ALTER TABLE `grants`
  MODIFY `grant_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `personnelgroup`
--
ALTER TABLE `personnelgroup`
  MODIFY `group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `productioncompany`
--
ALTER TABLE `productioncompany`
  MODIFY `company_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `shareholder`
--
ALTER TABLE `shareholder`
  MODIFY `shareholder_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `application`
--
ALTER TABLE `application`
  ADD CONSTRAINT `applicationcompany` FOREIGN KEY (`company_id`) REFERENCES `productioncompany` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `applicationgrant` FOREIGN KEY (`grant_id`) REFERENCES `grants` (`grant_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `compensation`
--
ALTER TABLE `compensation`
  ADD CONSTRAINT `compensationfaction` FOREIGN KEY (`faction_id`) REFERENCES `faction` (`faction_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `contactinformation`
--
ALTER TABLE `contactinformation`
  ADD CONSTRAINT `contactemployee` FOREIGN KEY (`employee_ID_no`) REFERENCES `employee` (`employee_ID_no`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employeecompany` FOREIGN KEY (`company_id`) REFERENCES `productioncompany` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `employeefaction` FOREIGN KEY (`faction_id`) REFERENCES `faction` (`faction_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `faction`
--
ALTER TABLE `faction`
  ADD CONSTRAINT `factiondepartment` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `factiongroup` FOREIGN KEY (`group_id`) REFERENCES `personnelgroup` (`group_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `film`
--
ALTER TABLE `film`
  ADD CONSTRAINT `filmcompany` FOREIGN KEY (`company_id`) REFERENCES `productioncompany` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `registration`
--
ALTER TABLE `registration`
  ADD CONSTRAINT `companyregistration` FOREIGN KEY (`company_id`) REFERENCES `productioncompany` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `roles`
--
ALTER TABLE `roles`
  ADD CONSTRAINT `roleemployee` FOREIGN KEY (`employee_ID_no`) REFERENCES `employee` (`employee_ID_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rolefilm` FOREIGN KEY (`movie_code`) REFERENCES `film` (`movie_code`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `shareholder`
--
ALTER TABLE `shareholder`
  ADD CONSTRAINT `shareholdingcompany` FOREIGN KEY (`company_id`) REFERENCES `productioncompany` (`company_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

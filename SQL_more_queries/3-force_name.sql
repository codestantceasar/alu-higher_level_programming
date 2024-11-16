-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbtn_test_db_3`;

-- Select the database
USE `hbtn_test_db_3`;

-- Drop the table if it exists (optional)
DROP TABLE IF EXISTS `force_name`;

-- Create the table with proper escaping
CREATE TABLE `force_name` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(255) NOT NULL
);

-- Insert data into the table
INSERT INTO `force_name` (`name`) VALUES
('Holberton School'),
('Python is cool'),
('Holberton'),
('School'),
('C is fun');

-- Query the table
SELECT `id`, `name` FROM `force_name`;

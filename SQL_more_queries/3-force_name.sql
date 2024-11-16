-- A script that creates the table force_name on your MySQL server
-- Query to create a table 
CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL);

-- Insert data into the table
INSERT INTO `force_name` (`name`) VALUES
('Holberton School'),
('Python is cool'),
('Holberton'),
('School'),
('C is fun');

-- Query the table
SELECT `id`, `name` FROM `force_name`;

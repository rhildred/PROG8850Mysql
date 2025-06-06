-- Create the 'companydb' database if it doesn't exist
CREATE DATABASE IF NOT EXISTS companydb;

-- Use the 'companydb' database
USE companydb;

-- Create the 'departments' table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255)
);
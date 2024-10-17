-- Use the created database
USE DATABASE etl_project_db;
USE SCHEMA public;

-- Create a table to store donation data
CREATE OR REPLACE TABLE donations (
    external_id STRING,
    first_name STRING,
    last_name STRING,
    email STRING,
    donation_date DATE,
    donation_amount DECIMAL(10, 2),
    most_recent_donation_date DATE,
    most_recent_donation_amount DECIMAL(10, 2)
);

-- Example: Add a table for constituent information
CREATE OR REPLACE TABLE constituents (
    constituent_id STRING,
    first_name STRING,
    last_name STRING,
    email STRING,
    address STRING,
    phone STRING,
    total_donations DECIMAL(10, 2),
    lifetime_donation_amount DECIMAL(10, 2),
    lifetime_donation_count INT
);

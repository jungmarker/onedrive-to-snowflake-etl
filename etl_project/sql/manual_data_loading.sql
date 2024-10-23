INSERT INTO donations (external_id, first_name, last_name, email, donation_date, donation_amount, most_recent_donation_date, most_recent_donation_amount)
VALUES
('1', 'John', 'Doe', 'john.doe@example.com', '2024-10-01', 100.00, '2024-10-01', 100.00),
('2', 'Jane', 'Doe', 'jane.doe@example.com', '2024-09-30', 150.50, '2024-09-30', 150.50);

INSERT INTO constituents (constituent_id, first_name, last_name, email, address, phone, total_donations, lifetime_donation_amount, lifetime_donation_count)
VALUES
('1', 'John', 'Doe', 'john.doe@example.com', '123 Main St', '555-1234', 100.00, 1000.00, 10),
('2', 'Jane', 'Doe', 'jane.doe@example.com', '456 Oak St', '555-5678', 150.50, 500.00, 5);

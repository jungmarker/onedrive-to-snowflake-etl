-- Total donations by each individual along with their donation count, grouped by month for the last 6 months
SELECT 
    c.first_name,
    c.last_name,
    SUM(d.donation_amount) AS total_donations,
    COUNT(d.donation_id) AS donation_count,
    DATE_TRUNC('month', d.donation_date) AS donation_month
FROM 
    donations d
JOIN 
    constituents c ON d.constituent_id = c.constituent_id
WHERE 
    d.donation_date >= DATEADD(MONTH, -6, CURRENT_DATE)
GROUP BY 
    c.first_name, c.last_name, donation_month
ORDER BY 
    total_donations DESC, donation_month;

-- Average donation amount by payment method over the past year, grouped by quarter
SELECT 
    d.donation_method,
    AVG(d.donation_amount) AS average_donation,
    DATE_TRUNC('quarter', d.donation_date) AS donation_quarter
FROM 
    donations d
WHERE 
    d.donation_date >= DATEADD(YEAR, -1, CURRENT_DATE)
GROUP BY 
    d.donation_method, donation_quarter
ORDER BY 
    average_donation DESC, donation_quarter;

-- Top 5 contributors by lifetime total donations and count their donations
SELECT 
    c.first_name,
    c.last_name,
    SUM(d.donation_amount) AS total_donations,
    COUNT(d.donation_id) AS donation_count
FROM 
    donations d
JOIN 
    constituents c ON d.constituent_id = c.constituent_id
GROUP BY 
    c.first_name, c.last_name
ORDER BY 
    total_donations DESC
LIMIT 5;

-- Number of donations made in the last month, grouped by donation method and donation date
SELECT 
    d.donation_method,
    COUNT(d.donation_id) AS donation_count,
    DATE_TRUNC('day', d.donation_date) AS donation_day
FROM 
    donations d
WHERE 
    d.donation_date >= DATEADD(MONTH, -1, CURRENT_DATE)
GROUP BY 
    d.donation_method, donation_day
ORDER BY 
    donation_day DESC;

-- Total donations, count of donations, and average donation amount by currency and payment method
SELECT 
    d.currency,
    d.donation_method,
    SUM(d.donation_amount) AS total_donations,
    COUNT(d.donation_id) AS donation_count,
    AVG(d.donation_amount) AS avg_donation
FROM 
    donations d
GROUP BY 
    d.currency, d.donation_method
ORDER BY 
    total_donations DESC;

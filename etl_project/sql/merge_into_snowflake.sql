MERGE INTO ETL_EXAMPLE_PROJECT.PUBLIC.donations AS target
USING (
    -- Select data from the CSV file, mapping columns to placeholders
    SELECT 
        $1 AS external_id,  -- Map external_id from CSV
        $2 AS first_name,    -- Map first_name from CSV
        $3 AS last_name,     -- Map last_name from CSV
        $4 AS email,         -- Map email from CSV
        TO_DATE($5, 'MM/DD/YYYY') AS donation_date,  -- Convert donation_date from CSV to date format
        $6::DECIMAL(10, 2) AS donation_amount  -- Cast donation_amount to decimal
    FROM @STAGE_PATH/transformed_data.csv (FILE_FORMAT => 'CSV_FILE_FORMAT')  -- Read from staged CSV
) AS source
ON target.external_id = source.external_id  -- Match on external_id
WHEN MATCHED THEN
    -- Update existing rows if external_id matches
    UPDATE SET
        target.first_name = source.first_name,
        target.last_name = source.last_name,
        target.email = source.email,
        target.donation_date = source.donation_date,
        target.donation_amount = source.donation_amount
WHEN NOT MATCHED THEN
    -- Insert new rows if external_id doesn't exist
    INSERT (external_id, first_name, last_name, email, donation_date, donation_amount)
    VALUES (source.external_id, source.first_name, source.last_name, source.email, source.donation_date, source.donation_amount);


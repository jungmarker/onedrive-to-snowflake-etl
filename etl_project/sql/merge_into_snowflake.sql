MERGE INTO ETL_EXAMPLE_PROJECT.PUBLIC.donations AS target
USING (
    SELECT 
        $1 AS external_id,
        $2 AS first_name,
        $3 AS last_name,
        $4 AS email,
        TO_DATE($5, 'MM/DD/YYYY') AS donation_date,
        $6::DECIMAL(10, 2) AS donation_amount
    FROM @STAGE_PATH/transformed_data.csv (FILE_FORMAT => 'CSV_FILE_FORMAT')
) AS source
ON target.external_id = source.external_id
WHEN MATCHED THEN
    UPDATE SET
        target.first_name = source.first_name,
        target.last_name = source.last_name,
        target.email = source.email,
        target.donation_date = source.donation_date,
        target.donation_amount = source.donation_amount
WHEN NOT MATCHED THEN
    INSERT (external_id, first_name, last_name, email, donation_date, donation_amount)
    VALUES (source.external_id, source.first_name, source.last_name, source.email, source.donation_date, source.donation_amount);

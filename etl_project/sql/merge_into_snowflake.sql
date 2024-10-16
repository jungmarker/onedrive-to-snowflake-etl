MERGE INTO ETL_EXAMPLE_PROJECT.PUBLIC.donations AS target
USING @STAGE_PATH/transformed_data.csv AS source
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

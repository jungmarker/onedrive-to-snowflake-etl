import os

# Snowflake connection details
SNOWFLAKE_CONN = {
    'user': 'njungmarker',
    'password': 'Aidsplus1!',  # Replace with your actual Snowflake password
    'account': 'bzb66620.us-east-1',
    'warehouse': 'ETL_WAREHOUSE',
    'database': 'ETL_EXAMPLE_PROJECT',
    'schema': 'PUBLIC'
}

# OneDrive API credentials (update with actual values from Microsoft Entra ID)
ONEDRIVE = {
    'client_id': 'your_actual_client_id',
    'client_secret': 'your_actual_client_secret',
    'tenant_id': 'your_actual_tenant_id'
}

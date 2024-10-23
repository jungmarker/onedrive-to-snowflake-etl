import unittest
from scripts.transform_csv_data import transform_csv_data
from scripts.transform_json_data import transform_json_data
import pandas as pd
import os
import json

class TestETLWorkflow(unittest.TestCase):

    def test_transform_csv_data(self):
        # Create a mock CSV file
        test_csv = '/tmp/test_donations.csv'
        test_data = pd.DataFrame({
            'external_id': ['123', '456', '789', '123'],  # Duplicate ID for testing
            'donation_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01']
        })
        test_data.to_csv(test_csv, index=False)

        transformed_file = transform_csv_data(test_csv)
        transformed_df = pd.read_csv(transformed_file)

        # Check if duplicates are removed and dates are transformed
        self.assertEqual(len(transformed_df), 3)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(transformed_df['donation_date']))

    def test_transform_json_data(self):
        # Create a mock JSON file
        test_json = '/tmp/test_donations.json'
        test_data = [
            {"external_id": "123", "donation_date": "2024-01-01"},
            {"external_id": "456", "donation_date": "2024-01-02"},
            {"external_id": "789", "donation_date": "2024-01-03"},
            {"external_id": "123", "donation_date": "2024-01-01"}  # Duplicate ID for testing
        ]

        with open(test_json, 'w') as f:
            json.dump(test_data, f)

        transformed_file = transform_json_data(test_json)
        transformed_df = pd.read_csv(transformed_file)

        # Check if duplicates are removed and dates are transformed
        self.assertEqual(len(transformed_df), 3)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(transformed_df['donation_date']))

if __name__ == '__main__':
    unittest.main()

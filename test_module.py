import unittest
import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

class TestDemographicDataAnalyzer(unittest.TestCase):
    def setUp(self):
        # Run the function once before all tests to save time
        self.result = calculate_demographic_data()

    def test_return_type(self):
        # Check that the returned result is a dictionary
        self.assertIsInstance(self.result, dict)

    def test_race_count(self):
        # Check that race_count is a pandas Series and not empty
        self.assertIn('race_count', self.result)
        self.assertIsInstance(self.result['race_count'], pd.Series)
        self.assertGreater(len(self.result['race_count']), 0)

    def test_average_age_men(self):
        # Check average_age_men is a float within a reasonable range
        self.assertIn('average_age_men', self.result)
        self.assertIsInstance(self.result['average_age_men'], float)
        self.assertTrue(20 < self.result['average_age_men'] < 60)

    def test_percentage_values(self):
        # Check that percentage values are floats between 0 and 100
        percentage_keys = [
            'percentage_bachelors',
            'percentage_higher_education',
            'percentage_lower_education',
            'rich_percentage_min_hours',
            'highest_earning_country_percentage'
        ]
        for key in percentage_keys:
            self.assertIn(key, self.result)
            self.assertIsInstance(self.result[key], float)
            self.assertGreaterEqual(self.result[key], 0)
            self.assertLessEqual(self.result[key], 100)

    def test_min_work_hours(self):
        # Check min_work_hours is a positive number (int or float)
        self.assertIn('min_work_hours', self.result)
        self.assertIsInstance(self.result['min_work_hours'], (int, float))
        self.assertGreater(self.result['min_work_hours'], 0)

    def test_highest_earning_country(self):
        # Check highest_earning_country is a non-empty string
        self.assertIn('highest_earning_country', self.result)
        self.assertIsInstance(self.result['highest_earning_country'], str)
        self.assertGreater(len(self.result['highest_earning_country']), 0)

    def test_top_IN_occupation(self):
        # Check top_IN_occupation is a non-empty string
        self.assertIn('top_IN_occupation', self.result)
        self.assertIsInstance(self.result['top_IN_occupation'], str)
        self.assertGreater(len(self.result['top_IN_occupation']), 0)

if __name__ == '__main__':
    unittest.main()



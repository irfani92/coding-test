import unittest
from repositories.sales_rep_repository import SalesRepRepository
import os

class TestSalesRepRepository(unittest.TestCase):

    def setUp(self):
        # Create a dummy JSON file for testing
        self.dummy_data = {
            "salesReps": [
                {
                    "id": 1,
                    "name": "Test Rep 1",
                    "role": "Sales",
                    "region": "North",
                    "skills": ["communication"],
                    "deals": [{"client": "Client A", "value": 1000, "status": "Won"}],
                    "clients": [{"name": "Client X", "industry": "Tech", "contact": "john@example.com"}]
                },
                {
                    "id": 2,
                    "name": "Test Rep 2",
                    "role": "Manager",
                    "region": "South",
                    "skills": ["leadership"],
                    "deals": [],
                    "clients": []
                }
            ]
        }
        self.dummy_file_path = "test_dummy_data.json"
        with open(self.dummy_file_path, "w") as f:
            import json
            json.dump(self.dummy_data, f)

    def tearDown(self):
        # Clean up the dummy file after testing
        if os.path.exists(self.dummy_file_path):
            os.remove(self.dummy_file_path)

    def test_load_dummy_data(self):
        sales_reps = SalesRepRepository.load_dummy_data(self.dummy_file_path)
        self.assertEqual(len(sales_reps), 2)
        self.assertEqual(sales_reps[0].id, 1)
        self.assertEqual(sales_reps[0].name, "Test Rep 1")
        self.assertEqual(len(sales_reps[0].deals), 1)
        self.assertEqual(sales_reps[0].deals[0].client, "Client A")

    def test_load_dummy_data_all(self):
        data_json = SalesRepRepository.load_dummy_data_all(self.dummy_file_path)
        import json
        data = json.loads(data_json)
        self.assertIn("salesReps", data)
        self.assertEqual(len(data["salesReps"]), 2)
        self.assertEqual(data["salesReps"][0]["name"], "Test Rep 1")

if __name__ == "__main__":
    unittest.main()
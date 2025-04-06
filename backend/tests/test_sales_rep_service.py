import unittest
from unittest.mock import MagicMock
from services.sales_rep_service import SalesRepService
from repositories.sales_rep_repository import SalesRepRepository
from models.sales_rep import SalesRep, Deal, Client

class TestSalesRepService(unittest.TestCase):

    def setUp(self):
        self.mock_repository = MagicMock(spec=SalesRepRepository)
        self.sales_rep_service = SalesRepService(self.mock_repository)
        self.dummy_sales_reps = [
            SalesRep(id=1, name="Rep A", role="Sales", region="East", skills=[], deals=[], clients=[]),
            SalesRep(id=2, name="Rep B", role="Sales", region="West", skills=[], deals=[], clients=[]),
        ]
        self.mock_repository.load_dummy_data.return_value = self.dummy_sales_reps

    def test_get_sales_reps(self):
        file_path = "dummy_path.json"
        sales_reps = self.sales_rep_service.get_sales_reps(file_path)
        self.assertEqual(sales_reps, self.dummy_sales_reps)
        self.mock_repository.load_dummy_data.assert_called_once_with(file_path)

    def test_get_sales_rep_by_id_found(self):
        file_path = "dummy_path.json"
        rep = self.sales_rep_service.get_sales_rep_by_id(1, file_path)
        self.assertEqual(rep, self.dummy_sales_reps[0])
        self.mock_repository.load_dummy_data.assert_called_once_with(file_path)

    def test_get_sales_rep_by_id_not_found(self):
        file_path = "dummy_path.json"
        rep = self.sales_rep_service.get_sales_rep_by_id(3, file_path)
        self.assertIsNone(rep)
        self.mock_repository.load_dummy_data.assert_called_once_with(file_path)

if __name__ == "__main__":
    unittest.main()
import unittest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from controllers.sales_rep_controller import api_router
from services.sales_rep_service import SalesRepService
from repositories.sales_rep_repository import SalesRepRepository
from schemas.sales_rep import SalesRepSchema
from typing import List

# Mock the SalesRepService and SalesRepRepository
class MockSalesRepRepository:
    def load_dummy_data(self, file_path: str):
        return [
            {"id": 1, "name": "Rep 1", "role": "Sales", "region": "East", "skills": [], "deals": [], "clients": []},
            {"id": 2, "name": "Rep 2", "role": "Sales", "region": "West", "skills": [], "deals": [], "clients": []},
        ]

class MockSalesRepService:
    def __init__(self, repository):
        self.repository = repository

    def get_sales_reps(self, file_path: str) -> List[dict]:
        data = self.repository.load_dummy_data(file_path)
        return [SalesRepSchema(**rep) for rep in data]

    def get_sales_rep_by_id(self, rep_id: int, file_path: str) -> dict:
        data = self.repository.load_dummy_data(file_path)
        for rep in data:
            if rep["id"] == rep_id:
                return SalesRepSchema(**rep)
        return None

# Create a new FastAPI app instance for testing with the mocked dependencies
from fastapi import FastAPI
app = FastAPI()
app.include_router(api_router)
app.dependency_overrides[SalesRepService] = lambda: MockSalesRepService(MockSalesRepRepository())

client = TestClient(app)

class TestSalesRepController(unittest.TestCase):

    def test_get_sales_reps(self):
        response = client.get("/api/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(response.json()[0]["id"], 1)
        self.assertEqual(response.json()[1]["name"], "Bob")

    def test_get_sales_rep_by_id_found(self):
        response = client.get("/api/data/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 1)
        self.assertEqual(response.json()["name"], "Alice")

    def test_get_sales_rep_by_id_not_found(self):
        response = client.get("/api/data/30")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "SalesRep not found"})

if __name__ == "__main__":
    unittest.main()
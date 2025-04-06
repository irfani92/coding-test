import unittest
from unittest.mock import MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from controllers.ai_controller import api_router, QuestionRequest
from services.ai_service import AIService
from config import Settings
from repositories.sales_rep_repository import SalesRepRepository


class TestAIController(unittest.TestCase):

    def setUp(self):
        self.app = FastAPI()
        self.app.include_router(api_router)
        self.client = TestClient(self.app)
        self.mock_ai_service = MagicMock(spec=AIService)
        self.app.dependency_overrides[AIService] = lambda: self.mock_ai_service
        self.mock_settings = MagicMock(spec=Settings)
        self.app.dependency_overrides[Settings] = lambda: self.mock_settings

    def test_ai_endpoint_success(self):
        """
        Tests the /api/ai endpoint with a successful AI response.
        """
        user_question = "What is Alice's region?"
        mock_ai_response = "Alice's region is North America.\n"
        self.mock_ai_service.get_ai_response.return_value = mock_ai_response

        response = self.client.post("/api/ai", json={"question": user_question})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"answer": mock_ai_response})

    def test_ai_endpoint_empty_json(self):
        """
        Tests the /api/ai endpoint when the AI service with empty json.
        """
        self.mock_ai_service.get_ai_response.return_value = None

        response = self.client.post("/api/ai",json={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {"detail": [{'type': 'missing', 'loc': ['body', 'question'], 'msg': 'Field required', 'input': {}}]})

    def test_ai_endpoint_invalid_input(self):
        """
        Tests the /api/ai endpoint with invalid input data.
        """
        response = self.client.post("/api/ai", json={"invalid_field": "some value"})
        self.assertEqual(response.status_code, 422)
        self.assertTrue("question" in response.json()["detail"][0]["loc"])

if __name__ == "__main__":
    unittest.main()
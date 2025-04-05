from fastapi import APIRouter, HTTPException, Request
from services.ai_service import AIService
from pydantic import BaseModel
from config import settings
from repositories.sales_rep_repository import SalesRepRepository


# Pydantic model for the input data
class QuestionRequest(BaseModel):
    question: str

api_router = APIRouter()
ai_service = AIService()

@api_router.post("/api/ai")
async def ai_endpoint(request: QuestionRequest):
    """
    Accepts a user question and returns a placeholder AI response.
    """
    # body = await request.json()
    user_question = request.question
    
    # Placeholder: Eventually replace with a call to an AI service.
    sales_reps = SalesRepRepository.load_dummy_data_all(settings.file_path)
    ai_response = ai_service.get_ai_response(user_question, sales_reps)
    0
    if not ai_response:
        raise HTTPException(status_code=500, detail="AI service failed to respond")
    
    return {"answer": ai_response}

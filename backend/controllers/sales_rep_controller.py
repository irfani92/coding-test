# API endpoint controllers (FastAPI routes)
from fastapi import APIRouter, HTTPException
from typing import List
from services.sales_rep_service import SalesRepService
from schemas.sales_rep import SalesRepSchema
from repositories.sales_rep_repository import SalesRepRepository
from config import settings

api_router = APIRouter()

# Initialize service
sales_rep_service = SalesRepService(SalesRepRepository())

@api_router.get("/api/data", response_model=List[SalesRepSchema])
async def get_sales_reps():
    """
    Returns list of all sales representatives with their data.
    """
    sales_reps = sales_rep_service.get_sales_reps(settings.file_path)
    return [rep.to_dict() for rep in sales_reps]

@api_router.get("/api/data/{rep_id}", response_model=SalesRepSchema)
async def get_sales_rep_by_id(rep_id: int):
    """
    Returns a sales representative's data by their ID.
    """
    sales_rep = sales_rep_service.get_sales_rep_by_id(rep_id, settings.file_path)
    if sales_rep is None:
        raise HTTPException(status_code=404, detail="SalesRep not found")
    return sales_rep.to_dict()

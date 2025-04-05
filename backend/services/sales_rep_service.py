# Core business logic for sales rep data

from typing import List
from repositories.sales_rep_repository import SalesRepRepository
from models.sales_rep import SalesRep

class SalesRepService:
    def __init__(self, repository: SalesRepRepository):
        self.repository = repository

    def get_sales_reps(self, file_path: str) -> List[SalesRep]:
        return self.repository.load_dummy_data(file_path)

    def get_sales_rep_by_id(self, rep_id: int, file_path: str) -> SalesRep:
        sales_reps = self.repository.load_dummy_data(file_path)
        for rep in sales_reps:
            if rep.id == rep_id:
                return rep
        return None

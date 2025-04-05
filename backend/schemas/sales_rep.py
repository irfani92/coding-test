# Pydantic schemas for validation

from pydantic import BaseModel
from typing import List

class DealSchema(BaseModel):
    client: str
    value: int
    status: str

class ClientSchema(BaseModel):
    name: str
    industry: str
    contact: str

class SalesRepSchema(BaseModel):
    id: int
    name: str
    role: str
    region: str
    skills: List[str]
    deals: List[DealSchema]
    clients: List[ClientSchema]

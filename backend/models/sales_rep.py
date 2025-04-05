# Models representing the structure of Sales Rep data

from typing import List, Dict

class Deal:
    def __init__(self, client: str, value: int, status: str):
        self.client = client
        self.value = value
        self.status = status

class Client:
    def __init__(self, name: str, industry: str, contact: str):
        self.name = name
        self.industry = industry
        self.contact = contact

class SalesRep:
    def __init__(self, id: int, name: str, role: str, region: str, skills: List[str], deals: List[Deal], clients: List[Client]):
        self.id = id
        self.name = name
        self.role = role
        self.region = region
        self.skills = skills
        self.deals = deals
        self.clients = clients

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "region": self.region,
            "skills": self.skills,
            "deals": [deal.__dict__ for deal in self.deals],
            "clients": [client.__dict__ for client in self.clients]
        }

# Data access layer (loading data from a JSON file)

import json
from pathlib import Path
from typing import List
from models.sales_rep import SalesRep, Deal, Client

class SalesRepRepository:
    @staticmethod
    def load_dummy_data(file_path: str) -> List[SalesRep]:
        with open(file_path, "r") as file:
            data = json.load(file)

        sales_reps = []
        for rep in data["salesReps"]:
            deals = [Deal(client=d["client"], value=d["value"], status=d["status"]) for d in rep["deals"]]
            clients = [Client(name=c["name"], industry=c["industry"], contact=c["contact"]) for c in rep["clients"]]
            sales_reps.append(SalesRep(id=rep["id"], name=rep["name"], role=rep["role"], region=rep["region"], skills=rep["skills"], deals=deals, clients=clients))
        
        return sales_reps
    
    @staticmethod
    def load_dummy_data_all(file_path: str) -> List[SalesRep]:
        with open(file_path, "r") as file:
            data = json.load(file)
           
        return json.dumps(data, default=lambda o: o.dict(), indent=4)


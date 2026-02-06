from pydantic import BaseModel
from typing import List, Dict

class patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact: Dict[str, str]

def insert(patient: patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("Data Inserted Successfully")


patient_info={"name":"Monirul Islam", "age": 24, "weight": 62.5, "married": False, "allergies": ["Begun", "Sim"], "contact": {"Phone":"07142958888"}}

patient_1=patient(**patient_info)

insert(patient_1)


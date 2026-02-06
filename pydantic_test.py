from pydantic import BaseModel
from typing import List, Dict, Optional

class patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]]=None
    contact: Dict[str, str]

def insert(patient: patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("Data Inserted Successfully")


patient_info={"name":"Monirul Islam", "age": 24, "weight": 62.5, "married": False,  "contact": {"Phone":"07142958888"}}

patient_1=patient(**patient_info)

insert(patient_1)


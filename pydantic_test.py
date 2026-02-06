from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    fb_url: AnyUrl
    weight: float
    married: bool=False
    allergies: Optional[List[str]]=None
    contact: Dict[str, str]

def insert(patient: patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.fb_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
    print("Data Inserted Successfully")


patient_info={"name":"Monirul Islam", "age": 24, "email":"monirul@gmail.com", "fb_url":"https://www.facebook.com/moniirrul","weight": 62.5, "contact": {"Phone":"07142958888"}}

patient_1=patient(**patient_info)

insert(patient_1)


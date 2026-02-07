from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of The Patient ", description="Name of Patient Less than 50 Char", examples=["Monirul", "Akib"])]

    age: int= Field (gt=0, lt=120)
    email: EmailStr
    fb_url: AnyUrl
    weight: float= Field(gt=0, lt=150)
    married: Annotated[bool, Field(default=None, description="Is that Patient Married or Not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact: Dict[str, str]

def insert(patient: patient):

    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Email: {patient.email}")
    print(f"Any URL: {patient.fb_url}")
    print(f"Weight: {patient.weight}")
    print(f"Material Status: {patient.married}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact: {patient.contact}")
    print("Data Inserted Successfully")


patient_info={"name":"Monirul Islam", "age": 24, "email":"monirul@gmail.com", "fb_url":"https://www.facebook.com/moniirrul","weight": 62.5, "contact": {"Phone":"07142958888"}}

patient_1=patient(**patient_info)

insert(patient_1)


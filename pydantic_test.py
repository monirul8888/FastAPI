from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of The Patient ", description="Name of Patient Less than 50 Char", examples=["Monirul", "Akib"])]

    age: int= Field (gt=0, lt=120)
    email: EmailStr
    fb_url: AnyUrl
    weight: float= Field(gt=0, lt=150)
    height: float
    married: Annotated[bool, Field(default=None, description="Is that Patient Married or Not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        
        valid_domains=["hdfc.com", "icici.com"]
        domain_name=value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a Valid Email")
        
        return value
    
    @field_validator("name")
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age>60 and "emergency" not in model.contact:
            raise ValueError("Patient older than 60 must have and Emergency Contact")
        return model
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round((self.weight)/(self.height**2),2)

        return bmi



def insert(patient: Patient):

    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Height: {patient.height}")
    print(f"Weight: {patient.weight}")
    print(f"BMI: {patient.bmi}")
    print(f"Email: {patient.email}")
    print(f"Any URL: {patient.fb_url}")
    print(f"Weight: {patient.weight}")
    print(f"Material Status: {patient.married}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact: {patient.contact}")
    print("Data Inserted Successfully")


patient_info={"name":"Monirul Islam", "age": 65, "weight":62, "height": 1.65, "email":"monirul@hdfc.com", "fb_url":"https://www.facebook.com/moniirrul","weight": 62.5, "contact": {"Phone":"07142958888", "emergency":"0174295888"}}

patient_1=Patient(**patient_info)

insert(patient_1)


from pydantic import BaseModel , EmailStr, AnyUrl , Field , field_validator , model_validator
from typing import List , Dict , Optional, Annotated

class pateint(BaseModel):

    name:str
    age:int
    email:EmailStr 
    weight:float
    married:bool
    allergies:List[str]
    contact:Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency'not in model.contact:
            raise ValueError('Pateint older than 60 must have emergency contact')
        return model
  
         # if we give age>60 that will give error, to correct it we add emergency contact details.

def insert_pateint_data(pateint:pateint):
    print(pateint.name)
    print(pateint.email)
    print(pateint.age)
    print(pateint.weight)
    print(pateint.married)
    print(pateint.allergies)
    print(pateint.contact)
    print("Inserted")

pateint1 = pateint(name ="kishan", email="kishan@hdfc.com",age= 65 , weight =55.6 ,married=False,allergies ={"anesil"},contact={'email':'abc@gmail.com', 'phone': '724713244', 'emergency':'2444355'} ) 

insert_pateint_data(pateint1)
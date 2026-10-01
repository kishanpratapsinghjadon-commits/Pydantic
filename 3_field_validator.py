from pydantic import BaseModel , EmailStr, AnyUrl , Field , field_validator
from typing import List , Dict , Optional, Annotated

class pateint(BaseModel):

    name:str
    age:int
    email:EmailStr 
    weight:float
    married:bool
    allergies:List[str]
    contact:Dict[str, str]

    @field_validator('email' , mode='after') # value i will get after type coersion , if i select before then i will get before type coersion and by default it's after
    @classmethod
    def eamil_validator(cls , value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value           # Now only valid gmails will work like - abc@hdfc.com & abc@icici.com other than this will give an error

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()    # Now this will capitalize all name letters

    @field_validator('age', mode='after') # pateint1 has age in str if we get value before type coersion then this will give error as it comparre b/w str & int
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def insert_pateint_data(pateint:pateint):
    print(pateint.name)
    print(pateint.email)
    print(pateint.age)
    print(pateint.weight)
    print(pateint.married)
    print(pateint.allergies)
    print(pateint.contact)
    print("Inserted")

pateint1 = pateint(name ="kishan", email="kishan@hdfc.com",age= '30', weight =55.6 ,married=False,allergies ={"anesil"},contact={'email':'abc@gmail.com', 'phone': '724713244'}) # now when we give any different datatype other then assign this will show error 

insert_pateint_data(pateint1)
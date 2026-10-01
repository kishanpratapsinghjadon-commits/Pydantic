from pydantic import BaseModel , EmailStr, AnyUrl , Field , computed_field
from typing import List , Dict , Optional, Annotated

class pateint(BaseModel):

    name:str
    age:int
    email:EmailStr 
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact:Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def insert_pateint_data(pateint:pateint):
    print(pateint.name)
    print(pateint.email)
    print(pateint.age)
    print(pateint.weight)
    print('BMI', pateint.calculate_bmi)
    print(pateint.married)
    print(pateint.allergies)
    print(pateint.contact)
    print("Inserted")

pateint1 = pateint(name ="kishan", email="kishan@hdfc.com",age= '30', weight =55.6, height=1.65 ,married=False,allergies ={"anesil"},contact={'email':'abc@gmail.com', 'phone': '724713244'})

insert_pateint_data(pateint1)
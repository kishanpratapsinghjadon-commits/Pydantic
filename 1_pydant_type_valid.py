
# class Patient():
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def insert_patient_data(self):
#         print(self.name)
#         print(self.age)
#         print("Inserted")


# patient1 = Patient(name="kishan", age="thirty") # age is def as int it still print str when str input given , here it must raise type error

# patient1.insert_patient_data()


from pydantic import BaseModel , EmailStr
from typing import List , Dict , Optional
class pateint(BaseModel):
    name:str
    age:int
    email:EmailStr # this is pydantic built in datatype (for email validation)
    weight:float
    married:bool
    allergies:List[str] = None # none is the defalut value if we don't include allergies this will print none
    contact:Optional[Dict[str, str]] = None # this field is optional if don't include this in pateint1 data then this will not give error
def insert_pateint_data(pateint:pateint):
    print(pateint.name)
    print(pateint.email)
    print(pateint.age)
    print(pateint.weight)
    print(pateint.married)
    print(pateint.allergies)
    print(pateint.contact)
    print("Inserted")

def update_data(pateint:pateint):
    print(pateint.name)
    print(pateint.age)
    print("Updated")

pateint1 = pateint(name ="kishan", email="kishan@gmail.com",age= 30, weight =55.6 ,married=False,allergies ={"anesil"},contact={'email':'abc@gmail.com', 'phone': '724713244'}) # now when we give any different datatype other then assign this will show error 

insert_pateint_data(pateint1)

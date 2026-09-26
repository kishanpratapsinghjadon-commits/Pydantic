from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import Annotated

class pateint(BaseModel):
    name:Annotated[str, Field(max_length=50, title='Name of the pateint',
 description='Give the name of the pateint in less than 50 chars', examples=['Kishan','amit'])] # using field  and annotated func we can add meta data as seen in code
    
    age:int = Field(gt=0 , lt=110)# this field func sets the range
    
    email:EmailStr # this is pydantic built in datatype (for email validation)
    
    linkedin_url:AnyUrl  # this is pydantic built in datatype (for URL validation)
   

def insert_pateint_data(pateint:pateint):
    print(pateint.name)
    print(pateint.email)
    print(pateint.age)
    print(pateint.linkedin_url)
    print("Inserted")

def update_data(pateint:pateint):
    print(pateint.name)
    print(pateint.age)

    print("Updated")

pateint1 = pateint(name ="kishan", email="kishan@gmail.com", age= 30,linkedin_url="http://linkedin.com/1324345")

insert_pateint_data(pateint1)
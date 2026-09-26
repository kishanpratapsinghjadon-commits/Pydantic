from pydantic import BaseModel , EmailStr , AnyUrl

class pateint(BaseModel):
    name:str
    age:int
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
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:int

class Pateint(BaseModel):
    name:str
    age:int
    gender:str
    address:Address

address1 = Address(city= 'Gwalior', state= 'Madhyapradesh', pin= 474012)
pateint1 = Pateint(name= 'kishan', age= 19, gender= 'purush', address=address1)

temp = pateint1.model_dump() # pateint1.model_dump_json to print in json
# temp = pateint1.model_dump(include=['name'])
# temp =pateint1.model_dump(exclude={address:['city']})

print(temp)
print(type(temp))
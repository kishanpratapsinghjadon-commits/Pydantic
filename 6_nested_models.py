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

print(pateint1.name)
print(pateint1.address.city)
print(pateint1.address.pin)
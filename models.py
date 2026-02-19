from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

class Numbers(BaseModel):
    num1: float
    num2: float

class UserAge(BaseModel):
    name: str
    age: int
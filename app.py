from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, Numbers, UserAge

app = FastAPI()

#Задание 1.1
@app.get("/")
async def welcome():
    return {"message": "Добро пожаловать в моё приложение FastAPI! (плюс изменил)"}

#Задание 1.2
@app.get("/secondTask")
async def second_task():
    return FileResponse("index.html")

#Задание 1.3
@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

#Задание 1.4
user = User(name="Домашев Егор Сергеевич", id=1)  
@app.get("/users")
async def get_user():
    return user  

#Задание 1.5
@app.post("/user")
async def check_user_age(user_data: UserAge):
    is_adult = user_data.age >= 18    
    response = {
        "name": user_data.name,
        "age": user_data.age,
        "is_adult": is_adult
    }
    return response
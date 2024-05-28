from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
import uvicorn
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id : Optional[int] = Field(primary_key=True)
    username:str
    email:str
users = [User(id=1,username="ya",email="ya@gmail.com"),User(id=2,username="admin",email="admin@gmail.com")]

@app.post("/users/{user_id}")
def user_id(user_id:int):
    
    for user in users:
        if user.id == user_id:
            return user
    return "User not founded"
@app.get("/users")
def get_users():
    return users
@app.post("/create_user")
def create_user(username:str,email:str):
    user = User(username=username, email=email)
    users.append(user)
    return "User was added"
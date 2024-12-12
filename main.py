from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
import uvicorn
from typing import Optional
import sqlite3

app = FastAPI()
con = sqlite3.connect("users.db")
cur = con.cursor()
def get_user_by_id(user_id):
    cur.execute("SELECT user_name, email FROM users WHERE id=?",user_id)
    return cur.fetchone()
class User(BaseModel):
    id : int
    username:str
    email:str
users = [User(id=1,username="ya",email="ya@gmail.com"),User(id=2,username="admin",email="admin@gmail.com")]

@app.post("/users/{user_id}")
def user_id(user_id:int):
    get_user_by_id(user_id=user_id)
@app.get("/users")
def get_users():
    return users
@app.post("/create_user")
def create_user(user:User):
    
    users.append(user)
    return "User was added"
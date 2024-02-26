from fastapi import FastApi  
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:str


class Post(BaseModel):
    title:str
    content:str
    user:User

app = FastApi()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/")
def post_method(req:Post):
    return req

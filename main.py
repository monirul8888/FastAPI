from fastapi import FastAPI
from pydantic import BaseModel, AnyUrl

app=FastAPI()


class course(BaseModel):
    name: str
    id: int
    url: AnyUrl


@app.post("/course")
def course(post: course):
    return {"data": post}


@app.get("/")
def home():
    return {"message": "Welcome To Fast-API Thanks...!"}



@app.get("/home")
def home():
    return {"message": "Welcome To Home Page"}
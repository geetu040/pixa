from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service import create_user, verify_user

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.get("/")
def index():
    return JSONResponse("Application is all set")

@app.post("/create_user")
def post_create_user(user: User):
    return create_user(user.username, user.password)

@app.post("/verify_user")
def post_verify_user(user: User):
    return verify_user(user.username, user.password)
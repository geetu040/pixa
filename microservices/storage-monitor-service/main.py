from fastapi import FastAPI
from pydantic import BaseModel
from service import get_storage_usage

app = FastAPI()

class User(BaseModel):
    username: str

@app.get("/")
def index():
    return "Application is all set"

@app.post("/get_storage_usage")
def post_get_storage_usage(user: User):
    return get_storage_usage(user.username)
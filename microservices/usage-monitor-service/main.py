from fastapi import FastAPI
from pydantic import BaseModel
from service import get_bandwidth_usage

app = FastAPI()

class User(BaseModel):
    username: str

@app.get("/")
def index():
    return "Application is all set"

@app.post("/get_bandwidth_usage")
def post_get_bandwidth_usage(user: User):
    return get_bandwidth_usage(user.username)
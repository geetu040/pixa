from fastapi import FastAPI
from pydantic import BaseModel
import service

app = FastAPI()

class User(BaseModel):
    username: str

class UserImageUpload(BaseModel):
    username: str
    file_base64: str

class Image(BaseModel):
    link: str

@app.get("/")
def index():
    return "Application is all set"

@app.post("/create_user")
def post_create_user(user: User):
    return service.create_user(user.username)

@app.post("/get_images_links")
def post_get_images_links(user: User):
    return service.get_images_links(user.username)

@app.post("/upload_image")
def post_upload_image(user: UserImageUpload):
    return service.upload_image(user.username, user.file_base64)

@app.post("/delete_image")
def post_delete_image(image: Image):
    return service.delete_image(image.link)

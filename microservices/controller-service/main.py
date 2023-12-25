from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from jose import jwt
from pydantic import BaseModel
import service
import base64
import utils
from config import SECRET_KEY, ALGORITHM

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_token(username: str):
	to_encode = {'sub': username}
	token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return token

def decode_token(token: str):
	payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
	username = payload.get("sub", None)
	return username

# ---------------

@app.get("/")
def html_index():
    return FileResponse("static/index.html")

@app.get("/login")
def html_login():
    return FileResponse("static/login.html")

@app.get("/favicon")
def html_favicon():
    return FileResponse("static/favicon.png")

# ---------------

class AuthUser(BaseModel):
	username: str
	password: str

@app.post("/auth_user")
def post_auth_user(user: AuthUser):

	# check if inputs are correct
	username = user.username.strip()
	password = user.password.strip()
	response = utils.validation(username, password)
	if response.status_code != 200:
		return response

	# authenticate the creds
	response = service.auth_user(username, password)

	# if successful create token
	if response.status_code == 200:
		token = create_token(username)
		return JSONResponse({"token": token})

	# else return error response
	return response

# ---------------

@app.post("/load_user_data")
def post_load_user_data(token: str = Depends(oauth2_scheme)):
	username = decode_token(token)
	if username == None: return JSONResponse("Unauthorized", 400)

	return service.load_user_data(username)

# ---------------

@app.post("/upload_image")
def post_upload_image(file: UploadFile = File(...), token: str = Depends(oauth2_scheme)):

	# Preparing Inputs
	username = decode_token(token)
	if username == None: return JSONResponse("Unauthorized", 400)
	file_binary = file.file.read()	# binary data
	file_base64 = base64.b64encode(file_binary).decode('utf-8')	# base64

	# Uploading the File
	response = service.upload_image(username, file_base64)

	# Invalid Response, exit here
	if response.status_code != 200:
		return response

	# Load latest data
	response = service.load_user_data(username)

	# Returning final response
	return response

# ---------------

class Image(BaseModel):
	link: str

@app.post("/delete_image")
def post_delete_image(image: Image, token: str = Depends(oauth2_scheme)):
	username = decode_token(token)
	if username == None: return JSONResponse("Unauthorized", 400)

	response = service.delete_image(image.link)

	# Invalid Response, exit here
	if response.status_code != 200:
		return response

	# Load latest data
	response = service.load_user_data(username)

	# Returning final response
	return response
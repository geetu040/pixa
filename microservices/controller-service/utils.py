import requests
from fastapi.responses import JSONResponse

def send_request(url, data):
	response = requests.post(
		url,
		json=data
	)
	response = JSONResponse(content=response.json(), status_code=response.status_code)
	return response

def validation(username, password):
	is_valid = len(username) >= 3 and len(password) >= 3

	if is_valid:
		return JSONResponse("")
	else:
		return JSONResponse("Inputs cannot be smaller than 3 characters", 400)
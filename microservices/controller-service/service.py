from fastapi.responses import JSONResponse
from concurrent.futures import ThreadPoolExecutor
from config import API_EPS
import utils
import json
import random

# =====> MAIN FUNCTIONS

def auth_user(username, password):

	response = verify_user(username, password)

	if response.status_code == 200:
		# verified
		return response

	if response.status_code == 400:
		# incorrect password
		return response

	if response.status_code == 201:
		# new username, create user
		return create_user(username, password)

	# some other response
	return response

def load_user_data(username):

	with ThreadPoolExecutor() as executor:
		# Execute the functions concurrently
		storage_usage_future = executor.submit(get_storage_usage, username)
		bandwidth_usage_future = executor.submit(get_bandwidth_usage, username)
		images_links_future = executor.submit(get_images_links, username)

	# Get results from the futures
	storage_usage = storage_usage_future.result()
	bandwidth_usage = bandwidth_usage_future.result()
	images_links = images_links_future.result()
	random.shuffle(images_links)

	return JSONResponse({
		"username": username,
		"storage_usage": storage_usage,
		"bandwidth_usage": bandwidth_usage,
		"images_links": images_links,
	})

def delete_image(link):
	url = API_EPS.get("storage-account-service/delete_image")
	data = {
		"link": link,
	}
	return utils.send_request(url, data)

def upload_image(username, file_base64):
	url = API_EPS.get("storage-account-service/upload_image")
	data = {
		"username": username,
		"file_base64": file_base64,
	}
	return utils.send_request(url, data)

# =====> HELPER FUNCTIONS

def get_images_links(username):
	url = API_EPS.get("storage-account-service/get_images_links")
	data = {"username": username}
	response = utils.send_request(url, data)
	if response.status_code == 200:
		images_links = json.loads(response.body).get("images_links")
		return images_links
	return None

def get_storage_usage(username):
	url = API_EPS.get("storage-monitor-service/get_storage_usage")
	data = {"username": username}
	response = utils.send_request(url, data)
	if response.status_code == 200:
		storage_usage = json.loads(response.body).get("storage_usage")
		return storage_usage
	return None

def get_bandwidth_usage(username):
	url = API_EPS.get("usage-monitor-service/get_bandwidth_usage")
	data = {"username": username}
	response = utils.send_request(url, data)
	if response.status_code == 200:
		bandwidth_usage = json.loads(response.body).get("bandwidth_usage")
		return bandwidth_usage
	return None


def verify_user(username, password):
	url = API_EPS["auth-service/verify_user"]
	data = {
		"username": username,
		"password": password,
	}
	return utils.send_request(url, data)

def create_user_in_auth_service(username, password):
	url = API_EPS["auth-service/create_user"]
	data = {
		"username": username,
		"password": password,
	}
	response = utils.send_request(url, data)
	return response

def create_user_in_storage_account_service(username, password):
	url = API_EPS["storage-account-service/create_user"]
	data = {
		"username": username,
	}
	response = utils.send_request(url, data)
	return response

def create_user(username, password):

	with ThreadPoolExecutor() as executor:
		# Execute the functions concurrently
		creater1_future = executor.submit(
			create_user_in_auth_service,
			username, password
		)
		creater2_future = executor.submit(
			create_user_in_storage_account_service,
			username, password
		)

	# Get results from the futures
	creater1_response = creater1_future.result()
	creater2_response = creater2_future.result()
	
	# Return any failed response
	if creater1_response.status_code == 200:
		return creater2_response
	return creater1_response
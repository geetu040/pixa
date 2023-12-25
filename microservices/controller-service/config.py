import os

SECRET_KEY = os.environ.get("PIXA_AUTH_SECRET_KEY")
ALGORITHM = os.environ.get("PIXA_AUTH_ALGORITHM")

API_EPS = {

	"auth-service/verify_user": "http://localhost:5000/verify_user",
	"auth-service/create_user": "http://localhost:5000/create_user",

	"storage-account-service/create_user": "http://localhost:5001/create_user",
	"storage-account-service/get_images_links": "http://localhost:5001/get_images_links",
	"storage-account-service/upload_image": "http://localhost:5001/upload_image",
	"storage-account-service/delete_image": "http://localhost:5001/delete_image",

	"storage-monitor-service/get_storage_usage": "http://localhost:8000/get_storage_usage",
	"usage-monitor-service/get_bandwidth_usage": "http://localhost:8001/get_bandwidth_usage",
}
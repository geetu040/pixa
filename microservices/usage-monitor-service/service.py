import json
from azure.storage.blob import BlobServiceClient
from fastapi.responses import JSONResponse
from datetime import datetime
import concurrent.futures
from config import CONNECTION_STRING, CONTAINER_NAME, STORAGE_NAME

account_url = "https://"+STORAGE_NAME+".blob.core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(container=CONTAINER_NAME)

def get_bandwidth_usage(username: str):
	"""
	Retrieves the bandwidth usage for the specified username.

	Parameters:
	- username (str): The username for which bandwidth usage is to be determined.

	Returns:
	- float: The amount of bandwidth used by the specified username in megabytes.
	"""

	try:
		# loading blobs
		blobs = container_client.list_blobs()
		blobs = [i.name for i in blobs]
		blobs = filter_blobs(blobs)

		# processing blobs
		downloaded = download_blobs(blobs)
		size = parse(username, downloaded)

		# returning valid response
		return JSONResponse({"bandwidth_usage": size})

	except Exception as e:
		print(e)
		return JSONResponse(str(e), 500)

def parse(username, downloaded):
	size = 0.0

	for logs in downloaded:
		for log in logs:
			log = json.loads(log)

			if log['operationName'] != "PutRange": continue
			if username not in log['uri']: continue

			size += log['properties']['requestBodySize']

	size = size / 1024**2
	return size

def download_blobs(blobs):
	return process_data_parallel(download_blob, blobs)

def download_blob(blob):
	return container_client.download_blob(blob).readall().decode("utf-8").splitlines()

def process_data_parallel(process_data, data):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = list(executor.map(process_data, data))
	return results

def filter_blobs(blobs):

	today = datetime.today()

	def filter_blob(blob):
		split = blob.split("/")
		ymd = split[-6:-3]
		ymd_cleaned = [int(i[2:]) for i in ymd]
		y, m, d = ymd_cleaned
		return (
			d == today.day
				and
			m == today.month
				and
			y == today.year
		)
	
	return list(filter(filter_blob, blobs))

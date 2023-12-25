from azure.storage.fileshare import ShareDirectoryClient
import uuid
import base64
from fastapi.responses import JSONResponse
from config import CONNECTION_STRING, SHARE_NAME, STORAGE_NAME, URL_SASTOKEN

URL_HOSTNAME = f"https://{STORAGE_NAME}.file.core.windows.net"

def _get_dir_client(dir):
    return ShareDirectoryClient.from_connection_string(CONNECTION_STRING, SHARE_NAME, dir)

def _get_url(dir, file_name):
    return f"{URL_HOSTNAME}/{SHARE_NAME}/{dir}/{file_name}{URL_SASTOKEN}"

def _extract_url(url):

    url = url.replace(URL_HOSTNAME, "")
    url = url.replace(SHARE_NAME, "")
    url = url.replace(URL_SASTOKEN, "")

    url = url.split("/")
    url = [i for i in url if i != ""]
    dir_name, file_name = url

    return dir_name, file_name

def create_user(username: str):
    try:
        dir_client = _get_dir_client(username)
        dir_client.create_directory()
        return JSONResponse("User Directory Created", 200)
    except Exception as e:
        return JSONResponse(str(e), 500)

def get_images_links(username: str):
    """
    Retrieves image URLs for the given username

    Parameters:
    - username (str): The input username.

    Returns:
    - List[str]: A list of strings representing image URLs.
    """

    try:
        dir_client = _get_dir_client(username)

        files = dir_client.list_directories_and_files()

        files = [i for i in dir_client.list_directories_and_files()]
        files = [file.name for file in files]
        files = [_get_url(username, file) for file in files]

        return JSONResponse({"images_links": files})
    except Exception as e:
        return JSONResponse(str(e), 500)

def upload_image(username: str, file_base64: str):
    try:
        dir_client = _get_dir_client(username)
        random_filename = str(uuid.uuid4()) + ".jpg"
        file_client = dir_client.get_file_client(random_filename)
        file_binary = base64.b64decode(file_base64)
        file_client.upload_file(file_binary)

        return JSONResponse("Uploaded")
    except Exception as e:
        return JSONResponse(str(e), 500)

def delete_image(link: str):

    try:
        dir, filename = _extract_url(link)

        dir_client = _get_dir_client(dir)
        file_client = dir_client.get_file_client(filename)

        file_client.delete_file()

        return JSONResponse("Deleted")
    except Exception as e:
        return JSONResponse(str(e), 500)
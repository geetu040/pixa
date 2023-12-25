from azure.storage.fileshare import ShareServiceClient
from fastapi.responses import JSONResponse
from config import *

file_service_client = ShareServiceClient(account_url=f"https://{STORAGE_ACCOUNT_NAME}.file.core.windows.net", credential=STORAGE_ACCOUNT_KEY)
share_client = file_service_client.get_share_client(SHARE_NAME)

def get_storage_usage(username: str):
    """
    Retrieves the storage usage for the specified username.

    Parameters:
    - username (str): The username for which storage usage is to be determined.

    Returns:
    - float: The amount of storage used by the specified username in megabytes.
    """

    try:
        print(username)

        # Specify the user's folderuser
        user_folder = f"{username}/"

        # Get the user's directory client
        user_directory_client = share_client.get_directory_client(user_folder)

        # Initialize total size
        total_size_bytes = 0.0

        # Iterate through files in the user's folder
        for file_item in user_directory_client.list_directories_and_files():
            total_size_bytes += file_item.size

        # Calculate total storage size in gigabytes
        total_size_mb = total_size_bytes / (1024 ** 2)

        return JSONResponse({"storage_usage": total_size_mb})

    except Exception as e:
        return JSONResponse(str(e), 500)
import os

# for connection to azure file storage client
CONNECTION_STRING = os.environ.get("PIXA_STORAGE_CONNECTION_STRING")

# storage
STORAGE_NAME = os.environ.get("PIXA_STORAGE_STORAGE_NAME")

# share in azure file storage
SHARE_NAME = os.environ.get("PIXA_STORAGE_SHARE_NAME")

# this is the SAS Token
URL_SASTOKEN = os.environ.get("PIXA_STORAGE_URL_SASTOKEN")
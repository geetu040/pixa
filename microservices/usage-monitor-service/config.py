import os

# for connection to azure file storage client
CONNECTION_STRING = os.environ.get("PIXA_STORAGELOGS_CONNECTION_STRING")

# storage
STORAGE_NAME = os.environ.get("PIXA_STORAGELOGS_STORAGE_NAME")

# share in azure file storage
CONTAINER_NAME = os.environ.get("PIXA_STORAGELOGS_CONTAINER_NAME")

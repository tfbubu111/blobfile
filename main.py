import os

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

def main():
token_credential = DefaultAzureCredential()

blob = BlobClient(
        account_url="https://privatesaforaks.blob.core.windows.net/testforsa",
        credential=token_credential
    )


with open("./BlockDestination.txt", "wb") as my_blob:
    blob_data = blob.download_blob()
    blob_data.readinto(my_blob)
	
if __name__ == '__main__':
    main()

import os
from dotenv import load_dotenv
from google.cloud import storage
import pandas as pd

# Load environment variables from .env file
load_dotenv()


BUCKET_NAME = os.getenv('BUCKET_NAME')
SOURCE_BLOB_NAME = os.getenv('SOURCE_BLOB_NAME')


load_dotenv()
project = os.getenv('GOOGLE_CLOUD_PROJECT')

storage_client = storage.Client(project=project)

# Get the bucket
bucket = storage_client.bucket(BUCKET_NAME)

# Get the blob (file) from the bucket
blob = bucket.blob(SOURCE_BLOB_NAME)

# Define the local file path to save the downloaded file
local_file_path = 'downloaded_data.csv'

# Download the file to the local filesystem
try:
    blob.download_to_filename(local_file_path)
    print(f"File {SOURCE_BLOB_NAME} downloaded to {local_file_path}.")
except Exception as e:
    print(f"Error downloading file: {e}")

# Load the file into a Pandas DataFrame for further processing
try:
    df = pd.read_csv(local_file_path)
    print("DataFrame head:")
    print(df.head())
except Exception as e:
    print(f"Error reading CSV: {e}")
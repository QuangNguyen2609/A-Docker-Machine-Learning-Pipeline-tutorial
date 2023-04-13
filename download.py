from pathlib import Path
from google.cloud import storage
gcs_client = storage.Client()
bucket = gcs_client.bucket('mle-class-storage')

import os 
# export GOOGLE_APPLICATION_CREDENTIALS=./dummy-mles.json
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./dummy-mles.json'

import schedule
import time

import os

from google.cloud import storage
gcs_client = storage.Client()
bucket = gcs_client.bucket('mle-class-storage')

from pathlib import Path
blobs = bucket.list_blobs()

def download_data():
  for blob in blobs:
      if blob.exists():
          filename = blob.name
          if filename.endswith("/"):
            continue
          file_split = filename.split("/")
          print(file_split)
          directory = "/".join(file_split[0:-1])
          Path(directory).mkdir(parents=True, exist_ok=True)
          print('Downloading {} from GCS'.format(filename))
          blob.download_to_filename(filename) 
          print('Downloaded {} from GCS'.format(filename))

# schedule.every(1).minutes.do(download_data)

# while True:
#   schedule.run_pending()
#   time.sleep(1)
  
download_data()
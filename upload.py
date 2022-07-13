"""
from gcloud import storage

client = storage.Client()
bucket = client.get_bucket('notification_pubsub')
blob = bucket.blob('my-test-file.png')
# Uploading from local file without open()
blob.upload_from_filename('kitten.png')
"""

import os
from gcloud import storage
project_id = 'pub-sub-672022' 
bucket_name = 'notification_pubsub' 
bucket_file = 'kitten.png' 
local_file = 'kitten.png'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'pub-sub-672022-b4dde19e12bf.json'
# Initialise a client
client = storage.Client(project_id)# Create a bucket object for our bucket
bucket = client.get_bucket(bucket_name)# Create a blob object from the filepath
blob = bucket.blob(bucket_file)# Upload the file to a destination
blob.upload_from_filename(local_file)
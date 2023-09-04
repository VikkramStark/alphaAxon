from google.cloud import storage 
import os 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "lipnet-dataset-gcs.json" 

storage_client = storage.Client() 

bucket_name = "lipnet-bucket" 

assets = "assets/"  
dataset = "processed_dataset/" 

bucket = storage_client.get_bucket(bucket_name) 

blobs = bucket.list_blobs(prefix = assets) 

logo = bucket.get_blob("assets/alphaAxon.png")  

# [ print(blob.name) for blob in blobs ]  

# print(logo) 
# print(logo.download_as_bytes())    


def get_logo():
    img = bucket.get_blob("assets/alphaAxon.png") 
    return img.download_as_bytes()  

def list_dataset():
    blobs = bucket.list_blobs(prefix = dataset)   
    return [blob.name.split("/")[1] for blob in blobs] 

def get_video(video_name):
    blob = bucket.get_blob(dataset+video_name) 
    return blob.download_as_bytes()   


     


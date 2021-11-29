from io import StringIO
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from view import get_view,get_upload_file_view
#from azure.storage.blob import BlockBlobService
from azure.storage.blob import BlobServiceClient
#from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import __version__
# from azure.identity import ClientSecretCredential
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
# import string, random, requests
import pandas as pd
# import timeit
# import csv
#import os, uuid


app = Flask(__name__)

keyVaultName = 'EUE-BI-MLPlatform-KV-PPE'

#key vault name as an environment variable called KEY_VAULT_NAME. Optionally a name of the vault can be here : heck2021ml9859723739
KVUri = f"https://{keyVaultName}.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
key = client.get_secret("EUE-ML-Blob-Access-Key")
account = client.get_secret("euebimlplatform-storage-name")
connection_string = client.get_secret("EUE-ML-Blob-ConnectionString")
key = key.value
account = account.value
connection_string = connection_string.value

#account = 'heck2021ml9709306933'   # Azure account name
#key = 'nJuffKTB7A9UgzZtzllerpYvJch3pJNthxy9Ro89VNTRqq3C0vePegGi4ndT2a/zwvFA+wCBaJNTVbgRoBJbew=='     # Azure Storage account access key
#connection_string = "DefaultEndpointsProtocol=https;AccountName=heck2021ml9709306933;AccountKey=nJuffKTB7A9UgzZtzllerpYvJch3pJNthxy9Ro89VNTRqq3C0vePegGi4ndT2a/zwvFA+wCBaJNTVbgRoBJbew==;EndpointSuffix=core.windows.net"
container = 'setaselfserve' # Container name
blob_service = BlobServiceClient.from_connection_string(connection_string)
container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name = container)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in 'csv'

@app.route('/', methods=['POST','GET'])
def upload_file_to_blob():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            blob_client = blob_service.get_blob_client(container = container, blob = filename)
            with open(filename, "rb") as data:
                try:
                    blob_client.upload_blob(data, overwrite=True)
                except:
                    pass
 #           os.remove(filename)
        ref =  'http://'+ account + '.blob.core.windows.net/' + container + '/' + filename
        return '''
	    <!doctype html>
	    <title>File Link</title>
	    <h1>Uploaded File Link</h1>
	    <p>''' + str(ref) + '''</p>
	    <img src="'''+ ref +'''">
	    '''
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload File to Blob</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


def get_blob():
    blob_list = container_client.list_blobs()
    sorted_blob_list = sorted(blob_list,key=lambda x: x.creation_time, reverse=True)
    return sorted_blob_list[0].name
def schema_check():
    blob_name = get_blob()
    print(blob_name)
    blob_string = container_client.download_blob(blob_name).content_as_text()
    df = pd.read_csv(StringIO(blob_string))
    shape = df.shape
    try:
        assert (shape[1]==5), "The number of columns in the dataset needs to be equal to 3#################################################################"
    except Exception as e:
        print(e)
        container_client.delete_blobs(blob_name)
        listing_blobs()

blob_list=[]
def listing_blobs():
        try:

                global blob_list
                content = container_client.list_blobs()
                print("******Blobs currently in the container:**********")
                for blob in content:
                        blob_list.append(blob.name)
                        print(blob.name)
        except:
                print("The specified container does not exist, Please check the container name or if it exists.")

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')

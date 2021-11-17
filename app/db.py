from app import app
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import json

with open('./secrets.json') as data_file:
    cloudant_creds = json.load(data_file)

CLOUDANT_URL = cloudant_creds['url']
CLOUDANT_APIKEY = cloudant_creds['apikey']
CLOUDANT_USERNAME = cloudant_creds['username']
DB_NAME = "dev-aw" # eco-db

app.config['CLOUDANT_URL'] = cloudant_creds['url']

authenticator = IAMAuthenticator(CLOUDANT_APIKEY)

client = CloudantV1(authenticator=authenticator)

client.set_service_url(CLOUDANT_URL)

# Get all documents
def get_docs():
    all_docs_data = client.post_all_docs(
    db=DB_NAME,
    include_docs=True,
    ).get_result()

    return all_docs_data['rows']

# Post document
def post_doc(document):
    client.post_document(db=DB_NAME, document=document)

# Delete document (by id)
def delete_doc(doc_id_to_delete):
    document = client.get_document(
        db=DB_NAME,
        doc_id=doc_id_to_delete
    ).get_result()

    client.delete_document(
        db=DB_NAME,
        doc_id=document["_id"],
        rev=document["_rev"]
    )
from ibmcloudant.cloudant_v1 import CloudantV1, AllDocsQuery
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import json

with open('./secrets.json') as data_file:
    cloudant_creds = json.load(data_file)

CLOUDANT_URL = cloudant_creds['url']
CLOUDANT_APIKEY = cloudant_creds['apikey']
CLOUDANT_USERNAME=cloudant_creds['username']
DB_NAME = "eco-db"

authenticator = IAMAuthenticator(CLOUDANT_APIKEY)

client = CloudantV1(authenticator=authenticator)

client.set_service_url(CLOUDANT_URL)

server_information = client.get_server_information().get_result()


# Post Document
test_doc = {
    "name" : "testing",
    "are_you_ok" : "yes"
    }

post_response = client.post_document(db=DB_NAME, document=test_doc).get_result()

print(post_response)
print()

# Get all documents
all_docs_result = client.post_all_docs(
  db=DB_NAME,
  include_docs=True,
  limit=10
).get_result()

print()
print(all_docs_result)
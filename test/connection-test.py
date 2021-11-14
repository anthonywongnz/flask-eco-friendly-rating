from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

import datetime

import json

with open('./secrets.json') as data_file:
    cloudant_creds = json.load(data_file)
CLOUDANT_URL = cloudant_creds['url']
CLOUDANT_APIKEY = cloudant_creds['apikey']
CLOUDANT_USERNAME = cloudant_creds['username']
DB_NAME = "eco-db"

authenticator = IAMAuthenticator(CLOUDANT_APIKEY)

client = CloudantV1(authenticator=authenticator)

client.set_service_url(CLOUDANT_URL)


# Post Document
test_doc = {
    "name" : "Gordon Hamsey's Fancy Resaurant",
    "category":"fine dining",
    "packaging" : "plastic",
    "city": "Auckland",
    "insert_datetime": datetime.datetime.now()
    }

# post_response = client.post_document(db=DB_NAME, document=test_doc).get_result()
# print(post_response)
# print()

# Get all documents
all_docs_result = client.post_all_docs(
  db=DB_NAME,
  include_docs=True,
  limit=10
).get_result()

all_docs = all_docs_result['rows']

# print(all_docs)

for id in all_docs:
  print(id['doc'])
  # print(id['doc']['name'])

print()

# Delete document by id

example_doc_id = '701edff2f1a2916ea7a7efc08613b3f4'

get_document_response = client.get_document(
    db=DB_NAME,
    doc_id=example_doc_id
).get_result()

print(get_document_response)

print()

# client.delete_document(db=DB_NAME, doc_id=example_doc_id)

try:
    document = client.get_document(
        db=DB_NAME,
        doc_id='701edff2f1a2916ea7a7efc08613b3f4'
    ).get_result()

    delete_document_response = client.delete_document(
        db=DB_NAME,
        doc_id=document["_id"],
        rev=document["_rev"]
    ).get_result()

    if delete_document_response["ok"]:
        print('You have deleted the document.')

except ApiException as ae:
    if ae.code == 404:
        print('Cannot delete document because either ' +
              f'"{DB_NAME}" database or "{example_doc_id}"' +
              'document was not found.')
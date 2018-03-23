#------------------------------------------------------------------------------
# Get the dominant prints for an image in the catalog.
# GET /v1/catalog/{catalog_name}/dominant_prints/{id}/{image_id}
#------------------------------------------------------------------------------

import os
import json
import requests
from urlparse import urljoin
from pprint import pprint

from props import *

# Replace this with the custom url generated for you.
api_gateway_url = props['api_gateway_url']

# Pass the api key into the header
# Replace 'your_api_key' with your API key.
headers = {'X-Api-Key': props['X-Api-Key']}

# Catalog name.
catalog_name = props['catalog_name']

id ='SHRES16AWFSDR9346B'
image_id = '2'

api_endpoint = '/v1/catalog/%s/dominant_prints/%s/%s'%(catalog_name,id,image_id)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,headers=headers)

print response.status_code
pprint(response.json())


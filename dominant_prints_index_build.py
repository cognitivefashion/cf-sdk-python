#------------------------------------------------------------------------------
# Build the dominant prints index.
# POST /v1/catalog/{catalog_name}/dominant_prints_index
# params - prints,max_prints_per_image,fraction_boxes_threshold
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

params = {}

# Optional parameters.
params['prints'] = 10
params['max_prints_per_image'] = 2
params['fraction_boxes_threshold'] = 0.1

# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/dominant_prints_index'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.post(url,headers=headers,params=params)

print response.status_code
pprint(response.json())


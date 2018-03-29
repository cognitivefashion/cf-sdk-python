#------------------------------------------------------------------------------
# Build the looks search index.
# POST /v1/catalog/{catalog_name}/looks_search_index
#------------------------------------------------------------------------------

import os
import json
import requests
from urlparse import urljoin
from pprint import pprint

from props import *

# Replace this with the custom url generated for you.
api_gateway_url = props['api_gateway_url']

# Pass the api key into the header.
headers = {'X-Api-Key': props['X-Api-Key']}

# Query parameters.
params = {}
# Optional parameters.
#params['image_max_dimension'] = 512
params['ignore_background'] = 'true'
params['model'] = 'person_fast'
#params['ignore_images_without_person'] = 'true'

# Path paarameters.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/looks_search_index'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.post(url,headers=headers,params=params)

print response.status_code
pprint(response.json())


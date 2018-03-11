#------------------------------------------------------------------------------
# Build the color search index.
# POST /v1/catalog/{catalog_name}/color_search_index
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
params['color_count'] = 3
params['quality'] = 1
params['image_max_dimension'] = 256
params['ignore_background'] = 'true'
params['model'] = 'person_fast'
params['fraction_pixels_threshold'] = 0.1

# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/color_search_index'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.post(url,headers=headers,params=params)

print response.status_code
pprint(response.json())


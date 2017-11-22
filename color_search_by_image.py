#------------------------------------------------------------------------------
# Get similar color images in the catalog for a given uploaded image.
# GET /v1/catalog/{catalog_name}/color_search
# params - color_count,image_max_dimension,max_number_of_results
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

# Parameters.
params = {}
params['color_count'] =  1
params['max_number_of_results'] = 5

headers['Content-Type'] = 'image/jpeg'

# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/color_search'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,
                        headers=headers,
                        params=params,
                        data=open('test_image_2.jpeg','rb'))

print response.status_code
pprint(response.json())


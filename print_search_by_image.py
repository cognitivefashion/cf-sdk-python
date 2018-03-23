#------------------------------------------------------------------------------
# Get similar image/print swatches in the catalog for a user uploaded image.
# POST /v1/catalog/{catalog_name}/print_search
# params - print_count,image_max_dimension,max_number_of_results
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
params['print_count'] =  1
params['max_number_of_results'] = 5
#params['image_max_dimension'] = 512

headers['Content-Type'] = 'image/jpeg'

# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/print_search'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.post(url,
                        headers=headers,
                        params=params,
                        data=open('test_image_1.jpeg','rb'))

print response.status_code
pprint(response.json())


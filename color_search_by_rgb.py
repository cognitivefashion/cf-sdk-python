#------------------------------------------------------------------------------
# Get similar color images in the catalog for a specified RGB value.
# GET /v1/catalog/{catalog_name}/color_search
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

# Parameters.
params['r'] = 179
params['g'] = 80
params['b'] = 54
params['max_number_of_results'] = 5


# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/color_search'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,
                        headers=headers,
                        params=params)


print response.status_code
pprint(response.json())


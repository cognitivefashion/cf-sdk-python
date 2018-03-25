#------------------------------------------------------------------------------
# Delete product from a catalog.
# DELETE /v1/catalog/{catalog_name}/products/{id}
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

# Product id.
id = '20DRA16FWCWHL9012909'

# Parameters
params = {}
params['api_key'] = props['X-Api-Key']

# API end point.
api_endpoint = '/v1/images'

url = urljoin(api_gateway_url,api_endpoint)

"""
response = requests.get(url,
                        headers=headers,
                        params=params)

print response.status_code
pprint(response.json())
"""

headers['Content-Type'] = 'image/jpeg'
response = requests.post(url,
                        headers=headers,
                        params=params,
                        data=open('test_image_1.jpeg','rb'))

print response.status_code
print response.headers['location']
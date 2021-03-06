#------------------------------------------------------------------------------
# Get the dominant prints for all images in the catalog.
# GET /v1/catalog/{catalog_name}/dominant_prints
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
params['prints'] = 5

# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/dominant_prints'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,headers=headers,params=params)

print response.status_code
pprint(response.json())

# Here is how you can serve the print swatches
results = response.json()
for print_info in results['dominant_prints']:
    print_swatch = '%s&api_key=%s'%(urljoin(api_gateway_url,print_info['image_location']),
                                    props['X-Api-Key'])
    print('[print swatch] %s'%(print_swatch)) 
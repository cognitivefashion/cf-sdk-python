#------------------------------------------------------------------------------ 
# Get similar looks in the catalog for an existing image.
# GET /v1/catalog/{catalog_name}/looks_search
# params - id,image_id,max_number_of_results
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
params['id'] = 'SHRES16AWFSDR9346A' 
params['image_id'] = '1'
params['max_number_of_results'] = 3

# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/looks_search'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,
                        headers=headers,
                        params=params)


print response.status_code
pprint(response.json())

# Human friendly repsonse.

results = response.json()

for info in results['products']:
    person_image = '%s&api_key=%s'%(urljoin(api_gateway_url,info['image_location']),
                                    props['X-Api-Key'])
    print('[%1.2f] %s'%(info['similarity'],person_image)) 


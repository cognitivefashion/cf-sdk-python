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

# Pass the api key into the header.
headers = {'X-Api-Key': props['X-Api-Key']}

# Query parameters.
params = {}
# Optional parameters.
#params['fraction_boxes_threshold'] = 0.1

# Path parameters
catalog_name = props['catalog_name']
id ='SHRES16AWFSDR9346B'
image_id = '1'

api_endpoint = '/v1/catalog/%s/dominant_prints/%s/%s'%(catalog_name,id,image_id)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,
                        headers=headers,
                        params=params)

print response.status_code
pprint(response.json())

# Human friendly repsonse.

results = response.json()

print('[image url      ] %s'%(results['image_url']))

image_location = '%s?api_key=%s'%(urljoin(api_gateway_url,results['image_location']),
                                  props['X-Api-Key'])
print('[original image ] %s'%(image_location))

image_location = '%s&api_key=%s'%(urljoin(api_gateway_url,results['bounding_box']['image_location']),
                                  props['X-Api-Key'])
print('[bounding box   ] %s'%(image_location))

for print_info in results['dominant_prints']:
    print_swatch = '%s&api_key=%s'%(urljoin(api_gateway_url,print_info['image_location']),
                                    props['X-Api-Key'])
    print('[dominant prints] %1.2f %s'%(print_info['fraction_boxes'],print_swatch)) 
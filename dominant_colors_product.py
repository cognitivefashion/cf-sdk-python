#------------------------------------------------------------------------------
# Get the dominant colors for an image in the catalog.
# GET /v1/catalog/{catalog_name}/dominant_colors/{id}/{image_id}
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
#params['fraction_pixels_threshold'] = 0.1

# Path parameters
catalog_name = props['catalog_name'] 
id ='SHRES16AWFSDR9346B' 
image_id = '1'

api_endpoint = '/v1/catalog/%s/dominant_colors/%s/%s'%(catalog_name,id,image_id)

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

for color_info in results['dominant_colors']:
    print('[dominant colors] %s - %1.2f - %s - %s - %s - %s'%(color_info['hex'],
                                  color_info['fraction_pixels'],
                                  color_info['name'],
                                  color_info['entrylevel_name'],
                                  color_info['universal_name'],
                                  color_info['pantone_id']))

#------------------------------------------------------------------------------
# Get similar looks in the catalog for a user uploaded image.
# POST /v1/catalog/{catalog_name}/looks_search
# params - max_number_of_results,ignore_background,model,image_max_dimension
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
params['max_number_of_results'] = 3
#params['image_max_dimension'] = 512
params['ignore_background'] = 'true'
params['model'] = 'person_fast'

headers['Content-Type'] = 'image/jpeg'

# Catalog name.
catalog_name = props['catalog_name']

api_endpoint = '/v1/catalog/%s/looks_search'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.post(url,
                        headers=headers,
                        params=params,
                        data=open('test_image_3.jpeg','rb'))

print response.status_code
pprint(response.json())

# Human friendly repsonse.

results = response.json()

image_location = '%s?api_key=%s'%(urljoin(api_gateway_url,results['image_location']),
                                  props['X-Api-Key'])
print('[original image ] %s'%(image_location))

image_location = '%s&api_key=%s'%(urljoin(api_gateway_url,results['bounding_box']['image_location']),
                                  props['X-Api-Key'])
print('[bounding box   ] %s'%(image_location))

for info in results['products']:
    person_image = '%s&api_key=%s'%(urljoin(api_gateway_url,info['image_location']),
                                    props['X-Api-Key'])
    print('[%1.2f] %s'%(info['similarity'],person_image)) 
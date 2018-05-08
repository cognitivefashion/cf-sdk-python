#------------------------------------------------------------------------------
# Get visual attributes for a given iconic/non-iconic image.
# GET /v1/visualattributes
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
# Optional parameters.
params['threshold'] = 0.32
#params['image_type'] = 'iconic'
params['image_type'] = 'non-iconic'

api_endpoint = '/v1/visualattributes'

url = urljoin(api_gateway_url,api_endpoint)

# Three options to pass the image

# OPTION 1 : Directly post the image
headers['Content-Type'] = 'image/jpeg'
response = requests.post(url,
                         headers=headers,
                         params=params,
                         data=open('test_image_2.jpeg','rb'))

"""            
# OPTION 2 : Pass the image url
params['image_url'] = 'http://vg-images.condecdn.net/image/oDXPOxw65EZ/crop/405'
response = requests.post(url,
                         headers=headers,
                         params=params)
"""

"""
# OPTION 3 : using multipart
image_filename = 'test_image_1.jpeg'
with open(image_filename,'rb') as images_file:
    response = requests.post(url,
                             headers=headers,
                             params=params,
                             files={'image': (image_filename,images_file,'image/jpeg')})   
"""

print response.status_code
pprint(response.json())

# Human friendly repsonse.

results = response.json()

image_location = '%s?api_key=%s'%(urljoin(api_gateway_url,results['image_location']),
                                  props['X-Api-Key'])
print('[original image] %s'%(image_location))

for entity in results['entities']:
    entity_swatch = '%s&api_key=%s'%(urljoin(api_gateway_url,entity['image_location']),
                                    props['X-Api-Key'])
    print('[%1.2f][%s][%s]'%(entity['category']['score'][entity['category']['value']],
                                     entity['category']['value'],
                                     entity_swatch)) 
    if 'attributes' in entity:
        for attribute in entity['attributes']:
            print('[%1.2f][%s][%s]'%(entity['attributes'][attribute]['score'][entity['attributes'][attribute]['value']],
                                     attribute,
                                     entity['attributes'][attribute]['value']))

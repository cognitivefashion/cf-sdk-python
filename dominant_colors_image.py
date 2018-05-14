#------------------------------------------------------------------------------
# Dominant Colors for an user uploaded image. 
# POST /v1/colors/dominant_colors
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

params = {}
# Optional parameters.
params['color_count'] = 5
params['quality'] = 1
#params['image_max_dimension'] = 256
params['ignore_background'] = 'true'
#params['model'] = 'person_accurate'
params['model'] = 'person_fast'
params['fraction_pixels_threshold'] = 0.1

api_endpoint = '/v1/colors/dominant_colors'

url = urljoin(api_gateway_url,api_endpoint)

# Three options to pass the image

# OPTION 1 : Directly post the image
headers['Content-Type'] = 'image/jpeg'
response = requests.post(url,
                         headers=headers,
                         params=params,
                         data=open('test_image_2.jpeg','rb'))

       
# OPTION 2 : Pass the image url
""""
params['image_url'] = 'https://vg-images.condecdn.net/image/oDXPOxw65EZ/crop/405'
response = requests.post(url,
                         headers=headers,
"""


# OPTION 3 : using multipart
"""
image_filename = 'test_image_2.jpeg'
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
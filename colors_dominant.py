#------------------------------------------------------------------------------
# Dominant color palette. 
# POST /v1/colors/image_color_palette
#------------------------------------------------------------------------------

import os
import json
import requests
from urlparse import urljoin

from props import *

# Replace this with the custom url generated for you.
api_gateway_url = props['api_gateway_url']

# Pass the api key into the header
# Replace 'your_api_key' with your API key.
headers = {'X-Api-Key': props['X-Api-Key']}

api_endpoint = '/v1/colors/image_color_palette'

url = urljoin(api_gateway_url,api_endpoint)

headers['Content-Type'] = 'image/jpeg'

response = requests.post(url,headers=headers,data=open('test_image_2.jpeg','rb'))

print response.status_code
print response.json()

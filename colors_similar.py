#------------------------------------------------------------------------------
# Get similar colors. 
# GET /v1/colors/similar_colors
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

api_endpoint = '/v1/colors/similar_colors'

url = urljoin(api_gateway_url,api_endpoint)

params = {}
params['color_term'] = 'purple'

# Optional parameters
#params['color_family'] = 'full'

response = requests.get(url,headers=headers,params=params)

print response.status_code
pprint(response.json())


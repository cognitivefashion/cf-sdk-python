#------------------------------------------------------------------------------
# Get color terms. 
# GET /v1/colors/color_terms
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

api_endpoint = '/v1/colors/color_terms'

url = urljoin(api_gateway_url,api_endpoint)

# Parameters - required
params = {}
params['r'] = 106
params['g'] = 103
params['b'] = 95

# Parameters - optional
params['color_count'] = 3
params['color_family'] = 'full'
#params['color_family'] = 'universal'
#params['color_family'] = 'entrylevel'
#params['color_family'] = 'pantone'
params['method'] = 'accurate'
#params['method'] = 'fast'

response = requests.get(url,
                        headers=headers,
                        params=params)

print response.status_code
pprint(response.json())



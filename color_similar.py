#------------------------------------------------------------------------------
# Get other color terms similar to a given color term.
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

# Pass the api key into the header.
headers = {'X-Api-Key': props['X-Api-Key']}

api_endpoint = '/v1/colors/similar_colors'

url = urljoin(api_gateway_url,api_endpoint)

params = {}
params['color_term'] = 'purple'

# Optional parameters
params['color_count'] = 3
#params['color_family'] = 'universal'
#params['color_family'] = 'entrylevel'
#params['color_family'] = 'full'

# To serch within the pantone family
#params['color_term'] = 'pantone 19-3336 tcx sparkling grape'
#params['color_family'] = 'pantone'

response = requests.get(url,headers=headers,params=params)

print response.status_code
pprint(response.json())


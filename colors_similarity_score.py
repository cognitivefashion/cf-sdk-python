#------------------------------------------------------------------------------
# Get similarity score between two color terms. 
# GET /v1/colors/color_terms_similarity
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

api_endpoint = '/v1/colors/color_terms_similarity'

url = urljoin(api_gateway_url,api_endpoint)

params = {}
params['color_term_1'] = 'red'
params['color_term_2'] = 'pink'

response = requests.get(url,
                        headers=headers,
                        params=params)

print response.status_code
pprint(response.json())


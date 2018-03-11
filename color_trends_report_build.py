#------------------------------------------------------------------------------
# Start computing the color trend report.
# POST /v1/color_trends/{report_name}/trend_report
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

params = {}

# Pass the catalog names as a comma separated list of names.
catalog_names = []
catalog_names.append('vogue-autumn-winter-2014')
catalog_names.append('vogue-autumn-winter-2015')
catalog_names.append('vogue-autumn-winter-2016')
catalog_names.append('vogue-autumn-winter-2017')
params['catalog_names'] = ','.join(catalog_names)

# Optional parameters.
params['colors'] = 10
params['max_colors_per_image'] = 2
params['fraction_pixels_threshold'] = 0.1

report_name = 'vogue-autumn-winter'

api_endpoint = '/v1/color_trends/%s/trend_report'%(report_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.post(url,headers=headers,params=params)

print response.status_code
pprint(response.json())


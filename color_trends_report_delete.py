#------------------------------------------------------------------------------
# Delete the color trend report.
# DELETE /v1/color_trends/{report_name}/trend_report
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

report_name = 'vogue-autumn-winter'

api_endpoint = '/v1/color_trends/%s/trend_report'%(report_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.delete(url,headers=headers)

print response.status_code
pprint(response.json())




#------------------------------------------------------------------------------
# Get the trending colors.
# GET /v1/color_trends/{report_name}/trending_colors
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
params['colors'] = 20
# Optional
#params['catalog_name'] = 'vogue-autumn-winter-2017'

report_name = 'vogue-autumn-winter'

api_endpoint = '/v1/color_trends/%s/trending_colors'%(report_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.get(url,headers=headers,params=params)

print response.status_code
pprint(response.json())

# Print the colors.
results = response.json()
years = ['2013','2014','2015','2016','2017']
for color_info in results['colors']:
    print('popularity [%s] [%+1.2f] trend [%s] [%+1.2f] [%s]'%(
                          ' '.join(['%1.2f'%(color_info['popularity_by_id']['%s-%s'%(report_name,year)]) for year in years]),
                          color_info['popularity_forecast']['mean'],
                          ' '.join(['%+1.2f'%(color_info['trend_by_id']['%s-%s'%(report_name,year)]) for year in years]),
                          color_info['trend_forecast']['mean'],
                          color_info['pantone_id']))



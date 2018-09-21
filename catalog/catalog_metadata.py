#------------------------------------------------------------------------------
# Add metadata to a catalog.    
# POST /v1/catalog/{catalog_name}
#------------------------------------------------------------------------------

import os
import json
import requests
from urlparse import urljoin
from pprint import pprint

from props import *

#------------------------------------------------------------------------------
# API URL
#------------------------------------------------------------------------------
api_gateway_url = props['api_gateway_url']

#------------------------------------------------------------------------------
# HEADERS
#------------------------------------------------------------------------------
headers = {}
# API key
headers['X-Api-Key'] = props['X-Api-Key']
# Data collection opt out.
headers['X-Data-Collection-Opt-Out'] = props['X-Data-Collection-Opt-Out']

#------------------------------------------------------------------------------
# OPTIONAL QUERY PARAMETERS
#------------------------------------------------------------------------------
params = {}

#------------------------------------------------------------------------------
# PATH PARAMETERS
#------------------------------------------------------------------------------
# Catalog name.
catalog_name = props['catalog_name']

#------------------------------------------------------------------------------
# Metadata
# Post any metadata you want to track for the catalog. Suggested fields
#------------------------------------------------------------------------------
data={}
#A friendly name for display purposes.
data['friendly_name'] = 'sample' 
# The url of the hero image.
data['hero_image_url'] = 'https://cognitivefashion.github.io/img/portfolio/logo_cf.svg' 
# A brief description.
data['description'] = 'A sample catalog to test IBM Research AI for Fashion APIs.' 

#------------------------------------------------------------------------------
# API END POINT
#------------------------------------------------------------------------------
api_endpoint = 'v1/catalog/%s'%(catalog_name)

url = urljoin(api_gateway_url,api_endpoint)

response = requests.post(url,
                         headers=headers,
                         params=params,
                         json=data)

print response.status_code
pprint(response.json())

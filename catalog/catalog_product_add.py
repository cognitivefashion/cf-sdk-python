#------------------------------------------------------------------------------
# Add product to a catalog.    
# POST /v1/catalog/{catalog_name}/products/{id}
# params - download_images
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
# download_images : str, optional (default: 'true') 
# By default all the images in the json will be downloaded.  
# Set this to 'false' if you do not want to download the images.  
# This is mainly useful when we have a local copy of the images.
#------------------------------------------------------------------------------
params['download_images'] = 'true'

#------------------------------------------------------------------------------
# PATH PARAMETERS
#------------------------------------------------------------------------------
# Catalog name.
catalog_name = props['catalog_name']

#------------------------------------------------------------------------------
# ADD A BUNCH OF PRODUCTS
#------------------------------------------------------------------------------

# Some sample data where each product in the catalog is in a json format.
catalog_folder = os.path.join(props['catalog_folder'],'jsons')
json_filenames = [f for f in os.listdir(catalog_folder) if not f.startswith('.')]

for filename in json_filenames:
    # Load the json file.
    with open(os.path.join(catalog_folder,filename),'r') as f:
        data = json.loads(f.read())
        
    api_endpoint = '/v1/catalog/%s/products/%s'%(catalog_name,data['id'])

    url = urljoin(api_gateway_url,api_endpoint)
    
    response = requests.post(url,
                             headers=headers,
                             data=json.dumps(data),
                             params=params)
    
    print response.status_code
    pprint(response.json())


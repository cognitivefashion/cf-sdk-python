#------------------------------------------------------------------------------
# Add product to a catalog.    
# POST /v1/catalog/{catalog_name}/products/{id}
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

# You need to give a name to your catalog.
catalog_name = 'sample_catalog'

# Some sample data where each product in the catalog is in a json format
# described earlier.
catalog_folder = 'sample_catalog'
json_filenames = [f for f in os.listdir(catalog_folder) if not f.startswith('.')]

params = {}
# Optional parameters.
params['download_images'] = 'true'
params['ignore_detail_images'] = 'true'

for filename in json_filenames:
    # load the json file
    with open(os.path.join(catalog_folder,filename),'r') as f:
        data = json.loads(f.read())

    api_endpoint = '/v1/catalog/%s/products/%s'%(catalog_name,data['id'])
    url = urljoin(api_gateway_url,api_endpoint)
    
    response = requests.post(url,
                             headers=headers,
                             json=data,
                             params=params)
    
    print response.status_code
    print response.json()


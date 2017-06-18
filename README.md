# cf-sdk-python

Python examples using [requests](http://docs.python-requests.org/en/master/) for the [IBM Research Cognitive Fashion APIs](http://irlbxvm137.irl.in.ibm.com:4567/).

## Sign up for IBM Research Cognitive Fashion 

https://www.ibm.com/us-en/marketplace/8075

Once you sign up you will get a custom url and an API key.

## API slate documentation

https://cognitivefashion.github.io/slate/

## Getting started

Make changes to `props.py` with your url and API key.

You can also change the catalog name.

    props = {}
    
    # Replace this with the custom url generated for you.
    props['api_gateway_url'] = 'http://localhost:9080'
    
    # Replace 'your_api_key' with your API key.
    props['X-Api-Key'] = 'your_api_key'

    # You need to give a name to your catalog.
    # The sample scripts read the json files from this folder.
    props['catalog_name'] = 'sample_catalog'    


Run `fashion_quote.py` to ensure that your custom api url and the API key is working.

## Catalog ingestion and management

1. Add products to a catalog (`catalog_add_product.py`).
1. Update product in a catalog (`catalog_update_product.py`).
1. Get product from a catalog (`catalog_get_product.py`).
1. Delete product from a catalog. (`catalog_delete_product.py`).
1. Get info about a product catalog (`catalog_info.py`).
1. Delete a product catalog (`catalog_delete.py`).

## Visual Browse and Visual Search

1. Build the visual search index (`visual_search_index_build.py`).
1. Building the index takes some time. Check the status (`visual_search_index_status.py`).
1. Get other visually similar products in the catalog (`visual_browse.py`). 
1. Get visually similar products in the catalog for an uploaded image (`visual_search.py`).
1. Delete the visual search index (`visual_search_index_delete.py`).

## Natural Language Search

1. Natural Language Search (`natural_language_search.py`).
2. elasticsearch queries (`elasticsearch_queries`). 
3. Parse fashion query/text (`fashion_query_parse`). 
4. Get search terms (`fashion_query_search_terms`). 
5. Spelling correction (`fashion_query_spell_correct`). 

## Colors

1. Get color terms (`colors_terms.py`). 
2. Get similar colors (`colors_similar.py`).
3. Dominant color palette (`colors_dominant`). 
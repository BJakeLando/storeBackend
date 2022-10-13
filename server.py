from flask import Flask
import json 
from config import me, hello
from mock_data import catalog

app = Flask("Server")

@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "This is a test"

@app.get("/about")
def name():
    return "BJakeLando"

#########################################################
#      API ENDPOINTS 
#      JSON
#########################################################


@app.get("/api/version")
def version():
    v = {
        "version": "1.0.0",
        "build": 42,
        "name": "penguin",
        "developer": me
    }

    hello()
    
    return json.dumps(v)

# get /api/catalog
# return catlog as json

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


# get /api/products/count
#  return the number of products in the catalog

@app.get("/api/products/count")
def get_products_count():
    return json.dumps(len(catalog))

    https://github.com/BJakeLando/storeBackend.git

app.run(debug=True)
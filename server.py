
from os import remove
from flask import Flask, request, abort
import json
from config import me, db
from mock_data import catalog
from bson import ObjectId


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

    return json.dumps(v)


# get /api/catalog
# return catlog as json


def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj


@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({}).sort("title")
    results = []
    for prod in cursor:
        results.append(fix_id(prod))

        return json.dumps(results)


@app.get("/api/coupons")
def get_coupons():
    cursor = db.coupons.find({}).sort("title")
    results = []
    for coupon in cursor:
        results.append(fix_id(coupon))

        return json.dumps(results)


@app.post("/api/catalog")
def save_product():
    product = request.get_json()

    if product is None:
        return abort(400, "Product required")

    if not "title" in product:
        return abort(404, "Title Required")

    if len(product["title"]) < 5:
        return abort(400, "Minimum 5 characters required")

    if not "category" in product:
        return abort(400, "Please provide a category")
    
    if not "price" in product:
        return abort(400, "Price is required")

    if (not isinstance(product["price"], float)) and not isinstance(product["price"], int):
        return abort(400, "Price must be a number")

    if product["price"] < 1:
        return abort(400, "Invalid price")

    product["category"] = product["category"].lower()

    # validate price, title, etc
    db.products.insert_one(product)

    # Solved the objectId Crash below this comment
    product["_id"] = str(product["_id"])

    return json.dumps(product)


@app.get("/api/coupons/details/<code>")
def get_couponCode(code):
    coupon = db.coupons.find_one({"code": code})
    if coupon:
        fix_id(coupon)
        return json.dumps(coupon)

    return abort(404, "Invlaid code")


@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()

    if not coupon:
        return abort(400, "Coupon required")

    if not "code" in coupon:
        return abort(400, "Coupon code required")

    if not "discount" in coupon:
        return abort(400, "Discount is required")

    if (not isinstance(coupon["discount"], float)) and not isinstance(coupon["discount"], int):
        return abort(400, "Discount must be a number")

    # validate coupon
    db.coupons.insert_one(coupon)
    fix_id(coupon)
    return json.dumps(coupon)


@app.put("/api/catalog")
def update_product():
    product = request.get_json()
    id = product.pop("_id")  # read and remove
    # del product ["_id"] remove
    db.products.update_one({"_id": ObjectId(id)}, {"$set": product})

    return json.dumps("ok")


@app.delete("/api/catalog/<id>")
def delete_product(id):
    res = db.products.delete_one({"_id": ObjectId(id)})
    return json.dumps({"count": res.deleted_count})

# get /api/products/count
#  return the number of products in the catalog


@app.get("/api/products/count")
def get_products_count():
    count = db.products.count_documents({})
    return json.dumps(count)


@app.get("/api/products/total")
def total_price():
    total = 0
    cursor = db.products.find({})
    for x in cursor:
        total += x["price"]

    return json.dumps(total)

    # for prod in catalog:
    #     total += prod["price"]

    # return json.dumps(total)


@app.get("/api/products/details/<id>")
def get_details(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    if prod:
        return json.dumps(fix_id(prod))

    return abort(404, "Product not found")


# get /api/catalog/category
# return all the products that belong to the received category

@app.get("/api/catalog/<category>")
def by_category(category):

    results = []
    cursor = db.products.find({"category": category})
    for prod in cursor:
        results.append(fix_id(prod))

    # for prod in catalog:
    #     if prod["category"].lower() == category.lower():
    #         results.append(prod)

    return json.dumps(results)

    # get /api/catalog/lower/<amount>


@app.get("/api/catalog/lower/<float:amount>")
def lower_than(amount):
    results = []
    cursor = db.products.find({"price": {"$lt": float(amount)}})
    for prod in cursor:
        results.append(fix_id(prod))
    # for prod in catalog:
    #     if prod["price"] < float(amount):

    #         results.append(prod)

    return json.dumps(results)


@app.get("/api/catalog/greater/<amount>")
def greater_than(amount):
    results = []
    cursor = db.products.find({"price": {"$gte": float(amount)}})
    for prod in cursor:
        results.append(fix_id(prod))
        # if prod["price"] > float(50):
        #     results.append(prod)

    return json.dumps(results)

# get /api/category/unique
# get the list of unique categories


@app.get("/api/catalog/unique")
def unique_cats():
    results = []
    cursor = db.products.distinct("category")
    for cat in cursor:
        results.append(cat)

    # for prod in catalog:
        # if not category exist inside results
        # then add it
        # category = prod["category"]
        # if not category in results:
        #     results.append(category)

    return json.dumps(results)

# app.run(debug=True)

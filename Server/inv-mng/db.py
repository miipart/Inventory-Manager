import pymongo
from flask import current_app, g
from flask.cli import with_appcontext

def __get_db():
    if 'db' not in g:
        g.db = pymongo.MongoClient('mongodb://server:fixMe@localhost:27017/Inventory-Manager')['Inventory-Manager']
    return g.db

def __insert(collection, data):
    db = __get_db()
    col = db[collection]
    r = col.insert_one(data)
    return r

def add_category(name="Sample Name. Please change", desc="A sample category. Please change"):
    data= {"name":name, "desc":desc}
    collection = "Category"
    r = __insert(collection,data)
    return r

def get_categories():
    db = __get_db()
    collection = db['Category']
    r = collection.find({})
    return r

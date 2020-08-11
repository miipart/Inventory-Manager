import pymongo
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = pymongo.MongoClient('mongodb://server:fixMe@localhost:27017/Inventory-Manager')['Inventory-Manager']
    return g.db

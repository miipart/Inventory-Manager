
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    from .db import get_db
    db = get_db()
    #db['test'].insert_one({'name':'johnny'})
    x = db['test'].find_one()
    return x['name']

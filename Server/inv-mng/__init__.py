
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #from .db import add_category, get_categories
    return "Hello"

    #add_category("Packet one", "Run baby run")

    #return ''.join( [f"<li>{x['name']}</li>" for x in get_categories()])

@app.route('/api/new_category', methods=['GET', 'POST'])
def api_new_category():
    if request.method == "GET":
        return render_template('/new_category.html')

    from .db import add_category

    new_category_name = request.form['name']
    new_cateogry_desc = request.form['desc']

    add_category(new_category_name, new_cateogry_desc)
    return "ok"

@app.route('/api/get_categories')
def api_get_categories():
    from .db import get_categories
    from flask import jsonify
    categories = [ {"name":x['name'], "id":str(x.get('_id')), "desc":x['desc'] } for x in get_categories() ]
    return jsonify(categories)

@app.route('/api/get_items')
@app.route('/api/get_items/<string:category_id>')
def api_get_items(category_id=None):
    from .db import get_items
    from flask import jsonify
    items = [ {"name":x['name'], "category_id":x['category_id'], "id":str(x['_id'])} for x in get_items({"category_id":category_id} if category_id else {})]
    return jsonify(items)

@app.route('/api/new_item', methods=['GET','POST'])
def api_new_item():
    if request.method == "GET":
        return render_template('/new_item.html')

    from .db import add_item

    name = request.form['name']
    category_id = request.form['category_id']

    add_item(name=name,category_id=category_id)
    return "ok"

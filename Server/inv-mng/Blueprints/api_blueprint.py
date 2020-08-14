from flask import Blueprint, request, render_template, jsonify
from ..db import add_category, get_categories, get_items, add_item

def RegisterBlueprint(app):
    """
    Registers the api_blueprint to the app
    """
    bp = Blueprint("API-Blueprint", __name__)

    ## TODO: Add auth for API

    @bp.route('/test')
    def ApiTest():
        return 'The api route seamse to work'

    @bp.route('/category/new', methods=['POST'])
    def ApiNewCategory():
        """
        Creates a new category Document in the DB.
        Returns the new Document as JSON
        """
        new_category_name = request.form['name']
        new_cateogry_desc = request.form['desc']

        r = add_category(new_category_name, new_cateogry_desc)
        r['_id'] = str(r['_id']) # Unpacks ObjectID, so r can be serialized
        return jsonify(r)

    @bp.route('/category/get')
    def ApiGetCategories():
        """
        Returns a JSON set of all categories
        """
        categories = [ {"name":x['name'], "_id":str(x.get('_id')), "desc":x['desc'] } for x in get_categories() ]
        return jsonify(categories)

    @bp.route('/item/get')
    @bp.route('/item/get/<string:category_id>')
    def api_get_items(category_id=None):
        """
        Returns a JSON set of all items in DB, filtered by category_id.
        category_id left as None returns all items.
        """
        print(category_id)
        items = [ {"name":x['name'], "category_id":x['category_id'], "_id":str(x['_id'])} for x in get_items({"category_id":category_id} if category_id else {})]
        return jsonify(items)

    @bp.route('/item/new', methods=['POST'])
    def api_new_item():
        """
        Creates a new item Document in DB.
        Returns the new item as JSON.
        """
        name = request.form['name']
        category_id = request.form['category_id']
        r = add_item(name=name,category_id=category_id)
        r['_id'] = str(r['_id']) # Unpacks ObjectID, so r can be serialized
        return jsonify(r)


    app.register_blueprint(bp,url_prefix="/api")

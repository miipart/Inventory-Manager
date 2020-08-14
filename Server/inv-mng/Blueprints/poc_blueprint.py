from flask import Blueprint, render_template

def RegisterBlueprint(app):

    bp = Blueprint('POC-Blueprint', __name__)

    @bp.route('/new_item')
    def PocNewItem():
        return render_template('/new_item.html')

    @bp.route('/new_category')
    def PocNewCategory():
        return render_template('/new_category.html')

    app.register_blueprint(bp, url_prefix='/poc')

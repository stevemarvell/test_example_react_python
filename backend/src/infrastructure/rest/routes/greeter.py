from flask import request, jsonify, Blueprint

from application import greeting_by_name_query

bp = Blueprint('greeter', __name__)


@bp.route('/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name')

    if not name or not isinstance(name, str):
        return jsonify({"error": "Invalid or missing 'name' parameter"}), 400

    greeting = greeting_by_name_query.handle(name)
    return jsonify({"greeting": greeting})

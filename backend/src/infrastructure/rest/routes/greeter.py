from flask import jsonify, Blueprint, make_response
from flask import request as incoming_request
from flask_cors import CORS

from application import greeting_by_name_query

bp = Blueprint('greeter', __name__)

CORS(bp)


@bp.route('/greet', methods=['GET'])
def response():
    response_data, status_code = greet_process(incoming_request)
    return generate_response(response_data, status_code)


def generate_response(response_data, status_code=200):
    return jsonify(response_data), status_code


def greet_process(request):
    name = request.args.get('name')
    if not name or not isinstance(name, str):
        return {"error": "Invalid or missing 'name' parameter"}, 400

    greeting = greeting_by_name_query.handle(name)
    return {"greeting": greeting}, 200

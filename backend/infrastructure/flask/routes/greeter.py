from flask import Blueprint, request, jsonify
from schema import SchemaError

from application import greeting_by_name_query
from di import dependency_manager

greeter_bp = Blueprint('greeter', __name__)


@greeter_bp.route('/greet', methods=['GET'])
def greet():
    greeting_repository = dependency_manager.greeting_repository()

    name = request.args.get('name')
    if not name:
        return jsonify({"detail": "Missing parameter 'name'"}), 400

    try:
        greeting = greeting_by_name_query.handle(greeting_repository, {"name": name})
        return jsonify({"greeting": greeting})
    except SchemaError as e:
        return jsonify({"detail": "Invalid or missing parameter"}), 400
    except Exception as e:
        return jsonify({"detail": "An error occurred"}), 500

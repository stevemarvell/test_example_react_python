from flask import Flask, request, jsonify
from flask_cors import CORS
from injector import inject
from schema import SchemaError
from werkzeug.exceptions import BadRequest, InternalServerError


from application import greeting_by_name_query
from di import dependency_manager
from domain.greeting_repository import GreetingRepository

app = Flask(__name__)

origins = [
    "http://localhost",
    "http://localhost:3000",  # front end
]

CORS(app, origins=origins)

@app.route('/greet', methods=['GET'])
@inject
def greet_route(greeting_repository: GreetingRepository=dependency_manager.greeting_repository()):
    name = request.args.get('name')

    if not name:
        return jsonify({"detail": "name parameter missing"}), 400

    try:
        return jsonify(greet(name, greeting_repository)), 200
    except SchemaError as e:
        return jsonify({"detail": "Invalid or missing parameter"}), 400
    except BadRequest as e:
        return jsonify({"detail": "Well we didn't expect that!"}), 400
    except Exception as e:
        return jsonify({"detail": "The sky is falling!"}), 500


def greet(name, greeting_repository: GreetingRepository):

    try:
        greeting = greeting_by_name_query.handle(greeting_repository, {"name": name})
        return {"greeting": greeting}
    except SchemaError as e:
        raise BadRequest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




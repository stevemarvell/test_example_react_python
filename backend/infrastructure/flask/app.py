from flask import Flask, request, jsonify
from flask_cors import CORS
from schema import SchemaError
from werkzeug.exceptions import BadRequest


from application import greeting_by_name_query
from di import dependency_manager, inject_greeting_repository
from domain.greeting_repository import GreetingRepository

app = Flask(__name__)

origins = [
    "http://localhost",
    "http://localhost:3000",  # front end
]

CORS(app, origins=origins)

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"detail": "Well we didn't expect that!"}), 400

@app.route('/greet', methods=['GET'])
@inject_greeting_repository
def greet_route(greeting_repository: GreetingRepository):
    name = request.args.get('name')

    if not name:
        raise BadRequest()

    return jsonify(greet(name, greeting_repository)), 200

def greet(name, greeting_repository: GreetingRepository):

    try:
        greeting = greeting_by_name_query.handle(greeting_repository, {"name": name})
        return {"greeting": greeting}
    except SchemaError as e:
        raise BadRequest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




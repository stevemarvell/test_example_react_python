from flask import Flask, request, jsonify
from flask_cors import CORS

from infrastructure.flask.routes.greeter import greeter_bp

app = Flask(__name__)

CORS(app, origins=["http://localhost", "http://localhost:3000"])

app.register_blueprint(greeter_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


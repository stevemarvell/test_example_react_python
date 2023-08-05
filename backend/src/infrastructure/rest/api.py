from flask import Flask

from infrastructure.rest.routes.greeter import bp as greeter_bp

api = Flask(__name__)
api.register_blueprint(greeter_bp)

if __name__ == '__main__':
    api.run()

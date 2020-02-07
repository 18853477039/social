from flask import Flask
from flask_restful import Api
from app import views
from app.apis import Calculator


def create_app():
    app = Flask(__name__)
    app.debug = True
    api = Api(app)
    api.add_resource(Calculator, '/cal_num')

    app.register_blueprint(views.bp)
    return app

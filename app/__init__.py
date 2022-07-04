from flask import Flask

# app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(dev):
    app = Flask(__name__, instance_relative_config=True)
    if dev:
        CONFIG_FILE = 'instance.config.DevConfig'
    else:
        CONFIG_FILE = 'instance.config.TestConfig'
    print(CONFIG_FILE)
    app.config.from_object('instance.config.DevConfig')
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    from app.customer_order.controllers import customer_order_blueprint
    app.register_blueprint(customer_order_blueprint)


def setup_db():
    db.drop_all()
    db.create_all()

# @app.errorhandler(400)
# def missing_customer_data(e):
#     return jsonify(error=str(e)), 400
#
#
# @app.errorhandler(404)
# def invalid_customer_data(e):
#     return jsonify(error=str(e)), 404
#
# # clear all previous data stored after restarting
# db.drop_all()
# db.create_all()
# db.session.commit()

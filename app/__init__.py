from flask import Flask, jsonify

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
    register_error_handlers(app)
    return app


def initialize_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    from app.customers.routes import customer_blueprint
    from app.orders.routes import order_blueprint
    app.register_blueprint(customer_blueprint)
    app.register_blueprint(order_blueprint)


def register_error_handlers(app):
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(404, handle_not_found)


def setup_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


def handle_bad_request(e):
    return jsonify(error=str(e)), 400


def handle_not_found(e):
    return jsonify(error=str(e)), 404

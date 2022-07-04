from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from tests.dummy_data import customer_dummy_data, order_dummy_data

db = SQLAlchemy()


def create_app(dev):
    app = Flask(__name__, instance_relative_config=True)
    if dev:
        CONFIG_FILE = 'instance.config.DevConfig'
    else:
        CONFIG_FILE = 'instance.config.TestConfig'
    print(CONFIG_FILE)
    app.config.from_object(CONFIG_FILE)
    initialize_extensions(app, dev)
    register_blueprints(app)
    register_error_handlers(app)
    return app


def initialize_extensions(app, dev):
    db.init_app(app)

    with app.app_context():
        if not dev:
            engine = create_engine('postgresql://wuluoyu:password@localhost/backend_test')
            engine.execute('DROP TABLE IF EXISTS customer CASCADE ;')
            engine.execute('DROP TABLE IF EXISTS "order";')
            from .models import Customer, Order
            db.create_all()
            insert_dummy_data()
            db.session.commit()
        else:
            db.create_all()
            db.session.commit()


def insert_dummy_data():
    from app.models import Customer, Order
    for customer in customer_dummy_data:
        Customer.create(customer['name'], customer['dob'])
    for order in order_dummy_data:
        Order.create(
            order['item_name'],
            order['item_price'],
            order['datetime'],
            order['customer_id']
        )

def register_blueprints(app):
    from app.customers.routes import customer_blueprint
    from app.orders.routes import order_blueprint
    app.register_blueprint(customer_blueprint)
    app.register_blueprint(order_blueprint)


def register_error_handlers(app):
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(404, handle_not_found)
    app.register_error_handler(405, handle_method_not_allowed)


def setup_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


def handle_bad_request(e):
    return jsonify(error=str(e)), 400


def handle_not_found(e):
    return jsonify(error=str(e)), 404


def handle_method_not_allowed(e):
    return jsonify(error="405: Method Not Allowed"), 405

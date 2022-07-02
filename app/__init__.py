from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.errorhandler(400)
def missing_customer_data(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(404)
def invalid_customer_data(e):
    return jsonify(error=str(e)), 404


from app.customer_order.controllers import mod_customer_order as customer_order_module

app.register_blueprint(customer_order_module)

# clear all previous data stored after restarting
db.drop_all()
db.create_all()
db.session.commit()

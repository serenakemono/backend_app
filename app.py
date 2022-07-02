import datetime
import json

import sqlalchemy.exc
import werkzeug.exceptions
from sqlalchemy import desc
from werkzeug.exceptions import HTTPException
from flask import Flask, render_template, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wuluoyu:password@localhost/backend'
db = SQLAlchemy(app)
CORS(app)


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date)
    orders = db.relationship('Order', backref='customer')

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return '<h3>%r</h3>' % self.name


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    item_price = db.Column(db.DECIMAL, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __init__(self, item_name, item_price, datetime, customer_id):
        self.item_name = item_name
        self.item_price = item_price
        self.datetime = datetime
        self.customer_id = customer_id

    def __repr__(self):
        return '<h3>%r</h3>' % self.item_name


@app.route('/customer', methods=['GET'])
def get_customers():
    number = request.args.get('number', type=int, default=None)
    if number is None:
        customers = Customer.query.all()
    else:
        customers = Customer.query.order_by(desc(Customer.dob)).limit(number).all()

    all_customers = []
    for customer in customers:
        results = {
            "customer_id": customer.id,
            "customer_name": customer.name,
            "customer_dob": customer.dob.strftime("%Y-%m-%d"),
        }
        all_customers.append(results)

    return jsonify(
        {
            "success": True,
            "customers": all_customers,
            "total_customers": len(customers),
        }
    )


@app.route('/order', methods=['GET'])
def get_orders():
    customer_id = request.args.get('customer_id', type=int, default=None)
    if customer_id is None:
        orders = Order.query.all()
    else:
        orders = Order.query.filter_by(customer_id=customer_id).all()

    all_orders = []
    for order in orders:
        results = {
            "order_id": order.id,
            "item_name": order.item_name,
            "item_price": order.item_price,
            "order_time": order.datetime,
            "customer_id": order.customer_id,
        }
        all_orders.append(order)

    return jsonify(
        {
            "success": True,
            "orders": all_orders,
            "total_orders": len(all_orders),
        }
    )


@app.route('/customer/create', methods=['POST'])
def create_customer():
    customer_data = request.json
    try:
        name = customer_data["name"]
        dob = customer_data["dob"]
    except KeyError:
        abort(400, description="Customer name and/or dob missing")

    if name == "":
        abort(404, description="Name cannot be empty")

    try:
        date = datetime.datetime.strptime(dob, '%Y-%m-%d')
        present = datetime.datetime.now()
        if present.date() < date.date():
            abort(404, description="Invalid date, should be before today")
    except ValueError:
        abort(404, description="Incorrect date format, should be YYYY-mm-dd")

    customer = Customer(name=name, dob=dob)
    db.session.add(customer)
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "response": "Customer created",
        }
    )


@app.errorhandler(400)
def missing_customer_data(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(404)
def invalid_customer_data(e):
    return jsonify(error=str(e)), 404



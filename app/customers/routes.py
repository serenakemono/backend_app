import datetime
from sqlalchemy import desc
from flask import jsonify, request, abort, Blueprint
from app import db
from app.models import Customer
from . import customer_blueprint


@customer_blueprint.route('/customer', methods=['GET'])
def get_customers():
    number = request.args.get('number', type=int, default=None)
    if number is None:
        customers = Customer.query.all()
    else:
        customers = Customer.query.order_by(desc(Customer.dob)).limit(number).all()

    all_customers = retrieve_customers_info(customers)

    return jsonify({
            "customers": all_customers,
            "total_customers": len(customers),
        }), 200


def retrieve_customers_info(customers):
    all_customers = []
    for customer in customers:
        orders = []
        for order in customer.orders:
            orders.append(order.id)
        results = {
            "customer_id": customer.id,
            "customer_name": customer.name,
            "customer_dob": customer.dob.strftime("%Y-%m-%d"),
            "customer_orders": {
                "orders": orders,
                "total_orders": len(orders),
            }
        }
        all_customers.append(results)
    return all_customers


@customer_blueprint.route('/customer/create', methods=['POST'])
def create_customer():
    name, dob = retrieve_customer_params(request.json)
    validate_customer_name(name)
    validate_customer_dob(dob)

    customer = Customer.create(name, dob)

    return jsonify({
        "customer_id": customer.id,
        "customer_name": customer.name,
        "customer_dob": customer.dob.strftime("%Y-%m-%d"),
    }), 201


def retrieve_customer_params(customer_data):
    try:
        name = customer_data["name"]
        dob = customer_data["dob"]
        return name, dob
    except KeyError:
        abort(400, description="Customer name and/or dob missing")


def validate_customer_name(name):
    if name == "":
        abort(400, description="Name cannot be empty")


def validate_customer_dob(dob):
    try:
        date = datetime.datetime.strptime(dob, '%Y-%m-%d')
        present = datetime.datetime.now()
        if present.date() < date.date():
            abort(400, description="Invalid date, should be before today")
    except ValueError:
        abort(400, description="Incorrect date format, should be YYYY-mm-dd")

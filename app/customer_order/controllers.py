import datetime
from sqlalchemy import desc
from flask import jsonify, request, abort, Blueprint
from app import app, db
from app.customer_order.entities import Customer, Order

mod_customer_order = Blueprint('customer_order', __name__, url_prefix='')


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/customer', methods=['GET'])
def get_customers():
    number = request.args.get('number', type=int, default=None)
    if number is None:
        customers = Customer.query.all()
    else:
        customers = Customer.query.order_by(desc(Customer.dob)).limit(number).all()

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
        all_orders.append(results)

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

    return jsonify({
        "customer_id": customer.id,
        "customer_name": customer.name,
        "customer_dob": customer.dob.strftime("%Y-%m-%d"),
    })


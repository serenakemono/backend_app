import datetime

from flask import jsonify, request, Blueprint
from app.models import Order
from . import order_blueprint


@order_blueprint.route('/order', methods=['GET'])
def get_orders():
    customer_id = request.args.get('customer_id', type=int, default=None)
    if customer_id is None:
        orders = Order.query.all()
    else:
        orders = Order.query.filter_by(customer_id=customer_id).all()

    all_orders = retrieve_orders_info(orders)

    return jsonify(
        {
            "orders": all_orders,
            "total_orders": len(all_orders),
        }
    ), 200


def retrieve_orders_info(orders):
    all_orders = []
    for order in orders:
        results = {
            "order_id": order.id,
            "item_name": order.item_name,
            "item_price": order.item_price,
            "order_time": order.datetime.strftime('%Y-%m-%d %H:%M:%S'),
            "customer_id": order.customer_id,
        }
        all_orders.append(results)
    return all_orders

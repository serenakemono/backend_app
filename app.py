from flask import Flask, render_template, jsonify
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
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customer', methods=['GET'])
def get_customers():
    all_customers = []
    customers = Customer.query.all()
    for customer in customers:
        results = {
            "customer_id": customer.id,
            "customer_name": customer.name,
            "customer_dob": customer.dob,
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
    all_orders = []
    orders = Order.query.all()
    for order in orders:
        results = {

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

# db.create_all()
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

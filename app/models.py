import decimal

from app import db


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date)
    orders = db.relationship('Order', backref='customer')

    def __init__(self, name: str, dob: str):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return '<Customer: %s>' % self.name

    @staticmethod
    def create(name: str, dob: str):
        new_customer = Customer(name, dob)
        db.session.add(new_customer)
        db.session.commit()
        return new_customer


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    item_price = db.Column(db.DECIMAL(10, 2), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __init__(self, item_name: str, item_price: decimal, datetime: str, customer_id: int):
        self.item_name = item_name
        self.item_price = item_price
        self.datetime = datetime
        self.customer_id = customer_id

    def __repr__(self):
        return f'<Order: {self.id}>'

    @staticmethod
    def create(item_name: str, item_price: decimal, datetime: str, customer_id: int):
        new_order = Order(item_name, item_price, datetime, customer_id)
        db.session.add(new_order)
        db.session.commit()
        return new_order

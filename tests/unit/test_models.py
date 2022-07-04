from app.models import Customer, Order


def test_new_customer():
    """
    GIVEN a Customer model
    WHEN a new Customer is created
    THEN check the name, dob are defined correctly
    """
    customer = Customer('Serena Wu Luoyu', '2000-07-15')
    assert customer.name == 'Serena Wu Luoyu'
    assert customer.dob == '2000-07-15'
    assert customer.__repr__() == '<Customer: Serena Wu Luoyu>'


def test_new_order():
    """
    GIVEN a Order model
    WHEN a new Order is created
    THEN check the item_name, item_price, datetime, customer_id are defined correctly
    """
    order = Order('Coke', 2.00, '2022-07-04 19:11:25', 1)
    assert order.item_name == 'Coke'
    assert order.item_price == 2.00
    assert order.datetime == '2022-07-04 19:11:25'
    assert order.customer_id == 1
    assert order.__repr__() == f'<Order: {order.id}>'

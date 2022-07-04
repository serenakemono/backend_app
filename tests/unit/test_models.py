from app.models import Customer, Order


def test_new_customer(new_customer):
    """
    GIVEN a Customer model
    WHEN a new Customer is created
    THEN check the name, dob are defined correctly
    """
    assert new_customer.name == 'Serena Wu Luoyu'
    assert new_customer.dob == '2000-07-15'
    assert new_customer.__repr__() == '<Customer: Serena Wu Luoyu>'


def test_new_order(new_order):
    """
    GIVEN a Order model
    WHEN a new Order is created
    THEN check the item_name, item_price, datetime, customer_id are defined correctly
    """
    assert new_order.item_name == 'Coke'
    assert new_order.item_price == 2.00
    assert new_order.datetime == '2022-07-04 19:11:25'
    assert new_order.customer_id == 1
    assert new_order.__repr__() == f'<Order: {new_order.id}>'

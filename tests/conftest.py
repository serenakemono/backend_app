import pytest
from app import create_app
from app.models import Customer, Order


@pytest.fixture(scope='module')
def new_customer():
    customer = Customer('Serena Wu Luoyu', '2000-07-15')
    return customer


@pytest.fixture(scope='module')
def new_order():
    order = Order('Coke', 2.00, '2022-07-04 19:11:25', 1)
    return order


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(False)

    with flask_app.test_client() as testing_client:
        yield testing_client

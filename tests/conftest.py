import pytest
from sqlalchemy import MetaData, ForeignKeyConstraint, Table, create_engine
from sqlalchemy.engine import reflection
from sqlalchemy.sql.ddl import DropConstraint, DropTable

from app import create_app, db
from app.models import Customer, Order
from tests.dummy_data import customer_dummy_data, order_dummy_data


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


@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()
    db.session.commit()
    yield

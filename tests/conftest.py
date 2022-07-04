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


def db_DropEverything(db):
    # From http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything

    conn=db.engine.connect()

    # the transaction only applies if the DB supports
    # transactional DDL, i.e. Postgresql, MS SQL Server
    trans = conn.begin()

    inspector = reflection.Inspector.from_engine(db.engine)

    # gather all data first before dropping anything.
    # some DBs lock after things have been dropped in
    # a transaction.
    metadata = MetaData()

    tbs = []
    all_fks = []

    for table_name in inspector.get_table_names():
        fks = []
        for fk in inspector.get_foreign_keys(table_name):
            if not fk['name']:
                continue
            fks.append(
                ForeignKeyConstraint((),(),name=fk['name'])
                )
        t = Table(table_name,metadata,*fks)
        tbs.append(t)
        all_fks.extend(fks)

    for fkc in all_fks:
        conn.execute(DropConstraint(fkc))

    for table in tbs:
        conn.execute(DropTable(table))

    trans.commit()

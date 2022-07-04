import json


def test_get_all_orders(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/order' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('order')
    assert response.status_code == 200
    assert b'orders' in response.data
    assert b'total_orders' in response.data
    data = json.loads(response.data)
    assert data['total_orders'] == 10
    assert data['orders'] == \
           [{"customer_id": 6, "item_name": "Nulla Integer LLC", "item_price": "79.33", "order_id": 1,
             "order_time": "2022-07-04 08:33:55"},
            {"customer_id": 5, "item_name": "Nec Quam Limited", "item_price": "33.06", "order_id": 2,
             "order_time": "2022-07-04 05:21:24"},
            {"customer_id": 5, "item_name": "Lorem LLP", "item_price": "68.40", "order_id": 3,
             "order_time": "2022-07-04 10:37:17"},
            {"customer_id": 2, "item_name": "At PC", "item_price": "44.59", "order_id": 4,
             "order_time": "2022-07-04 01:14:33"},
            {"customer_id": 10, "item_name": "At Auctor Ullamcorper Incorporated", "item_price": "18.12", "order_id": 5,
             "order_time": "2022-07-04 11:30:39"},
            {"customer_id": 8, "item_name": "Eget Venenatis Corporation", "item_price": "3.64", "order_id": 6,
             "order_time": "2022-07-04 09:54:27"},
            {"customer_id": 8, "item_name": "Risus Donec Corp.", "item_price": "94.64", "order_id": 7,
             "order_time": "2022-07-04 11:11:03"},
            {"customer_id": 5, "item_name": "Arcu Eu Foundation", "item_price": "41.86", "order_id": 8,
             "order_time": "2022-07-04 08:21:27"},
            {"customer_id": 2, "item_name": "Purus Ac Tellus Limited", "item_price": "67.53", "order_id": 9,
             "order_time": "2022-07-04 02:25:30"},
            {"customer_id": 9, "item_name": "Donec Associates", "item_price": "83.43", "order_id": 10,
             "order_time": "2022-07-04 10:23:58"}]


def test_get_all_orders_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/order' page is posted to (POST)
    THEN check that a '405' status code is returned
    """

    response = test_client.post('/order')
    assert response.status_code == 405
    assert b"orders" not in response.data
    assert b"total_orders" not in response.data


def test_get_orders_from_customer_with_id_5(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/order?customer_id=5' page is requested (GET)
    THEN check that the response is valid
    """

    response = test_client.get('/order?customer_id=5')
    assert response.status_code == 200
    assert b"orders" in response.data
    assert b"total_orders" in response.data
    data = json.loads(response.data)
    assert data['total_orders'] == 3
    assert data['orders'] == \
           [{"customer_id": 5, "item_name": "Nec Quam Limited", "item_price": "33.06", "order_id": 2,
             "order_time": "2022-07-04 05:21:24"},
            {"customer_id": 5, "item_name": "Lorem LLP", "item_price": "68.40", "order_id": 3,
             "order_time": "2022-07-04 10:37:17"},
            {"customer_id": 5, "item_name": "Arcu Eu Foundation", "item_price": "41.86", "order_id": 8,
             "order_time": "2022-07-04 08:21:27"}]


def test_get_orders_from_non_integer_customer_id(test_client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/order?customer_id=serena' page is requested (GET)
        THEN check that a '400' status code is returned
        """

    response = test_client.get('/order?customer_id=serena')
    assert response.status_code == 400
    assert b"orders" not in response.data
    assert b"total_orders" not in response.data


def test_get_orders_from_customer_id_not_found(test_client):
    """
        GIVEN a Flask application configured for testing
        WHEN the '/order?customer_id=20' page is requested (GET)
        THEN check that a '404' status code is returned
        """

    response = test_client.get('/order?customer_id=20')
    assert response.status_code == 404
    assert b"orders" not in response.data
    assert b"total_orders" not in response.data


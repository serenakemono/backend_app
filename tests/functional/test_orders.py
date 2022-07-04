from app import create_app


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


def test_get_all_orders_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/order' page is posted to
    THEN check that a '405' status code is returned
    """

    response = test_client.post('/order')
    assert response.status_code == 405
    assert b"orders" not in response.data
    assert b"total_orders" not in response.data

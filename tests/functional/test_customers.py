from app import create_app


def test_get_all_customers():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/customer' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app(False)

    with flask_app.test_client() as test_client:
        response = test_client.get('customer')
        assert response.status_code == 200
        assert b'success' in response.data
        assert b'customers' in response.data
        assert b'total_customers' in response.data

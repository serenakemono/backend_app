import json


def test_get_all_customers(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('customer')
    assert response.status_code == 200
    assert b'customers' in response.data
    assert b'total_customers' in response.data
    data = json.loads(response.data)
    assert data['total_customers'] == 10
    assert data['customers'] == \
           [{"customer_dob": "2022-06-09", "customer_id": 1, "customer_name": "Erin Morgan",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "1983-02-08", "customer_id": 2, "customer_name": "Quyn Chapman",
             "customer_orders": {"orders": [4, 9], "total_orders": 2}},
            {"customer_dob": "2005-12-22", "customer_id": 3, "customer_name": "Calista Mcgowan",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "1990-06-08", "customer_id": 4, "customer_name": "Desiree Skinner",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "1946-09-12", "customer_id": 5, "customer_name": "Shelby Hale",
             "customer_orders": {"orders": [2, 3, 8], "total_orders": 3}},
            {"customer_dob": "1987-03-20", "customer_id": 6, "customer_name": "Darrel Salas",
             "customer_orders": {"orders": [1], "total_orders": 1}},
            {"customer_dob": "2007-07-13", "customer_id": 7, "customer_name": "Geraldine Frank",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "1948-10-19", "customer_id": 8, "customer_name": "Sawyer Clements",
             "customer_orders": {"orders": [6, 7], "total_orders": 2}},
            {"customer_dob": "1950-03-15", "customer_id": 9, "customer_name": "Yeo White",
             "customer_orders": {"orders": [10], "total_orders": 1}},
            {"customer_dob": "2022-06-23", "customer_id": 10, "customer_name": "Callum Santiago",
             "customer_orders": {"orders": [5], "total_orders": 1}}]


def test_get_all_customers_post(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer' page is posted to
    THEN check that a '405' status code is returned
    """

    response = test_client.post('/customer')
    assert response.status_code == 405
    assert b"customers" not in response.data
    assert b"total_customers" not in response.data


def test_get_three_youngest_customers(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer?number=3' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('customer?number=3')
    assert response.status_code == 200
    assert b'customers' in response.data
    assert b'total_customers' in response.data
    data = json.loads(response.data)
    assert data['total_customers'] == 3
    assert data['customers'] == \
           [{"customer_dob": "2022-06-23", "customer_id": 10, "customer_name": "Callum Santiago",
             "customer_orders": {"orders": [5], "total_orders": 1}},
            {"customer_dob": "2022-06-09", "customer_id": 1, "customer_name": "Erin Morgan",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "2007-07-13", "customer_id": 7, "customer_name": "Geraldine Frank",
             "customer_orders": {"orders": [], "total_orders": 0}}]


def test_get_zero_youngest_customers(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer?number=0' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('customer?number=0')
    assert response.status_code == 200
    assert b'customers' in response.data
    assert b'total_customers' in response.data
    data = json.loads(response.data)
    assert data['total_customers'] == 0
    assert data['customers'] == []


def test_get_twenty_youngest_customers(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer?number=20' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('customer?number=20')
    assert response.status_code == 200
    assert b'customers' in response.data
    assert b'total_customers' in response.data
    data = json.loads(response.data)
    assert data['total_customers'] == 10
    assert data['customers'] == \
           [{"customer_dob": "2022-06-23", "customer_id": 10, "customer_name": "Callum Santiago",
             "customer_orders": {"orders": [5], "total_orders": 1}},
            {"customer_dob": "2022-06-09", "customer_id": 1, "customer_name": "Erin Morgan",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "2007-07-13", "customer_id": 7, "customer_name": "Geraldine Frank",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "2005-12-22", "customer_id": 3, "customer_name": "Calista Mcgowan",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "1990-06-08", "customer_id": 4, "customer_name": "Desiree Skinner",
             "customer_orders": {"orders": [], "total_orders": 0}},
            {"customer_dob": "1987-03-20", "customer_id": 6, "customer_name": "Darrel Salas",
             "customer_orders": {"orders": [1], "total_orders": 1}},
            {"customer_dob": "1983-02-08", "customer_id": 2, "customer_name": "Quyn Chapman",
             "customer_orders": {"orders": [4, 9], "total_orders": 2}},
            {"customer_dob": "1950-03-15", "customer_id": 9, "customer_name": "Yeo White",
             "customer_orders": {"orders": [10], "total_orders": 1}},
            {"customer_dob": "1948-10-19", "customer_id": 8, "customer_name": "Sawyer Clements",
             "customer_orders": {"orders": [6, 7], "total_orders": 2}},
            {"customer_dob": "1946-09-12", "customer_id": 5, "customer_name": "Shelby Hale",
             "customer_orders": {"orders": [2, 3, 8], "total_orders": 3}}]


def test_create_customer_success(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer/create' page is posted to with a valid body
    THEN check that the response is valid
    """
    response = test_client.post(
        '/customer/create',
        json={"name": "Serena Wu Luoyu", "dob": "2000-07-15"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['customer_name'] == 'Serena Wu Luoyu'
    assert data['customer_dob'] == '2000-07-15'
    assert data['customer_id'] == 11


def test_create_customer_with_missing_attribute(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer/create' page is posted to without one attribute
    THEN check that a '400' status code is returned
    """
    response_wo_name = test_client.post(
        '/customer/create',
        json={"dob": "2000-07-15"})
    assert response_wo_name.status_code == 400
    assert b'customer_id' not in response_wo_name.data
    response_wo_dob = test_client.post(
        '/customer/create',
        json={"name": "Serena Wu Luoyu"})
    assert response_wo_dob.status_code == 400
    assert b'customer_id' not in response_wo_dob.data


def test_create_customer_with_empty_name(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer/create' page is posted to with an empty name
    THEN check that a '400' status code is returned
    """
    response = test_client.post(
        '/customer/create',
        json={"name": "", "dob": "2000-07-15"})
    assert response.status_code == 400
    assert b'customer_id' not in response.data


def test_create_customer_with_invalid_dob_format(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer/create' page is posted to with an invalid date format
    THEN check that a '400' status code is returned
    """
    response = test_client.post(
        '/customer/create',
        json={"name": "Serena Wu Luoyu", "dob": "2000-15-07"})
    assert response.status_code == 400
    assert b'customer_id' not in response.data


def test_create_customer_with_future_dob(test_client):
    """
    GIVEN a Flask application configured for testing
    (with 10 customers in the database)
    WHEN the '/customer/create' page is posted to with a dob in the future
    THEN check that a '400' status code is returned
    """
    response = test_client.post(
        '/customer/create',
        json={"name": "Serena Wu Luoyu", "dob": "2030-07-15"})
    assert response.status_code == 400
    assert b'customer_id' not in response.data

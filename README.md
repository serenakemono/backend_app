## Overview
This Flask backend application provides users with API endpoints to view information for customers and orders, as well as to create customer in the database.

## Table of Contents
* [Installation Instructions](#installation-instructions)
  * [Installation](#installation)
  * [Running the Flask Application](#running-the-flask-application)
  * [Testing](#testing)
* [API Endpoints](#api-endpoints)
  * [Get Customers [GET]](#get-customers)
  * [Get Several Youngest Customers [GET]](#get-several-youngest-customers)
  * [Create Customer [POST]](#create-customer)
  * [Get Orders [GET]](#get-orders)
  * [Get Orders From Customer [GET]](#get-orders-from-customer)

## Installation Instructions
### Installation
Pull down the source code from this GitHub repository:
```
$ git clone https://github.com/serenakemono/backend_app.git
```
Create a new virtual environment:
```
$ cd backend_app
$ python3 -m venv venv
```
Activate the virtual environment:
```
$ source venv/bin/activate
```
Install the python packages specified in requirements.txt:
```
(venv) $ pip install -r requirements.txt
```
### Running the Flask Application
Set the file that contains the Flask application:
```
(venv) $ export FLASK_APP='app:create_app(True)'
```
Run development server to serve the Flask application:
```
(venv) $ flask run
```
Navigate to 'http://127.0.0.1:5000' in your favorite web browser to view the website!
Alternatively, use an API platform like Postman to send API requests.
### Testing
To run all the tests:
```
(venv) $ python -m pytest
```
To check the code coverage of the tests:
```
(venv) $ coverage report
```

## API Endpoints

### Get Customers
Get information for all customers.
#### Request
GET `/customer`
#### Responses
* [200](#200)
##### 200
A set of all customers

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `customers`  | array of objects  | information for all customers in the database
| `total_customers`  | integer  | the number of customers

customer object:

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `customer_id`  | integer  | the id for the customer
| `customer_name`  | string  | the name of the customer
| `customer_dob`  | date  | the date of birth of the customer
| `customer_orders`  | object  | the orders made by the customer

order object:

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `orders`  | array of integer  | the ids for orders made by the customer
| `total_orders`  | integer  | the number of orders made by the customer

response example:
```
{
    "customers": [
        {
            "customer_dob": "2022-06-09",
            "customer_id": 1,
            "customer_name": "Erin Morgan",
            "customer_orders": {
                "orders": [1, 3],
                "total_orders": 2
            }
        },
        {
            "customer_dob": "1983-02-08",
            "customer_id": 2,
            "customer_name": "Quyn Chapman",
            "customer_orders": {
                "orders": [2],
                "total_orders": 1
            }
        }
    ],
    "total_customers": 2
}
```

### Get Several Youngest Customers
Get information for the youngest customers, the number of which is decided by the request.
#### Request
GET `/customer`

params:

| Key  | Data type | Description | Example Value |
| ------------- | ------------- | --------- | ----
| `number`  | integer  | The number of youngest customers. If the number is larger than the total number of customers, all customers will be returned. | `1`

#### Responses
* [200](#200-1)
##### 200
A set of customers

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `customers`  | array of objects  | information for all customers in the database
| `total_customers`  | integer  | the number of customers

customer object:

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `customer_id`  | integer  | the id for the customer
| `customer_name`  | string  | the name of the customer
| `customer_dob`  | date  | the date of birth of the customer
| `customer_orders`  | object  | the orders made by the customer

order object:

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `orders`  | array of integer  | the ids for orders made by the customer
| `total_orders`  | integer  | the number of orders made by the customer

response example:
```
{
    "customers": [
        {
            "customer_dob": "2022-06-09",
            "customer_id": 1,
            "customer_name": "Erin Morgan",
            "customer_orders": {
                "orders": [1, 3],
                "total_orders": 2
            }
        },
    ],
    "total_customers": 1
}
```


### Create Customer
Create a customer.
#### Request
POST `/customer/create`

body (application/json):

| Key  | Data type | Description | Example Value |
| ------------- | ------------- | --------- | ----
| `name`  | string  | the name of the customer | `"Serena Wu Luoyu"`
| `dob`  | string  | date of birth of the customer in the format of YYYY-mm-dd | `"2000-07-15"`

#### Responses
* [200](#200-2)
* [400](#400)
##### 200
A customer

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `customer_id`  | integer  | the id for the customer created
| `customer_name`  | string  | the name of the customer created
| `customer_dob`  | date  | the date of birth of the customer created

response example:
```
{
    "customer_dob": "2000-07-15",
    "customer_id": 3,
    "customer_name": "Serena Wu Luoyu"
}
```
##### 400
Missing or invalid attributes e.g. missing "name" or "dob" attribute, value of "name" as an empty string, invalid "dob" format, value of "dob" in the future.

response example:
```
{
    "error": "400 Bad Request: Invalid date, should be before today"
}
```

### Get Orders
Get information for all orders.
#### Request
GET `/order`
#### Responses
* [200](#200-3)
##### 200
A set of orders

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `orders`  | array of objects  | information for all orders in the database
| `total_orders`  | integer  | the number of orders

order object:

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `order_id`  | integer  | the id for the order
| `item_name`  | string  | the name of the item ordered
| `item_price`  | decimal  | the price of the item ordered
| `order_time`  | datetime  | the time when the order was made
| `customer_id`  | integer  | the id for the customer who made the order

response example:
```
{
    "orders": [
        {
            "customer_id": 1,
            "item_name": "Nulla Integer LLC",
            "item_price": "79.33",
            "order_id": 1,
            "order_time": "2022-07-04 08:33:55"
        },
        {
            "customer_id": 2,
            "item_name": "Nec Quam Limited",
            "item_price": "33.06",
            "order_id": 2,
            "order_time": "2022-07-04 05:21:24"
        },
        {
            "customer_id": 1,
            "item_name": "Lorem LLP",
            "item_price": "68.40",
            "order_id": 3,
            "order_time": "2022-07-04 10:37:17"
        },
    ],
    "total_orders": 3
}
```
### Get Orders From Customer
Get information for multiple orders identified by the id for the customer who made the orders.
#### Request
GET `/order`

params:

| Key  | Data type | Description | Example Value |
| ------------- | ------------- | --------- | ----
| `customer_id`  | integer  | the id for the customer | `2`

#### Responses
* [200](#200-4)
* [400](#400-1)
* [404](#404)
##### 200
A set of orders

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `success`  | boolean  | the status of the request
| `orders`  | array of objects  | information for orders made by the identified customer
| `total_orders`  | integer  | the number of orders

order object:

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `order_id`  | integer  | the id for the order
| `item_name`  | string  | the name of the item ordered
| `item_price`  | decimal  | the price of the item ordered
| `order_time`  | datetime  | the time when the order was made
| `customer_id`  | integer  | the id for the customer who made the order, which should be the `customer_id` in the request

response example:
```
{
    "orders": [
        {
            "customer_id": 2,
            "item_name": "Nec Quam Limited",
            "item_price": "33.06",
            "order_id": 2,
            "order_time": "2022-07-04 05:21:24"
        }
    ],
    "total_orders": 1
}
```
##### 400
Non-integer value for the attribute.

response example:
```
{
    "error": "400 Bad Request: customer_id must be an integer"
}
```
##### 404
Customer with provided id not found.

response example:
```
{
    "error": "404 Not Found: customer with customer_id 50 not found"
}
```
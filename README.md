# Backend app

## Overview
This backend app provides users with API endpoints to add customers to the database as well as customers and orders.

## Endpoints
* Get Customers [GET] (#get-customers)
* Get Several Youngest Customers [GET] (#get-several-youngest-customers)
* Get Orders [GET] (#get-orders)
* Get Orders From Customer [GET] (#get-orders-from-customer)
* Create Customer [POST] (#create-customer)

## Get Customers
Get information for all customers.
### Request
#### GET `/customer`
### Responses
* 200
#### 200
A set of all customers

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `success`  | boolean  | the status of the request
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

## Get Several Youngest Customers
Get information for the youngest customers, the number of which is decided by the request.
### Request
#### GET `/customer`
params:

| Key  | Data type | Description | Example Value |
| ------------- | ------------- | --------- | ----
| `number`  | integer  | The number of youngest customers. If the number is larger than the total number of customers, all customers will be returned. | `5`

### Responses
* 200
#### 200
A set of customers

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `success`  | boolean  | the status of the request
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

## Get Orders
Get information for all orders.
### Request
#### GET `/order`
### Responses
* 200
#### 200
A set of orders

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `success`  | boolean  | the status of the request
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



## Get Orders From Customers
Get information for multiple orders identified by the id for the customer who made the orders.
### Request
#### GET `/order`
params:

| Key  | Data type | Description | Example Value |
| ------------- | ------------- | --------- | ----
| `customer_id`  | integer  | the id for the customer | `2`

### Responses
* 200
#### 200
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


## Create Customer
Create a customer.
### Request
#### POST `/customer/create`
body (application/json):

| Key  | Data type | Description | Example Value |
| ------------- | ------------- | --------- | ----
| `name`  | string  | the name of the customer | `"Serena"`
| `dob`  | string  | date of birth of the customer in the format of YYYY-mm-dd | `"2000-07-15"`

### Responses
* 200
#### 200
A customer

body (application/json):

| Attribute name  | Data type | Description |
| ------------- | ------------- | --------- |
| `customer_id`  | integer  | the id for the customer created
| `customer_name`  | string  | the name of the customer created
| `customer_dob`  | date  | the date of birth of the customer created

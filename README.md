# Bangazon-API-Sprint-1
This is an API for Bangazon INC. This API will allow user to GET/POST/PUT and (sometimes) DELETE items from the Bangazon Database.

# Using the API
For now, all calls to the API will be made from http://localhost:5000 as the domain. All calls will be made from here.

**CUSTOMERS**
* GET: /customer pulls all customer entries
* GET: /customer/*customer id* pulls single customer
* GET: /inactive_customers table added to show all customers with no activity, stored as a true/false attribute
* POST: adds new customer entry
* PUT: allows editing of customer infomration

**PRODUCTS**
* GET: /products pulls all products
* GET: /products/*products id* pulls a single product
* POST: adds new product categories and products
* PUT: allows editing of product categories and products

**PRODUCT TYPE**
* GET: /product_type pulls all product categories
* GET: /product_type/*product_type id* pulls a single product category
* POST: adds new product categories
* PUT: allows editing of product categories

**PAYMENT TYPE**
* GET: /payment_type pulls all payment types
* GET: /payment_type/*payment_type id* pulls a single payment type
* POST: adds new payment type
* PUT: allows editing of a payment type

**ORDERS**
* GET: /orders pulls all orders
* GET: /orders/*orders id* pulls a single order
* POST: adds a new order
* PUT: allows editing of an order

**EMPLOYEE**
* GET: /employee pulls all employees
* GET: /employee/*employee id* pulls a single employee
* POST: adds a new employee
* PUT: allows editing of an employee

**DEPARTMENTS**
* GET: /departments pulls all departments
* GET: /departments/*department id* pulls a single department
* POST: adds a new department
* PUT: allows editing of a department

**COMPUTERS**
* GET: /computers pulls all computers
* GET: /computers/*computer id* pulls a single computer
* POST: adds a new computer
* PUT: allows editing of computer

**TRAINING**
* GET: /trainng pulls all training programs
* GET: /training/*training id* pulls a single training program
* POST: adds a new training program
* PUT: allows editing of training program

**EMPLOYEE TRAINING**
* GET: /employee_training pulls all training programs assigned to all employees
* GET: /employee_training/*employee_training id* pulls a single training program for an employee
* POST: adds a new training program assigned to an employee
* PUT: allows editing of training program to assign a new training to an employee

**PRODUCT ORDER**
* GET: /prod_order pulls all products and the orders they are assigned to
* GET: /prod_order/*prod id* pulls a single product and the order it's assigned to
* POST: adds a new product order
* PUT: allows editing of a product order

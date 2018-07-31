# Bangazon-API-Sprint-1
This is an API for Bangazon INC. This API will allow user to GET/POST/PUT and (sometimes) DELETE items from the Bangazon Database.

# Using the API
For now, all calls to the API will be made from http://localhost:5000 as the domain. All calls will be made from here.

CUSTOMERS

* GET: /customer pulls all customer entries
* GET: /customer/*customer id* pulls single customer
* GET: /inactive_customers table added to show all customers with no activity, stored as a true/false attribute
* POST: adds new customer entry
* PUT: allows editing of customer infomration



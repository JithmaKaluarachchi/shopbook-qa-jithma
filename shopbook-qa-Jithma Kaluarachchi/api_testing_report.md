\-\-\-\-\-\-\-\-\--API Test Cases\-\-\-\-\-\-\-\-\--

API_01 
Endpoint: /customers 
Method: GET 
Scenario: Get all customers
Expected Result: Customer list returned 
Status: 200 OK

API_02 
Endpoint: /customers 
Method: POST 
Scenario: Create new customer
Expected Result: Customer created 
Status: 201 Created

API_03 
Endpoint: /customers/1 
Method: GET 
Scenario: Get valid customer
Expected Result: Customer data returned 
Status: 200 OK

API_04 
Endpoint: /customers/999 
Method: GET 
Scenario: Get invalid customer 
Expected Result: Resource not found 
Status: 404 Not Found

API_05 
Endpoint: /customers/1 
Method: PUT 
Scenario: Update customer
Expected Result: Customer updated 
Status: 200 OK

API_06 
Endpoint: /customers/999 
Method: PUT 
Scenario: Update invalid customer 
Expected Result: Resource not found 
Status: 404 Not Found

API_07 
Endpoint: /customers/1 
Method: DELETE 
Scenario: Delete customer
Expected Result: Customer deleted 
Status: 200 OK

API_08 
Endpoint: /customers/700 
Method: DELETE 
Scenario: Delete invalid customer 
Expected Result: Resource not found 
Status: 404 Not Found

API_09 
Endpoint: /creditSales 
Method: GET 
Scenario: Get all credit sales
Expected Result: Credit sales list returned 
Status: 200 OK

API_10 
Endpoint: /creditSales 
Method: POST 
Scenario: Create credit sale
Expected Result: Credit sale created 
Status: 201 Created

API_11 
Endpoint: /creditSales/1 
Method: DELETE 
Scenario: Delete credit sale 
Expected Result: Delete credit sale 
Status: 200 OK

API_12 
Endpoint: /products 
Method: GET 
Scenario: Get all products
Expected Result: Product list returned 
Status: 200 OK

API_13 
Endpoint: /products/1 
Method: PUT 
Scenario: Update product price
Expected Result: Product updated 
Status: 200 OK

API_14 
Endpoint: /products/999 
Method: DELETE 
Scenario: Delete invalid product 
Expected Result: Resource not found 
Status: 404 Not Found

API_15 
Endpoint: /expenses 
Method: GET 
Scenario: Get All Expenses
Expected Result: Expenses list returned 
Status: 200 OK

\-\-\-\-\-\-\-\-\--Endpoints Tested\-\-\-\-\-\-\-\-\--
base_url=http://localhost:3000 
{{base_url}}/customers (GET, POST, PUT,DELETE) 
{{base_url}}/creditSales (GET, POST, PUT, DELETE)
{{base_url}}/products (GET, POST, PUT, DELETE)
{{base_url}}/reports/dashboardSummary (GET) 
{{base_url}}/expenses (GET)

\-\-\-\-\-\-\-\-\--Bugs and Inconsistencies Found\-\-\-\-\-\-\-\-\--

Bug 1: Validation for Customer Name Missing
  API allows creating customer with an empty customer name
  Expected Result: 400 Bad Request
  Actual Result: Customer saved successfully (201 Created)

Bug 2: Duplicate Barcode for Product
  API allows creating multiple products with the same barcode
  Expected Result: Validation error
  Actual Result: Product saved without any error

Bug 3: Dashboard Summary API Not Working
  GET /reports/dashboardSummary returns 404
  Expected Result: Dashboard summary data
  Actual Result: Not Found error

Bug 4: No Authentication Implemented
  All APIs are accessible without login
  Expected Result: 401 Unauthorized
  Actual Result: No 401 Unauthorized response

\-\-\-\-\-\-\-\-\--Suggestions for Improvement\-\-\-\-\-\-\-\-\--

1. Input validation for all APIs
   Mandatory fields like name, barcode, and amount should not be empty
   Return 400 Bad Request for invalid data

2. Unique constraints for database
   Barcode for each product should be unique
   Duplicate data should be rejected

3. Fix dashboard summary endpoint
   /reports/dashboardSummary endpoint should return data correctly
   Should not return 404 for valid routes

4. Implement authentication and authorization
   JWT token-based authentication
   Should be implemented for sensitive routes

5. Improve error messages
   Should return meaningful error messages
   Should return reasons for validation failures

\-\-\-\-\-\-\-\-\--Conclusion\-\-\-\-\-\-\-\-\--

All the required API endpoints were tested using Postman, as required by
the assignment. Most of the basic operations, including create, update,
read, and delete, are functioning well.

However, some problems were identified during the testing process. These
problems include the absence of input validation, acceptance of
duplicates, and non-functioning API endpoints. The system does not
have adequate authentication and security mechanisms.

Therefore, it is recommended that the identified defects be addressed
before the system is deployed to production.

The testing of the Shopbook system's API was beneficial since some
important improvements are required for the system's improvement.

Shopbook Automation Testing

----Overview----
This automation test validates the Credit Sale flow of the Shopbook API.

----Test Flow----
1.Create a new customer
2.Create a credit sale for that customer
3.Retrieve the credit sale
4.Update the credit sale status to "paid"
5.Verify dashboard endpoint

----Technologies Used----
Python 3.11, Pytest, Requests library, JSON Server (Mock API)

----How to Run----

1.Start mock API server:
   json-server --watch db.json --port 3000

2.Install dependencies:
   python -m pip install -r requirements.txt

3.Run automation test:
   python -m pytest

----Design Pattern----
Page Object Model (POM) was used.
API methods are separated inside api_client.py.


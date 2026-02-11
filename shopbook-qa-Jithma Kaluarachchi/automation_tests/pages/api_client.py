import requests
import time


class ShopbookAPI:

    def __init__(self, base_url):
        self.base_url = base_url

    # -------------------------
    # Customers
    # -------------------------
    def create_customer(self, data):
        url = f"{self.base_url}/customers"
        return requests.post(url, json=data)

    # -------------------------
    # Credit Sales
    # -------------------------
    def create_credit_sale(self, data):
        url = f"{self.base_url}/creditSales"
        return requests.post(url, json=data)

    def get_credit_sale(self, sale_id, retries=3):
        """
        Get credit sale with retry (fixes connection reset issue)
        """

        url = f"{self.base_url}/creditSales/{sale_id}"

        for i in range(retries):
            try:
                response = requests.get(url, timeout=5)
                return response

            except requests.exceptions.ConnectionError:
                print(f"Retrying GET credit sale... ({i+1})")
                time.sleep(1)

        raise Exception("GET /creditSales API keeps crashing")

    def update_credit_sale(self, sale_id, data):
        url = f"{self.base_url}/creditSales/{sale_id}"
        return requests.put(url, json=data)

    # -------------------------
    # Reports
    # -------------------------
    def get_dashboard(self):
        url = f"{self.base_url}/reports/dashboardSummary"
        return requests.get(url)
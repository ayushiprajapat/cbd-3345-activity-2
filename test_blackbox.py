import unittest
import requests

class TestAPI(unittest.TestCase):

    BASE_URL = "http://localhost:5000"  

    def test_get_products(self):
        """Test /api/products endpoint for returning a product list with status 200"""
        response = requests.get(f"{self.BASE_URL}/api/products")
        self.assertEqual(response.status_code, 200)
        
        
        data = response.json()
        self.assertIsInstance(data, list)
        for product in data:
            self.assertIn("id", product)
            self.assertIn("name", product)
            self.assertIn("price", product)

    def test_post_cart_valid_request(self):
        """Test /api/cart endpoint for handling valid cart requests"""
        url = f"{self.BASE_URL}/api/cart"
        payload = {
            "cart_items": [
                {"product_id": "123", "quantity": 2},
                {"product_id": "456", "quantity": 1}
            ]
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        
        #
        data = response.json()
        self.assertIn("total", data)
        self.assertIsInstance(data["total"], (int, float))

    def test_post_cart_invalid_request(self):
        """Test /api/cart endpoint for handling invalid cart requests"""
        url = f"{self.BASE_URL}/api/cart"
        payload = {
            "cart_items": [
                {"product_id": None, "quantity": -1}
            ]
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 400)
        
        
        data = response.json()
        self.assertIn("error", data)
        self.assertEqual(data["error"], "Invalid cart data")

if __name__ == "__main__":
    unittest.main()

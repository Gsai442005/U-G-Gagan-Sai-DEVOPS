import unittest

from app import app


class FlashSaleApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_returns_sale_message(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Welcome to Big Sale!")

    def test_health_reports_healthy(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")

    def test_buy_returns_success_for_requested_user(self):
        response = self.client.get("/buy?user=student")
        payload = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(payload["status"], "success")
        self.assertEqual(payload["user"], "student")
        self.assertIn(payload["item"], ["Smartphone", "Shoes", "Headphones", "Laptop"])


if __name__ == "__main__":
    unittest.main()

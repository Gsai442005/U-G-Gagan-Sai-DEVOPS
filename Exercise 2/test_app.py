import unittest

from app import app


class FlaskAppTests(unittest.TestCase):
    def test_home_returns_expected_message(self):
        response = app.test_client().get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Hello from Flask on Kubernetes!")


if __name__ == "__main__":
    unittest.main()

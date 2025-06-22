import unittest
from app import app
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_get_topics(self):
        response = self.client.get("/topics")
        self.assertEqual(response.status_code, 200)

    def test_post_topic(self):
        payload = {
            "title": "API Test",
            "subject": "Unit",
            "notes": "API test payload"
        }
        response = self.client.post("/topics", json=payload)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)

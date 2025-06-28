import unittest
from app import app
from pymongo import MongoClient
import json

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["studysync_test"]
        app.config["TESTING"] = True

    def tearDown(self):
        self.client.drop_database("studysync_test")

    def test_post_and_get_topic(self):
        payload = {
            "title": "Integration Test",
            "subject": "Testing",
            "notes": "Integration check"
        }
        response = self.app.post("/topics", json=payload)
        self.assertEqual(response.status_code, 201)

        get_response = self.app.get("/topics")
        self.assertEqual(get_response.status_code, 200)
        data = json.loads(get_response.data)
        self.assertTrue(any(topic["title"] == "Integration Test" for topic in data))

    def tearDown(self):
        self.client.drop_database("studysync_test")
        self.client.close()  # <--- This line silences the warning

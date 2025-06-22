import unittest
from unittest.mock import MagicMock
from models import topic_model

class TestTopicModel(unittest.TestCase):
    def test_add_topic(self):
        db = MagicMock()
        data = {"title": "Mock Topic", "subject": "Mock", "notes": "Testing"}
        db.topics.insert_one.return_value.inserted_id = "mock_id"
        result = topic_model.add_topic(db, data)
        self.assertEqual(result.inserted_id, "mock_id")

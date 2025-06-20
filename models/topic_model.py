from flask import current_app as app
from bson import ObjectId

def get_all_topics(db):
    return list(db.topics.find())

def add_topic(db, data):
    data["completed"] = False
    return db.topics.insert_one(data)

def update_topic(db, topic_id, data):
    return db.topics.update_one({"_id": ObjectId(topic_id)}, {"$set": data})

def delete_topic(db, topic_id):
    return db.topics.delete_one({"_id": ObjectId(topic_id)})

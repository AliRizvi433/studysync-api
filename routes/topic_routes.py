from flask import Blueprint, request, jsonify
from models.topic_model import get_all_topics, add_topic, update_topic, delete_topic
from bson import ObjectId

routes = Blueprint('routes', __name__)

@routes.route('/topics', methods=['GET'])
def get_topics():
    topics = get_all_topics(request.db)
    for t in topics:
        t['_id'] = str(t['_id'])
    return jsonify(topics)

@routes.route('/topics', methods=['POST'])
def create_topic():
    data = request.json
    result = add_topic(request.db, data)
    return jsonify({"message": "Topic added", "id": str(result.inserted_id)}), 201

@routes.route('/topics/<id>', methods=['PUT'])
def edit_topic(id):
    data = request.json
    update_topic(request.db, id, data)
    return jsonify({"message": "Topic updated"})

@routes.route('/topics/<id>', methods=['DELETE'])
def remove_topic(id):
    delete_topic(request.db, id)
    return jsonify({"message": "Topic deleted"})

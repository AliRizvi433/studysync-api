from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from config import Config
from routes.topic_routes import routes

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient(Config.MONGO_URI)
db = client.get_default_database()

# Inject db into request
@app.before_request
def before_request():
    request.db = db

# Register routes
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)

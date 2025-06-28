from flask import Flask, request, render_template
from flask_cors import CORS
from pymongo import MongoClient
from config import Config
from routes.topic_routes import routes

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# MongoDB connection
client = MongoClient(Config.MONGO_URI)
db = client.get_default_database()

# Inject db into request
@app.before_request
def before_request():
    request.db = db

# Homepage route (must be before app.run)
@app.route('/')
def index():
    print("Rendering index.html")
    return render_template('index.html')

# Register your API routes
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)

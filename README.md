# StudySync API

![Python](https://img.shields.io/badge/python-3.12-blue)
![Flask](https://img.shields.io/badge/flask-API-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A RESTful API for topic modeling and study synchronization.

---

## 🚀 Features

- Topic modeling with custom models
- RESTful endpoints for topic management
- Easy configuration with `.env`
- Modular code structure

---

## 📦 Project Structure

```
.
├── app.py
├── config.py
├── models/
│   └── topic_model.py
├── routes/
│   └── topic_routes.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/studysync-api.git
    cd studysync-api
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv studysync
    source studysync/Scripts/activate  # On Windows
    # or
    source studysync/bin/activate      # On Unix/Mac
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure environment variables**
    - Copy `.env.example` to `.env` and update as needed.

---

## 🏃 Usage

Start the API server:

```sh
python app.py
```

The API will be available at `http://localhost:5000/`.

---

## 📚 Endpoints

- `GET /topics` — List all topics
- `POST /topics` — Create a new topic
- `GET /topics/<id>` — Get topic details
- `PUT /topics/<id>` — Update a topic
- `DELETE /topics/<id>` — Delete a topic

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests.

---
# """
# AI Customer Support Chatbot — Flask Backend
# Run: python app.py
# """

# from flask import Flask
# from flask_cors import CORS
# from routes import register_routes

# app = Flask(__name__)
# CORS(app)  # Allow frontend (different port) to call the API

# # Register all route blueprints
# register_routes(app)

# if __name__ == "__main__":
#     print("=" * 50)
#     print("  SupportAI Backend running on http://localhost:5000")
#     print("  Press CTRL+C to stop")
#     print("=" * 50)
#     app.run(debug=True, host="0.0.0.0", port=5000)


from flask import Flask
from flask_cors import CORS
from routes import register_routes

app = Flask(__name__)
CORS(app)

register_routes(app)

if __name__ == "__main__":
    print("=" * 50)
    print("SupportAI Backend running on http://localhost:5000")
    print("=" * 50)

    app.run(debug=True, host="0.0.0.0", port=5000)
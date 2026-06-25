# """
# Routes for the AI Customer Support Chatbot backend.
# """

# from flask import Blueprint, request, jsonify, session
# from utils import get_ai_response, build_messages

# chat_bp = Blueprint("chat", __name__)


# def register_routes(app):
#     app.secret_key = "support-chatbot-secret-key-change-in-production"
#     app.register_blueprint(chat_bp)


# # ─────────────────────────────────────────
# #  POST /api/chat  — Main chat endpoint
# # ─────────────────────────────────────────
# @chat_bp.route("/api/chat", methods=["POST"])
# def chat():
#     data = request.get_json(silent=True)

#     if not data or "message" not in data:
#         return jsonify({"error": "Missing 'message' field in request body."}), 400

#     user_message = data["message"].strip()
#     if not user_message:
#         return jsonify({"error": "Message cannot be empty."}), 400

#     # Frontend sends its own history; use it (stateless-friendly approach)
#     history = data.get("history", [])

#     # Build the messages list for the AI
#     messages = build_messages(history)

#     # Call the AI
#     reply, error = get_ai_response(messages)

#     if error:
#         return jsonify({"error": error}), 502

#     return jsonify({"reply": reply, "status": "ok"})


# # ─────────────────────────────────────────
# #  POST /api/clear  — Clear session
# # ─────────────────────────────────────────
# @chat_bp.route("/api/clear", methods=["POST"])
# def clear():
#     session.clear()
#     return jsonify({"status": "cleared"})


# # ─────────────────────────────────────────
# #  GET /api/health  — Health check
# # ─────────────────────────────────────────
# @chat_bp.route("/api/health", methods=["GET"])
# def health():
#     return jsonify({"status": "ok", "service": "SupportAI Backend"})


# # ─────────────────────────────────────────
# #  GET /  — Root info
# # ─────────────────────────────────────────
# @chat_bp.route("/", methods=["GET"])
# def index():
#     return jsonify({
#         "service": "SupportAI Customer Support Chatbot",
#         "version": "1.0.0",
#         "endpoints": {
#             "POST /api/chat":   "Send a message and receive an AI reply",
#             "POST /api/clear":  "Clear the conversation session",
#             "GET  /api/health": "Health check",
#         }
#     })

from flask import Blueprint, request, jsonify
from utils import get_ai_response, build_messages

chat_bp = Blueprint("chat", __name__)

def register_routes(app):
    app.register_blueprint(chat_bp)

@chat_bp.route("/")
def home():
    return jsonify({
        "service": "SupportAI Customer Support Chatbot",
        "status": "Running"
    })

@chat_bp.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    history = data.get("history", [])

    messages = build_messages(history)

    reply, error = get_ai_response(messages)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "reply": reply,
        "status": "ok"
    })

@chat_bp.route("/api/health")
def health():
    return jsonify({
        "status": "ok"
    })
# """
# Utility functions:
#   - System prompt definition
#   - Message builder
#   - Anthropic API call wrapper
# """

# import os
# import anthropic
# from dotenv import load_dotenv

# load_dotenv()

# # ─────────────────────────────────────────
# #  Anthropic client (reads ANTHROPIC_API_KEY from .env)
# # ─────────────────────────────────────────
# client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# # ─────────────────────────────────────────
# #  SYSTEM PROMPT
# # ─────────────────────────────────────────
# SYSTEM_PROMPT = """You are a friendly, professional customer support agent for SupportAI — a modern e-commerce platform.
# Your role is to help customers efficiently and warmly.

# GUIDELINES:
# - Always be polite, empathetic, and concise (2–5 sentences unless a step-by-step process is needed).
# - Use bullet points only when giving multi-step instructions.
# - If you cannot resolve something (e.g. need account access), tell the customer you'll escalate to a human agent.
# - Never fabricate order numbers, tracking codes, or personal account data.
# - Refer to the company as "we" naturally.

# TOPICS YOU HANDLE:
# 1. Account & Login — password reset, 2FA, locked accounts
# 2. Orders & Shipping — order status, tracking, delays, cancellations
# 3. Refunds & Returns — return policy (30 days), refund timelines (3–5 business days)
# 4. Billing & Subscriptions — plan changes, payment methods, invoice copies
# 5. Technical Issues — app bugs, website errors, compatibility
# 6. Product Questions — availability, specifications, recommendations
# 7. General — business hours (Mon–Fri 9am–6pm EST), contact options

# TONE: Professional but conversational. Avoid jargon. End with an offer to help further when appropriate."""


# # ─────────────────────────────────────────
# #  BUILD MESSAGES for the API
# # ─────────────────────────────────────────
# def build_messages(history: list) -> list:
#     """
#     Accepts a list like:
#       [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}, ...]
#     Returns it cleaned and validated for the Anthropic API.
#     """
#     cleaned = []
#     for msg in history:
#         role = msg.get("role", "")
#         content = msg.get("content", "").strip()
#         if role in ("user", "assistant") and content:
#             cleaned.append({"role": role, "content": content})
#     return cleaned


# # ─────────────────────────────────────────
# #  CALL ANTHROPIC API
# # ─────────────────────────────────────────
# def get_ai_response(messages: list) -> tuple:
#     """
#     Send messages to Claude and return (reply_text, error_string).
#     On success: (reply, None)
#     On failure: (None, error_message)
#     """
#     if not messages:
#         return None, "No messages provided."

#     try:
#         response = client.messages.create(
#             model="claude-sonnet-4-6",
#             max_tokens=1024,
#             system=SYSTEM_PROMPT,
#             messages=messages,
#         )

#         # Extract text from response content blocks
#         reply = " ".join(
#             block.text for block in response.content
#             if hasattr(block, "text")
#         ).strip()

#         if not reply:
#             return None, "Empty response from AI."

#         return reply, None

#     except anthropic.AuthenticationError:
#         return None, "Invalid API key. Check your ANTHROPIC_API_KEY in the .env file."

#     except anthropic.RateLimitError:
#         return None, "Rate limit reached. Please wait a moment and try again."

#     except anthropic.APIStatusError as e:
#         return None, f"Anthropic API error: {e.message}"

#     except Exception as e:
#         return None, f"Unexpected error: {str(e)}"

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are SupportAI, a professional customer support chatbot.

Rules:
- Be polite and helpful.
- Give short responses.
- Help with orders, refunds, shipping, billing and technical issues.
- If information is unavailable, ask the user for more details.
"""

def build_messages(history):

    cleaned = []

    for msg in history:

        role = msg.get("role", "")
        content = msg.get("content", "").strip()

        if role in ["user", "assistant"] and content:

            cleaned.append({
                "role": role,
                "content": content
            })

    return cleaned


def get_ai_response(messages):

    try:

        conversation = SYSTEM_PROMPT + "\n\n"

        for msg in messages:

            if msg["role"] == "user":
                conversation += f"User: {msg['content']}\n"

            elif msg["role"] == "assistant":
                conversation += f"Assistant: {msg['content']}\n"

        response = model.generate_content(conversation)

        return response.text, None

    except Exception as e:
        return None, str(e)

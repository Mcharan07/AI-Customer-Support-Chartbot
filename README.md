# AI Customer Support Chatbot

A full-stack AI-powered customer support chatbot built with:
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Backend**: Python (Flask)
- **AI**: Anthropic Claude (claude-sonnet-4-6)

---

## Project Structure

```
ai-customer-support-chatbot/
│
├── frontend/
│   ├── index.html          ← Main HTML page
│   ├── css/
│   │   └── style.css       ← All styles
│   └── js/
│       └── script.js       ← Chat logic, API calls
│
├── backend/
│   ├── app.py              ← Flask app entry point
│   ├── routes.py           ← API route definitions
│   └── utils.py            ← AI call logic + system prompt
│
├── .env                    ← API keys (never commit this)
├── requirements.txt        ← Python dependencies
└── README.md
```

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-customer-support-chatbot.git
cd ai-customer-support-chatbot
```

### 2. Set up the backend

```bash
# Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure environment variables

Edit `.env` and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_actual_api_key_here
```

Get your key from: https://console.anthropic.com/

### 4. Run the backend

```bash
cd backend
python app.py
```

Backend will start at: `http://localhost:5000`

### 5. Open the frontend

Open `frontend/index.html` in your browser directly,
OR use VS Code Live Server extension for best results.

---

## API Endpoints

| Method | Endpoint      | Description                          |
|--------|---------------|--------------------------------------|
| GET    | `/`           | API info and available endpoints     |
| POST   | `/api/chat`   | Send a message, receive AI reply     |
| POST   | `/api/clear`  | Clear the conversation session       |
| GET    | `/api/health` | Health check                         |

### POST `/api/chat` — Request body
```json
{
  "message": "How do I reset my password?",
  "history": [
    { "role": "user", "content": "Hello" },
    { "role": "assistant", "content": "Hi! How can I help?" }
  ]
}
```

### POST `/api/chat` — Response
```json
{
  "reply": "To reset your password, go to the login page and click...",
  "status": "ok"
}
```

---

## Features

- **AI-powered responses** via Anthropic Claude
- **Conversation memory** — full history sent with each message
- **Quick topic shortcuts** in the sidebar
- **Typing indicator** while AI is generating a response
- **Error handling** with user-friendly messages
- **Clear chat** button to start a fresh conversation
- **Responsive design** — works on mobile and desktop
- **Auto-resizing** message input

---

## GitHub Workflow

```bash
# Work on dev branch
git checkout -b dev

# Make changes, then commit
git add .
git commit -m "feat: add password reset flow"

# Push to remote
git push origin dev

# Merge to main when ready
git checkout main
git merge dev
git push origin main
```

---

## Environment Variables

| Variable          | Description                        | Required |
|-------------------|------------------------------------|----------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key           | Yes      |
| `FLASK_ENV`       | `development` or `production`      | No       |
| `FLASK_DEBUG`     | `true` or `false`                  | No       |
| `SECRET_KEY`      | Flask session secret key           | No       |

---

## Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend  | Python 3.10+, Flask     |
| AI Model | Anthropic Claude Sonnet |
| CORS     | flask-cors              |

---

## License

MIT License — free to use and modify.

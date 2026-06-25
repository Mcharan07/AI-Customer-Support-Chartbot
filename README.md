# 🤖 AI Customer Support Chatbot

An AI-powered customer support chatbot built using **Python (Flask)** for the backend and **HTML, CSS, JavaScript** for the frontend. The chatbot integrates with the **Google Gemini API** to provide intelligent responses to customer queries.

---

## 📌 Features

- 💬 AI-powered customer support
- ⚡ Fast and responsive interface
- 🔐 Secure API key management using `.env`
- 🌐 Flask REST API backend
- 🎨 Clean HTML, CSS & JavaScript frontend
- 📱 Responsive design

---

## 📂 Project Structure

```
ai-customer-support-chatbot/
│
├── backend/
│   ├── app.py              # Flask application
│   ├── routes.py           # API routes
│   ├── utils.py            # Helper functions
│   ├── .env                # Environment variables (Not uploaded)
│   └── venv/               # Virtual environment (Ignored)
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- Google Gemini API
- python-dotenv

### Frontend
- HTML5
- CSS3
- JavaScript

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/AI-CUSTOMER-SUPPORT-CHATBOT.git
```

```bash
cd AI-CUSTOMER-SUPPORT-CHATBOT
```

---

### Create Virtual Environment

Windows

```bash
python -m venv backend/venv
```

Activate

```bash
backend\venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file inside the `backend` folder.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

### Run the Backend

```bash
cd backend
python app.py
```

The Flask server will start on:

```
http://127.0.0.1:5000
```

---

### Open the Frontend

Open

```
frontend/index.html
```

in your browser.

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Chat Interface
- AI Responses

---

## 📖 How It Works

1. User enters a message.
2. JavaScript sends the message to the Flask backend.
3. Flask processes the request.
4. Google Gemini API generates a response.
5. The response is displayed in the chat interface.

---

## 📌 Future Improvements

- User Authentication
- Chat History
- Database Integration
- Voice Input
- Multi-language Support
- Dark Mode
- File Upload Support

---

## 👨‍💻 Author

**Charan Karthik Muppana**

B.Tech – Artificial Intelligence & Machine Learning

GitHub: https://github.com/Mcharan07

---

## 📄 License

This project is licensed under the MIT License.
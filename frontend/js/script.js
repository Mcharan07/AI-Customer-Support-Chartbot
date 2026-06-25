// ============================================================
//  AI Customer Support Chatbot — Frontend Script
//  Sends user messages to the Flask backend at /api/chat
// ============================================================

const BACKEND_URL = "http://localhost:5000/api/chat";

// ── DOM refs ──────────────────────────────────────────────
const messagesArea  = document.getElementById("messages-area");
const userInput     = document.getElementById("user-input");
const sendBtn       = document.getElementById("send-btn");
const typingBar     = document.getElementById("typing-bar");
const clearBtn      = document.getElementById("clear-btn");
const topicBtns     = document.querySelectorAll(".topic-btn");

// ── Conversation history (mirrors what backend keeps) ─────
let conversationHistory = [];
let isBusy = false;

// ─────────────────────────────────────────────────────────
//  INIT
// ─────────────────────────────────────────────────────────
window.addEventListener("DOMContentLoaded", () => {
  renderWelcomeCard();
  userInput.focus();
});

// ─────────────────────────────────────────────────────────
//  WELCOME CARD
// ─────────────────────────────────────────────────────────
function renderWelcomeCard() {
  const card = document.createElement("div");
  card.className = "welcome-card";
  card.innerHTML = `
    <div class="wc-icon">👋</div>
    <h2>Welcome to SupportAI</h2>
    <p>I'm your AI-powered support assistant. Ask me anything about<br>
       orders, refunds, billing, account issues, and more.</p>
  `;
  messagesArea.appendChild(card);

  // First bot greeting
  appendMessage(
    "Hello! I'm your support assistant, powered by AI. How can I help you today? " +
    "Feel free to ask about your order, refund, account, billing, or any other issue!",
    "bot"
  );
}

// ─────────────────────────────────────────────────────────
//  APPEND MESSAGE
// ─────────────────────────────────────────────────────────
function appendMessage(text, role) {
  const row = document.createElement("div");
  row.className = `msg-row ${role}`;

  const avatarDiv = document.createElement("div");
  avatarDiv.className = `msg-avatar ${role === "bot" ? "bot-avatar" : "user-avatar"}`;
  avatarDiv.textContent = role === "bot" ? "🤖" : "🧑";

  const contentDiv = document.createElement("div");
  contentDiv.className = "msg-content";

  const bubble = document.createElement("div");
  bubble.className = `bubble ${role === "bot" ? "bot-bubble" : "user-bubble"}`;
  bubble.textContent = text;

  const time = document.createElement("div");
  time.className = "msg-time";
  time.textContent = getTime();

  contentDiv.appendChild(bubble);
  contentDiv.appendChild(time);
  row.appendChild(avatarDiv);
  row.appendChild(contentDiv);
  messagesArea.appendChild(row);
  scrollToBottom();
  return bubble;
}

// ─────────────────────────────────────────────────────────
//  ERROR MESSAGE
// ─────────────────────────────────────────────────────────
function appendError(text) {
  const div = document.createElement("div");
  div.className = "error-bubble";
  div.textContent = "⚠️ " + text;
  messagesArea.appendChild(div);
  scrollToBottom();
}

// ─────────────────────────────────────────────────────────
//  SEND MESSAGE
// ─────────────────────────────────────────────────────────
async function sendMessage() {
  const text = userInput.value.trim();
  if (!text || isBusy) return;

  // UI lockdown
  isBusy = true;
  sendBtn.disabled = true;
  userInput.value = "";
  autoResize();

  // Show user message
  appendMessage(text, "user");

  // Track locally
  conversationHistory.push({ role: "user", content: text });

  // Typing indicator
  typingBar.style.display = "flex";
  scrollToBottom();

  try {
    const res = await fetch(BACKEND_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text, history: conversationHistory }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.error || `Server responded with ${res.status}`);
    }

    const data = await res.json();
    const reply = data.reply || "I'm sorry, I didn't get a response. Please try again.";

    conversationHistory.push({ role: "assistant", content: reply });
    appendMessage(reply, "bot");

  } catch (err) {
    console.error("Chat error:", err);
    appendError(
      err.message.includes("Failed to fetch")
        ? "Cannot reach the backend. Make sure the Flask server is running on port 5000."
        : err.message
    );
  } finally {
    typingBar.style.display = "none";
    isBusy = false;
    sendBtn.disabled = false;
    userInput.focus();
  }
}

// ─────────────────────────────────────────────────────────
//  CLEAR CHAT
// ─────────────────────────────────────────────────────────
clearBtn.addEventListener("click", async () => {
  conversationHistory = [];
  messagesArea.innerHTML = "";
  renderWelcomeCard();

  // Also clear the backend session
  try {
    await fetch("http://localhost:5000/api/clear", { method: "POST" });
  } catch (_) {}
});

// ─────────────────────────────────────────────────────────
//  QUICK TOPIC BUTTONS
// ─────────────────────────────────────────────────────────
topicBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    const msg = btn.getAttribute("data-msg");
    if (msg && !isBusy) {
      userInput.value = msg;
      sendMessage();
    }
  });
});

// ─────────────────────────────────────────────────────────
//  KEYBOARD SHORTCUTS
// ─────────────────────────────────────────────────────────
userInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// Send button click
sendBtn.addEventListener("click", sendMessage);

// ─────────────────────────────────────────────────────────
//  AUTO-RESIZE TEXTAREA
// ─────────────────────────────────────────────────────────
userInput.addEventListener("input", autoResize);

function autoResize() {
  userInput.style.height = "auto";
  userInput.style.height = Math.min(userInput.scrollHeight, 120) + "px";
}

// ─────────────────────────────────────────────────────────
//  HELPERS
// ─────────────────────────────────────────────────────────
function scrollToBottom() {
  messagesArea.scrollTop = messagesArea.scrollHeight;
}

function getTime() {
  return new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

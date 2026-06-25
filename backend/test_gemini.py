import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

try:
    response = model.generate_content("Hello")
    print(response.text)

except Exception as e:
    print("Error:", e)
    print("Waiting 30 seconds...")
    time.sleep(30)
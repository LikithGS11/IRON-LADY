import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
from flask import Flask, render_template, request, jsonify

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# 🔑 Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")
genai.configure(api_key=api_key)

# Knowledge base for fallback
faq_data = {
    "about": "Iron Lady is a leadership and transformation organization that empowers women to embrace leadership roles with confidence. It offers structured programs, coaching, and workshops to help women overcome barriers and build leadership skills.",
    "programs": "Iron Lady offers leadership programs designed to empower women in leadership roles, including corporate programs, public workshops, and one-on-one coaching sessions.",
    "duration": "The program duration varies. Leadership workshops are usually short-term (2–3 days), while deep coaching and corporate engagements can run for weeks or months.",
    "mode": "Iron Lady’s programs are conducted both online and offline, depending on the program type.",
    "certificates": "Yes ✅ Certificates are provided upon completion of selected leadership programs and workshops.",
    "mentors": "The mentors are experienced leaders, industry experts, and certified coaches in leadership development."
}

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # 👋 Greetings
    if any(greet in user_input for greet in ["hi", "hello", "hey", "good morning", "good evening"]):
        return "Hello 👋 I'm Iron Lady’s assistant. I can help you with details about Iron Lady, our mission, and our leadership programs. What would you like to know?"

    # 🙏 Farewell
    if any(bye in user_input for bye in ["bye", "exit", "quit", "thank you"]):
        return "Thank you for connecting with Iron Lady 💡. Wishing you success in your leadership journey! 🚀"

    # ❓ About the company
    if "what is iron lady" in user_input or "about iron lady" in user_input or "what do you do" in user_input or "company" in user_input:
        return faq_data["about"]

    # ❓ Programs
    if "program" in user_input or "courses" in user_input or "training" in user_input:
        return faq_data["programs"]

    # ❓ Duration
    if "duration" in user_input or "how long" in user_input or "time" in user_input:
        return faq_data["duration"]

    # ❓ Mode
    if "online" in user_input or "offline" in user_input or "mode" in user_input:
        return faq_data["mode"]

    # ❓ Certificates
    if "certificate" in user_input or "certification" in user_input or "proof" in user_input:
        return faq_data["certificates"]

    # ❓ Mentors
    if "mentor" in user_input or "coach" in user_input or "trainer" in user_input:
        return faq_data["mentors"]

    # 🧠 Try Gemini for smarter replies
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"""
        You are Iron Lady's official chatbot. 
        Answer only about Iron Lady, its mission, and its leadership programs.
        Be warm, professional, and concise. 

        Reference info:
        - About: {faq_data['about']}
        - Programs: {faq_data['programs']}
        - Duration: {faq_data['duration']}
        - Mode: {faq_data['mode']}
        - Certificates: {faq_data['certificates']}
        - Mentors: {faq_data['mentors']}

        User question: {user_input}
        """
        response = model.generate_content(prompt)
        return response.text.strip()

    except ResourceExhausted:
        return "I'm sorry, I cannot fetch live responses right now. Please ask about Iron Lady, our programs, duration, mode, certificates, or mentors."

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Chatbot API route using the original chatbot logic
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message', '')
    response_text = get_bot_response(user_input)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)

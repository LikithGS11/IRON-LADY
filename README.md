# 🚀 Iron Lady Chatbot Web Application ![IRON LADY](https://img.shields.io/badge/IRON%20LADY-AI%20Chatbot-%23e95420?logo=python&logoColor=white&style=for-the-badge) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=github)

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="Python" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" alt="Flask" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="JavaScript" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="HTML5" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="CSS3" />
</div>

---

## ✨ Overview

**Iron Lady** is a modern web application powered by Flask and enhanced with an AI chatbot based on Google Gemini. It’s designed to assist, inspire, and inform users about leadership programs for women, all through a sleek, animated, responsive interface.

---

## 🎯 Features

- 🤖 **AI Chatbot**: Powered by Google Gemini API for dynamic, helpful responses.
- 🔄 **Fallback Handling**: Answers common queries with reliable static responses.
- 💻 **Responsive Design**: Animated sections for programs, audience, and more.
- ⚡ **Flask Backend**: RESTful API for real-time chatbot interactions.
- 🧪 **Testing**: Pytest-based unit tests ensure robust performance.

---

## 📁 Project Structure

```text
CHATBOT/
├── app.py                 # Main Flask application
├── ironlady.py            # Standalone chatbot script
├── test_app.py            # Unit tests for the Flask app
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── chatbot.js
│   └── images/            # Logos, icons, etc.
├── templates/
│   └── index.html
└── README.md
```

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/LikithGS11/IRON-LADY.git
   cd IRON-LADY
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the root directory:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

---

## 🚦 Usage

- **Run the Web Application**
  ```bash
  python app.py
  ```
  Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and click the chatbot icon in the corner!

- **Run the Standalone Chatbot**
  ```bash
  python ironlady.py
  ```

- **Run Tests**
  ```bash
  pytest test_app.py
  ```

---

## 📡 API Endpoint

- **POST /chatbot**
  - Request:
    ```json
    { "message": "What is Iron Lady?" }
    ```
  - Response:
    ```json
    { "response": "Iron Lady is a leadership and transformation organization..." }
    ```

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000?logo=flask)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3)
![Google Gemini](https://img.shields.io/badge/-Google%20Gemini-4285F4?logo=google)

---

## 💡 Notes

- The standalone script (`ironlady.py`) uses a hardcoded API key for demonstration—use environment variables in production!
- The web UI leverages Google Fonts, Lottie animations, and visually engaging sections for a great user experience.

---

## 🤝 Contributing

- Fork, star, and submit pull requests for enhancements!
- Report bugs or suggest features via GitHub issues.

---

## 📄 License

This project is for educational and demonstration purposes. Please adhere to the Google Gemini API terms of service.

---

<div align="center">
  <img src="https://lottie.host/7d0e7b2e-ironlady-chatbot-ani.json" alt="Chatbot Animation" height="100"/>
  <img src="https://lottie.host/7d0e7b2e-women-leadership-ani.json" alt="Leadership Animation" height="100"/>
  <img src="https://lottie.host/7d0e7b2e-ai-ani.json" alt="AI Animation" height="100"/>
</div>

---

> Made with ❤️ by the Iron Lady team
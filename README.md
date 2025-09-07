# Iron Lady Chatbot Web Application

## Overview

Iron Lady is a Flask-based web application featuring an AI-powered chatbot designed to assist users with information about leadership programs for women. The chatbot leverages Google's Gemini AI for intelligent responses and provides a user-friendly interface for inquiries related to Iron Lady's mission, programs, duration, mode, certificates, and mentors.

The application includes a responsive website with sections highlighting the organization's offerings, target audience, and features. The chatbot is integrated into the website for seamless user interaction.

## Features

- **AI-Powered Chatbot**: Uses Google Gemini API for generating responses based on predefined knowledge about Iron Lady.
- **Fallback Responses**: Handles common queries with static responses for reliability.
- **Responsive Web Interface**: Modern, animated website with sections for programs, audience, and more.
- **Flask Backend**: RESTful API endpoint for chatbot interactions.
- **Testing**: Includes pytest-based unit tests for the Flask application.

## Project Structure

```
CHATBOT/
├── app.py                 # Main Flask application
├── ironlady.py            # Standalone chatbot script
├── test_app.py            # Unit tests for the Flask app
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Stylesheet for the website
│   ├── js/
│   │   └── chatbot.js     # JavaScript for chatbot frontend
│   └── images/            # Static images (logos, icons, etc.)
├── templates/
│   └── index.html         # HTML template for the homepage
└── README.md              # This file
```

## Installation

1. **Clone or Download the Repository**:
   - Ensure you have the project files in your working directory.

2. **Install Python Dependencies**:
   - Make sure you have Python 3.7+ installed.
   - Install the required packages using pip:
     ```
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Obtain an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

### Running the Web Application

1. Navigate to the project directory.
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your web browser and go to `http://127.0.0.1:5000/` to access the website.
4. Click the chatbot icon in the bottom-right corner to interact with the chatbot.

### Running the Standalone Chatbot

- Execute the standalone script:
  ```
  python ironlady.py
  ```
- Type your queries in the console. Type 'exit' or 'bye' to quit.

### Running Tests

- Run the unit tests using pytest:
  ```
  pytest test_app.py
  ```

## API Endpoint

- **POST /chatbot**: Accepts JSON with a 'message' field and returns a JSON response with the chatbot's reply.
  - Example request:
    ```json
    {
      "message": "What is Iron Lady?"
    }
    ```
  - Example response:
    ```json
    {
      "response": "Iron Lady is a leadership and transformation organization..."
    }
    ```

## Dependencies

- **Flask**: Web framework for the application.
- **python-dotenv**: For loading environment variables.
- **google-generativeai**: Google's Generative AI library for Gemini API.
- **google-api-core**: Core library for Google APIs.
- **pytest**: Testing framework for unit tests.

## Notes

- The standalone script (`ironlady.py`) has a hardcoded API key for demonstration purposes. In production, use environment variables as in `app.py`.
- Ensure your API key has the necessary permissions for the Gemini API.
- The website uses Google Fonts for typography and includes animations for a better user experience.

## Contributing

- Feel free to fork the repository and submit pull requests for improvements.
- Report issues or suggest features via GitHub issues.

## License

This project is for educational and demonstration purposes. Please check the terms of service for the Google Gemini API.

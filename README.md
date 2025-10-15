# Healthcare Symptom Checker

This project is a web-based symptom checker that uses a Large Language Model (LLM) to suggest possible conditions and recommend next steps based on user-input symptoms.

**Disclaimer:** This tool is for educational purposes only and is not a substitute for professional medical advice.

## Features
- Accepts symptom descriptions via a simple web interface.
- Sends symptoms to a backend API.
- Uses the Google Gemini LLM to generate potential conditions and recommendations.
- Displays the AI-generated response to the user.

## Tech Stack
- **Backend**: Python, Flask
- **LLM**: Google Gemini API
- **Frontend**: HTML, CSS, JavaScript (Optional)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd symptom-checker
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create a `.env` file** in the root directory and add your API key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
5.  **Run the Flask application:**
    ```bash
    flask run
    ```
The application will be available at `http://127.0.0.1:5000`.
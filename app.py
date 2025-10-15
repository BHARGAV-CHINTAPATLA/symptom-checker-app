import os
import json
from datetime import datetime
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")
genai.configure(api_key=api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def symptom_check():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms')

        if not symptoms or not isinstance(symptoms, str) or len(symptoms) > 1000:
            return jsonify({"error": "Invalid input."}), 400

        generation_config = genai.GenerationConfig(response_mime_type="application/json")
        model = genai.GenerativeModel('models/gemini-2.5-flash', generation_config=generation_config)
        
        prompt = f"""
        Analyze the user's symptoms and return a single, valid JSON object with the exact nested schema defined below. Do not deviate from this structure.
        Context: Today is {datetime.now().strftime('%Y-%m-%d')}. User is in Vijayawada, India.
        Symptoms: "{symptoms}"

        **JSON Output Schema:**
        {{
          "analysis": {{
            "severity_assessment": "(String) Must be 'Low', 'Moderate', or 'High'",
            "confidence_score": "(String) Must be 'Low', 'Medium', or 'High'",
            "confidence_justification": "(String) Briefly explain the confidence score."
          }},
          "guidance": {{
            "urgent_care_needed": "(Array of Strings) List specific 'red flag' symptoms requiring immediate attention. If none, return an empty array [].",
            "general_recommendations": "(Array of Strings) List non-urgent self-care advice."
          }},
          "medical_information": {{
            "possible_conditions": "(Array of Strings) List 3-4 likely conditions."
          }},
          "disclaimer": "(String) Must be the exact text: 'This is for informational purposes only and is not a substitute for professional medical advice. Please consult a healthcare provider for a diagnosis.'"
        }}
        """

        response = model.generate_content(prompt)
        response_data = json.loads(response.text)
        
        return jsonify(response_data), 200

    except json.JSONDecodeError:
        return jsonify({"error": "The AI returned an invalid JSON structure. Please try again."}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)


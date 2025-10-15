import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    # Get the API key from the environment
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY was not found in your .env file.")
    else:
        # Configure the generative AI library
        genai.configure(api_key=api_key)
        
        print("API key configured successfully. Fetching available models...\n")
        
        # List all models and find the ones that can generate content
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Found a usable model: {m.name}")

except Exception as e:
    print(f"An error occurred. This could be an issue with your API key or network.")
    print(f"Error details: {e}")
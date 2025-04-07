# Configuration settings like CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai
# Load environment variables from .env file
load_dotenv()

class Settings:
    allowed_origins = os.getenv("ALLOWED_ORIGINS")
    ai_api_key = os.getenv("AI_API_KEY")
    
    api_title = "Sales AI API"
    api_version = "1.0.0"

    # Get the absolute path of the file dynamically 
    file_path = ('../dummyData.json')

    # Initialize Google GenAI (replace with your actual API key)
    genai.configure(api_key=ai_api_key)
    # Load the available models (for debugging and finding the right name)
    # print("Available models:")
    # for model_info in genai.list_models():
    #     print(f"- Name: {model_info.name}, Supported Methods: {model_info.supported_generation_methods}")
 
    # Instantiate the model you found to be available
    model = genai.GenerativeModel(
         model_name='gemini-1.5-pro',
         generation_config={
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            },
         )

    
settings = Settings()
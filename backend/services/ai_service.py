from config import settings

class AIService:
    def get_ai_response(self, question: str, data: dict):
        """
        Generates an AI response using Google GenAI based on the question and provided data.
        """
        print(data)
        prompt = f"Based on the following data: {data}\nAnswer the question: {question}"
        try:
            response = settings.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating AI response: {e}")
            return None

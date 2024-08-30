import vertexai
from vertexai.generative_models import (
    GenerativeModel,
)

class VertexAIModel:
    def __init__(self, project, location, model):
        vertexai.init(project=project, location=location)
        self.client = GenerativeModel(model)

    def generate_text(self, prompt):
        try:
            print("Asking LLM...")
            response = self.client.generate_content(prompt)
            return response.candidates[0].content.parts[0].text
        except Exception as e:
            raise Exception(f"Error invoking LLM: {e}")


if __name__ == '__main__':
    model = VertexAIModel(project="riddhi-bot-test", location="us-central1", model="gemini-1.5-pro")
    print(model.generate_text("How is the weather in Seattle?"))
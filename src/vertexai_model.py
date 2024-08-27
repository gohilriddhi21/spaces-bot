from langchain_google_genai import ChatGoogleGenerativeAI

class VertexAIModel:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro")

    def generate_text(self, prompt):
        try:
            print("Asking LLM...")
            result = self.llm.invoke(prompt)
            return result.content
        except Exception as e:
            raise Exception(f"Error invoking LLM: {e}")

if __name__ == '__main__':
    model = VertexAIModel()
    print(model.generate_text("How is the weather in Seattle?"))
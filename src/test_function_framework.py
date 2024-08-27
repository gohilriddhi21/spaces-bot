from typing import Any, Mapping
import functions_framework
from flask import Request
from vertexai_model import VertexAIModel

model = VertexAIModel()

def process_message(message):
    print(f"Processing message: {message}")
    if message.lower() in ['hello', 'hi', 'hey']:
        return 'Hi there!'
    else:
        return model.generate_text(message)


@functions_framework.http
def chat(req: Request) -> Mapping[str, Any]:
  if req.method == "GET":
    return "Hello! This function must be called from Google Chat."

  data = req.get_json()
  print(f"\nRequest: {data}")
  
  prompt = data["message"]
  msg = process_message(prompt)
  print(f"Response: {msg}")
  cards = {
    "text": msg
  }

  return cards
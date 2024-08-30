import re
from typing import Any, Mapping
import functions_framework
from flask import Request
from vertextai_model import VertexAIModel

model = VertexAIModel(project="riddhi-bot-test", location="us-central1", model="gemini-1.5-pro")

def process_message(message):
    print(f"Processing message: {message}")
    prompt = re.sub(r'@\w+', '', message["text"]).strip()
    if prompt.lower() in ['hello', 'hi', 'hey']:
        return 'Hi there!'
    else:
        return model.generate_text(prompt)


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
from flask import Flask, request, jsonify
from vertextai_model import VertexAIModel

app = Flask(__name__)
model = VertexAIModel()

def process_message(message):
    if message.lower() == 'hello':
        return 'Hi there!'
    else:
        return model.generate_text(message)

@app.route('/', methods=['GET'])
def handle_message():
    data = request.get_json()
    message = data['message']
    response = process_message(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=8080, debug=True)
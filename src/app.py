from flask import Flask, request, jsonify

app = Flask(__name__)

def process_message(message):
    if message.lower() == 'hello':
        return 'Hi there!'
    else:
        return "I don't understand that. Try saying 'hello'."

@app.route('/messages', methods=['POST'])
def handle_message():
    data = request.get_json()
    message = data['message']
    response = process_message(message)
    return jsonify({'response': response})

from flask import Flask, request, jsonify, render_template

from helper.openai_api import chat_complition

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(
        {
            'status': 'OK',
            'message': 'Application is working okay.',
            'video_url': 'https://youtu.be/y9NRLnPXsb0'
        }
    )


@app.route('/chat')
def chat():
    return render_template('index.html')


@app.route('/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        data = request.get_json()
        message = data['message']
        result = chat_complition(message)
        if result['status'] == 1:
            return jsonify(
                {
                    'status': 1,
                    'response': result['response']
                }
            )
    except:
        pass
    return jsonify(
                {
                    'status': 0,
                    'response': ''
                }
            )

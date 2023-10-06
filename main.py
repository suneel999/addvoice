from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1/voices/add"
API_KEY = "e327fdf320043677a512f1b0dade8403"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    accent = request.form['accent']
    description = request.form['description']
    audio_file = request.files['audio']

    labels = json.dumps({"accent": accent})

    files = {'files': (audio_file.filename, audio_file.stream, audio_file.content_type)}

    data = {
        'name': name,
        'labels': labels,
        'description': description
    }

    headers = {
        "Accept": "application/json",
        "xi-api-key": API_KEY
    }

    response = requests.post(ELEVENLABS_API_URL, headers=headers, data=data, files=files)

    return response.text

if __name__ == '__main__':
    app.run(debug=True)

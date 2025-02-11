from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    response_data = request.get_json()
    text = response_data.get('text', '')
    result = emotion_detector(text)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

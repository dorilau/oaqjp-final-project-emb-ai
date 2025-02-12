"""
This module contains an emotion detection function and a function that formats its response.
"""
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


def format_emotion_response(emotion_scores):
    """
    This function formats the response.
    """
    anger = emotion_scores.get('anger', 0)
    disgust = emotion_scores.get('disgust', 0)
    fear = emotion_scores.get('fear', 0)
    joy = emotion_scores.get('joy', 0)
    sadness = emotion_scores.get('sadness', 0)
    dominant_emotion = emotion_scores.get('dominant_emotion', '')

    if dominant_emotion == "None":
        return "Invalid text! Please try again."

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    This function detection emotions based on input text.
    """
    data = request.get_json()
    text = data.get('text', '').strip()
    result = emotion_detector(text)
    formatted_response = format_emotion_response(result)

    return jsonify({"message": formatted_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
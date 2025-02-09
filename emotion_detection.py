from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/emotion_detector', methods=['POST'])
def emotion_detector():
    text_to_analyse = request.json.get("text", "")
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {"raw_document": {"text": text_to_analyse}}

    if not text_to_analyse:
        return jsonify({"error": "Please provide text for analysis"}), 404

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()

    emotions = response_data.get("emotions", {})
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }
    dominant_score = max(emotion_scores, key=emotion_scores.get)

    result = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_score
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

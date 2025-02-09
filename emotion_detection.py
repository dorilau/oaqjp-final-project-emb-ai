from flask import Flask, request,jsonify
import requests

app = Flask (__name__)


@app.route('/emotion_detector', methods=['POST'])
def emotion_detector():
    text_to_analyse = request.json.get ("text", "")
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload ={"raw_document": {"text": text_to_analyse}}

    if not text_to_analyse:
        return jsonify({"error": "Please provide text for analysis"}, 404)

    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()


if __name__ == "__main__":
    app.run (debug= True)
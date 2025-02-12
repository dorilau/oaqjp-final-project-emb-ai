import pytest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotions:

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        assert result['dominant_emotion'] == "joy"

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        assert result['dominant_emotion'] == "anger"

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        assert result['dominant_emotion'] == "disgust"

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        assert result['dominant_emotion'] == "sadness"

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        assert result['dominant_emotion'] == "fear"

from config.settings import ASPECTS
from transformers import pipeline


class AspectClassifier:
    def __init__(self):
        self._model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def classify(self, text: str) -> str:
        result = self._model(text, candidate_labels=ASPECTS)
        return result["labels"][0]
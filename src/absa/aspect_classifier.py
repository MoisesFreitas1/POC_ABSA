from config.settings import ASPECTS
from transformers import pipeline


class AspectClassifier:
    def __init__(self):
        self._zero_shot = None

    def classify(self, text: str) -> str:
        aspect = self._keyword_match(text)
        if aspect:
            return aspect
        return self._zero_shot_classify(text)

    def _keyword_match(self, text: str) -> str | None:
        lowered = text.lower()
        for aspect, keywords in ASPECTS.items():
            if any(kw in lowered for kw in keywords):
                return aspect
        return None

    def _zero_shot_classify(self, text: str) -> str:
        if self._zero_shot is None:
            self._zero_shot = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        result = self._zero_shot(text, candidate_labels=list(ASPECTS.keys()))
        return result["labels"][0]
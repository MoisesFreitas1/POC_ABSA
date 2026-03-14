from pysentimiento import create_analyzer


class SentimentAnalyzer:
    _LABEL_MAP = {"POS": "positivo", "NEU": "neutro", "NEG": "negativo"}

    def __init__(self):
        self._model = create_analyzer(task="sentiment", lang="pt")

    def analyze(self, text: str) -> dict:
        result = self._model.predict(text)
        label = self._LABEL_MAP.get(result.output, result.output)
        confidence = round(max(result.probas.values()), 4)
        return {
            "sentimento": label,
            "confiança_modelo": confidence,
        }
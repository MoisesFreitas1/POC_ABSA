from tqdm import tqdm
from config.settings import MIN_REVIEW_LENGTH
from src.scraper import PlayStoreScraper
from src.absa import AspectClassifier, SentimentAnalyzer


class ABSAPipeline:
    def __init__(self, app_id: str = None):
        self._scraper = PlayStoreScraper(app_id) if app_id else PlayStoreScraper()
        self._classifier = AspectClassifier()
        self._analyzer = SentimentAnalyzer()

    def run(self) -> list[dict]:
        reviews = self._scraper.fetch_reviews()
        valid = [r for r in reviews if self._is_valid(r)]
        return [self._process(r) for r in tqdm(valid, desc="Processing reviews")]

    def _is_valid(self, review: dict) -> bool:
        text = review.get("text") or ""
        return len(text.strip()) >= MIN_REVIEW_LENGTH

    def _process(self, review: dict) -> dict:
        text = review["text"]
        sentiment = self._analyzer.analyze(text)
        return {
            "texto_original": text,
            "aspecto_detectado": self._classifier.classify(text),
            "sentimento": sentiment["sentimento"],
            "confiança_modelo": sentiment["confiança_modelo"],
        }
from src.scraper import PlayStoreScraper
from src.absa import AspectClassifier, SentimentAnalyzer

scraper = PlayStoreScraper()
classifier = AspectClassifier()
analyzer = SentimentAnalyzer()

reviews = scraper.fetch_reviews()

for review in reviews[:50]:
    text = review["text"]
    aspect = classifier.classify(text)
    sentiment = analyzer.analyze(text)
    print(f"Texto     : {text}")
    print(f"Aspecto   : {aspect}")
    print(f"Sentimento: {sentiment['sentimento']} ({sentiment['confiança_modelo']})")
    print("-" * 60)
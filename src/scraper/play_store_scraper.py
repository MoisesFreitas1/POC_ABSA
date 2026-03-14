from google_play_scraper import reviews, Sort
from config.settings import TARGET_APP_ID, SCRAPER_LANG, SCRAPER_COUNTRY, SCRAPER_COUNT


class PlayStoreScraper:
    def __init__(self, app_id: str = TARGET_APP_ID):
        self.app_id = app_id

    def fetch_reviews(self) -> list[dict]:
        result, _ = reviews(
            self.app_id,
            lang=SCRAPER_LANG,
            country=SCRAPER_COUNTRY,
            sort=Sort.MOST_RELEVANT,
            count=SCRAPER_COUNT,
        )
        return [self._parse(r) for r in result]

    def _parse(self, raw: dict) -> dict:
        return {
            "review_id": raw.get("reviewId"),
            "text": raw.get("content"),
            "rating": raw.get("score"),
            "date": str(raw.get("at")),
        }
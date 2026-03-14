from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_OUTPUT_DIR = BASE_DIR / "data" / "output"
DATA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET_APP_ID = "com.duolingo"
SCRAPER_LANG = "pt"
SCRAPER_COUNTRY = "br"
SCRAPER_COUNT = 200
MIN_REVIEW_LENGTH = 20

ASPECTS = [
    "Usabilidade",
    "Conteúdo Didático",
    "Performance Técnica",
    "Engajamento",
]
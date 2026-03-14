from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_OUTPUT_DIR = BASE_DIR / "data" / "output"
DATA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET_APP_ID = "com.duolingo"
SCRAPER_LANG = "pt"
SCRAPER_COUNTRY = "br"
SCRAPER_COUNT = 200

ASPECTS = {
    "Usabilidade": ["interface", "fácil", "design", "navegação", "intuitivo", "usability", "easy", "layout"],
    "Conteúdo Didático": ["aula", "conteúdo", "material", "explicação", "didático", "lesson", "content", "course"],
    "Performance Técnica": ["lento", "travou", "crash", "bug", "erro", "carregamento", "slow", "freeze", "load"],
    "Engajamento": ["motivação", "gamificação", "recompensa", "viciante", "divertido", "fun", "streak", "reward"],
}
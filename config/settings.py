from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_OUTPUT_DIR = BASE_DIR / "data" / "output"
DATA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET_APP_ID = "com.duolingo"
SCRAPER_LANG = "pt"
SCRAPER_COUNTRY = "br"
SCRAPER_COUNT = 200

ASPECTS = {
    "Usabilidade": ["interface", "fácil", "difícil", "design", "navegação", "intuitivo", "layout", "menu", "botão", "tela"],
    "Conteúdo Didático": ["aula", "conteúdo", "material", "explicação", "didático", "lição", "lições", "superficial", "fluência", "aprender", "aprendizado", "exercício"],
    "Performance Técnica": ["lento", "travou", "travando", "crash", "bug", "erro", "carregamento", "instável", "fecha", "reinicia", "offline"],
    "Engajamento": ["motivação", "gamificação", "recompensa", "viciante", "divertido", "streak", "entediante", "empolgante", "desafio", "pontos"],
}
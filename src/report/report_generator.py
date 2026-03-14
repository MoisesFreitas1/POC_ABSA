import pandas as pd
from config.settings import DATA_OUTPUT_DIR


class ReportGenerator:
    def __init__(self, filename: str = "absa_report"):
        self._csv_path = DATA_OUTPUT_DIR / f"{filename}.csv"

    def generate(self, results: list[dict]) -> None:
        df = pd.DataFrame(results)
        df.to_csv(self._csv_path, index=False, encoding="utf-8-sig")
        print(f"Relatório salvo em: {self._csv_path}")
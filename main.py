from src.pipeline import ABSAPipeline
from src.report import ReportGenerator

pipeline = ABSAPipeline()
results = pipeline.run()

report = ReportGenerator()
report.generate(results)
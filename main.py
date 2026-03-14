from src.pipeline import ABSAPipeline

pipeline = ABSAPipeline()
results = pipeline.run()

print(f"Total processados: {len(results)}")
for r in results[:3]:
    print(r)
    print("-" * 60)
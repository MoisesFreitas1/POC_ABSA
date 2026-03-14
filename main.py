import argparse
from src.pipeline import ABSAPipeline
from src.report import ReportGenerator


def parse_args():
    parser = argparse.ArgumentParser(description="ABSA Pipeline for app reviews")
    parser.add_argument("--app-id", type=str, help="Google Play app ID")
    parser.add_argument("--output", type=str, default="absa_report", help="Output filename (without extension)")
    return parser.parse_args()


def main():
    args = parse_args()
    print("Starting ABSA pipeline...")

    pipeline = ABSAPipeline(app_id=args.app_id)
    results = pipeline.run()
    print(f"Processed {len(results)} reviews.")

    report = ReportGenerator(filename=args.output)
    report.generate(results)
    print("Done.")


if __name__ == "__main__":
    main()
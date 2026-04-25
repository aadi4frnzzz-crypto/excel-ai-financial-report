#!/usr/bin/env python3
"""
Excel AI Financial Report Generator
Usage: python main.py --file data/sample_financials.csv --output report.html
"""

import argparse
import os
from pathlib import Path
from dotenv import load_dotenv

from analyzer import DataAnalyzer
from chart_generator import ChartGenerator
from ai_summary import AISummary
from report_builder import ReportBuilder

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="AI-powered Excel financial report generator")
    parser.add_argument("--file", required=True, help="Path to CSV or XLSX file")
    parser.add_argument("--output", default="report.html", help="Output HTML report path")
    parser.add_argument("--no-ai", action="store_true", help="Skip AI summary (no API key needed)")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return

    print(f"📂 Loading: {file_path.name}")
    analyzer = DataAnalyzer(file_path)
    stats = analyzer.analyze()
    print(f"✅ Analyzed {stats['row_count']} rows, {stats['numeric_cols']} numeric columns")

    print("📈 Generating charts...")
    chart_gen = ChartGenerator(analyzer.df, stats)
    charts = chart_gen.generate_all()
    print(f"✅ Generated {len(charts)} charts")

    ai_insight = ""
    if not args.no_ai and os.getenv("OPENAI_API_KEY"):
        print("🤖 Generating AI summary...")
        ai_summary = AISummary(stats)
        ai_insight = ai_summary.generate()
        print("✅ AI summary ready")
    else:
        print("⚠️  Skipping AI summary (use --no-ai flag or set OPENAI_API_KEY)")

    print("📄 Building report...")
    builder = ReportBuilder(stats, charts, ai_insight)
    builder.build(args.output)
    print(f"\n🎉 Report saved: {args.output}")
    print(f"   Open with: open {args.output}")


if __name__ == "__main__":
    main()

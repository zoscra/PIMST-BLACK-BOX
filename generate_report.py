#!/usr/bin/env python3
"""
PIMST Black Box - Quick Report Generator

Simple script to generate visual reports from benchmark data.
No coding knowledge required - just run this script!

Usage:
    python generate_report.py
    python generate_report.py --input benchmarks/data/your_data.json
    python generate_report.py --output custom_report.html
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from report_generator import BenchmarkReportGenerator


def main():
    """Generate benchmark report from command line."""
    parser = argparse.ArgumentParser(
        description='Generate PIMST vs LKH-3 benchmark comparison reports'
    )
    parser.add_argument(
        '--input', '-i',
        default='benchmarks/data/example_atsp_results.json',
        help='Input JSON file with benchmark data (default: example data)'
    )
    parser.add_argument(
        '--output', '-o',
        default='benchmark_report.html',
        help='Output HTML file name (default: benchmark_report.html)'
    )
    parser.add_argument(
        '--output-dir', '-d',
        default='reports',
        help='Output directory for reports (default: reports/)'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("  PIMST BLACK BOX - REPORT GENERATOR")
    print("=" * 60)
    print()
    print(f"📂 Input file:  {args.input}")
    print(f"📄 Output file: {args.output_dir}/{args.output}")
    print()
    print("⏳ Generating report...")
    print()

    try:
        generator = BenchmarkReportGenerator(args.input, args.output_dir)
        output_path = generator.generate_html_report(args.output)

        print()
        print("=" * 60)
        print("✅ SUCCESS!")
        print("=" * 60)
        print()
        print(f"📊 Report generated: {output_path}")
        print()
        print("🌐 To view the report:")
        print(f"   Open '{output_path}' in your web browser")
        print()
        print("💡 Tip: You can double-click the HTML file to open it")
        print()

    except FileNotFoundError:
        print()
        print("❌ ERROR: Input file not found!")
        print(f"   Could not find: {args.input}")
        print()
        print("💡 Available example data:")
        print("   benchmarks/data/example_atsp_results.json")
        print()
        sys.exit(1)

    except Exception as e:
        print()
        print(f"❌ ERROR: {e}")
        print()
        sys.exit(1)


if __name__ == "__main__":
    main()

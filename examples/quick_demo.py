#!/usr/bin/env python3
"""
Quick Demo: Generate a Sample Benchmark Report

This script demonstrates how to quickly generate a benchmark comparison report.
Perfect for learning how the tool works!
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from report_generator import BenchmarkReportGenerator


def main():
    """Run a quick demonstration."""
    print("\n" + "=" * 60)
    print("  PIMST BLACK BOX - QUICK DEMO")
    print("=" * 60)
    print()
    print("This demo will generate a benchmark comparison report")
    print("showing PIMST performance vs LKH-3 on ATSP instances.")
    print()
    print("-" * 60)
    print()

    # Set up paths
    project_root = Path(__file__).parent.parent
    data_file = project_root / "benchmarks" / "data" / "example_atsp_results.json"
    output_dir = project_root / "reports"

    print(f"📂 Using data: {data_file.name}")
    print(f"📁 Output dir:  {output_dir}")
    print()
    print("⏳ Generating report...")
    print()

    # Generate report
    generator = BenchmarkReportGenerator(str(data_file), str(output_dir))
    output_path = generator.generate_html_report("demo_report.html")

    print()
    print("=" * 60)
    print("  ✅ DEMO COMPLETE!")
    print("=" * 60)
    print()
    print(f"📊 Report saved to: {output_path}")
    print()
    print("🌐 To view the report:")
    print(f"   1. Open your web browser")
    print(f"   2. Navigate to: {output_path}")
    print(f"   3. Or drag and drop the file into your browser")
    print()
    print("🎓 The report shows:")
    print("   • Interactive charts comparing PIMST vs LKH-3")
    print("   • Quality and time improvements")
    print("   • Detailed results for 15 ATSP instances")
    print("   • Professional design ready for presentations")
    print()
    print("💡 No code is shown - perfect for teaching!")
    print()
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()

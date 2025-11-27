# Quick Start Guide

Get started with PIMST Black Box in 3 simple steps!

## Step 1: Run the Demo

```bash
python examples/quick_demo.py
```

This generates a sample report using included benchmark data.

## Step 2: View the Report

Open the generated file in your web browser:

```
reports/demo_report.html
```

You'll see:
- 📊 Interactive charts
- 📈 Performance comparisons
- 🏆 Summary statistics
- 📋 Detailed results table

## Step 3: Use Your Own Data

1. **Create your data file** (JSON format)
   - Copy `benchmarks/data/example_atsp_results.json` as a template
   - Replace with your benchmark results

2. **Generate your report**
   ```bash
   python generate_report.py --input your_data.json
   ```

3. **Share or present** the HTML report

## What's Next?

- Read the [User Guide](docs/user_guide.md) for detailed instructions
- Check the [Benchmark Format](benchmarks/README.md) for data specifications
- Customize reports by modifying `src/report_generator.py`

## Example Data Included

The demo uses real benchmark data comparing PIMST with LKH-3:
- 15 ATSP instances (ftv33 to ftv150)
- Problem sizes from 33 to 150 nodes
- Shows quality and time improvements

## Need Help?

- See [docs/user_guide.md](docs/user_guide.md)
- Check the examples directory
- Open an issue on GitHub

---

**That's it!** You're ready to create professional benchmark reports.

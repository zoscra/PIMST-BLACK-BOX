# PIMST Black Box - User Guide

## Overview

PIMST Black Box is a tool for generating professional benchmark comparison reports. It takes your benchmark results and creates beautiful, interactive HTML reports that you can use for presentations, papers, or teaching.

## What Does It Do?

- **Visualizes benchmark results** comparing PIMST with LKH-3
- **Generates interactive charts** showing quality and time improvements
- **Creates professional reports** perfect for presentations
- **No coding required** - simple command-line interface

## Quick Start

### Step 1: Prepare Your Data

Create a JSON file with your benchmark results. See `benchmarks/data/example_atsp_results.json` for an example.

### Step 2: Generate Report

Run the report generator:

```bash
python generate_report.py
```

This will create an HTML report in the `reports/` directory.

### Step 3: View Results

Open the generated HTML file in any web browser. You'll see:

- 📊 **Interactive charts** showing improvements
- 📈 **Detailed statistics** about performance
- 📋 **Comparison tables** with all results
- 🎨 **Professional design** ready for presentations

## Using Your Own Data

### Option 1: Use the Command Line

```bash
python generate_report.py --input your_data.json --output my_report.html
```

### Option 2: Create a JSON File

1. Copy `benchmarks/data/example_atsp_results.json`
2. Edit it with your results
3. Save with a new name
4. Run the generator pointing to your file

## Understanding the Report

### Summary Statistics

The report shows key metrics:

- **Average Quality Improvement**: How much better PIMST solutions are (%)
- **Average Time Improvement**: How much faster PIMST is (%)
- **Better Results**: Number of instances where PIMST found better solutions
- **Equal Results**: Number of instances where results matched LKH-3

### Charts

1. **Quality Improvement Chart**: Bar chart showing quality improvement for each instance
2. **Time Improvement Chart**: Line chart showing speedup over time
3. **Size vs Improvement**: Scatter plot showing how improvements scale with problem size

### Detailed Table

Complete results for each benchmark instance including:
- Problem size
- Optimal solution (if known)
- LKH-3 results
- PIMST results
- Improvement percentages

## Tips for Presentations

### For Teaching

- Use the report to demonstrate algorithm performance
- Show the interactive charts during lectures
- Export specific charts as images if needed
- Print the detailed table for handouts

### For Research

- Include the HTML report in supplementary materials
- Use the visualizations in presentations
- Reference specific instances from the table
- Show trends across different problem sizes

### For Demonstrations

- Open the report in presentation mode (F11 in most browsers)
- Navigate through sections during demos
- Highlight specific improvements
- Compare with baseline (LKH-3) interactively

## Advanced Usage

### Customizing the Report

The report generator can be modified to:
- Change colors and styling
- Add more chart types
- Include additional metrics
- Customize the layout

See `src/report_generator.py` for implementation details.

### Batch Processing

Generate reports for multiple datasets:

```bash
for file in benchmarks/data/*.json; do
    python generate_report.py --input "$file" --output "$(basename $file .json).html"
done
```

### Adding New Metrics

To add new comparison metrics:

1. Add fields to your JSON data
2. Update the report generator template
3. Regenerate the report

## Troubleshooting

### Report doesn't display properly

- Make sure you're using a modern web browser (Chrome, Firefox, Safari, Edge)
- Check that JavaScript is enabled
- Try opening the file in a different browser

### Charts not showing

- Verify internet connection (charts use Chart.js from CDN)
- Check browser console for errors (F12)
- Ensure JSON data is properly formatted

### Data not updating

- Delete old reports and regenerate
- Clear browser cache
- Check that you're editing the correct JSON file

## Example Workflow

1. **Run experiments** with PIMST and LKH-3
2. **Collect results** (solution quality and runtime)
3. **Format data** into JSON structure
4. **Generate report** using the script
5. **Review results** in web browser
6. **Present or share** the HTML report

## Next Steps

- Check out `examples/` for more usage examples
- Read `docs/getting_started.md` for detailed setup
- See `benchmarks/README.md` for data format details
- Explore `src/report_generator.py` for customization options

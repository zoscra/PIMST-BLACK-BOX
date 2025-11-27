# PIMST Black Box

## Overview

PIMST Black Box is a benchmark visualization and reporting tool designed to showcase ATSP (Asymmetric Traveling Salesman Problem) algorithm performance. It generates professional, interactive HTML reports comparing PIMST results with LKH-3, perfect for presentations, teaching, and research demonstrations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **📊 Visual Reports**: Generate beautiful, interactive HTML reports from benchmark data
- **📈 Performance Comparison**: Compare PIMST results with LKH-3 algorithm
- **🎨 Professional Design**: Publication-ready visualizations for papers and presentations
- **🎓 Teaching-Friendly**: Perfect for educational demonstrations without showing code
- **⚡ Easy to Use**: Simple command-line interface, no coding required
- **📉 Interactive Charts**: Quality improvements, time comparisons, and scaling analysis

## Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed
- A modern web browser (Chrome, Firefox, Safari, or Edge)
- Basic command-line knowledge (optional)

## Installation

### Clone the Repository

```bash
git clone https://github.com/zoscra/PIMST-BLACK-BOX.git
cd PIMST-BLACK-BOX
```

### Install Dependencies

```bash
# Install required Python packages
pip install -r requirements.txt
```

No installation is needed for basic usage - the tool generates standalone HTML reports!

## Usage

### Quick Start - Generate Your First Report

```bash
# Generate a report using example data
python generate_report.py
```

This creates an interactive HTML report at `reports/benchmark_report.html`. Just open it in your browser!

### Using Your Own Data

```bash
# Generate report from your benchmark data
python generate_report.py --input benchmarks/data/your_results.json

# Specify custom output name
python generate_report.py --input your_data.json --output my_report.html
```

### What You Get

The generated report includes:

- 🏆 **Summary Statistics**: Average improvements, win/tie counts
- 📊 **Quality Chart**: Bar chart showing solution quality improvements
- ⚡ **Time Chart**: Line chart showing speedup over LKH-3
- 📈 **Scaling Analysis**: How improvements scale with problem size
- 📋 **Detailed Table**: Complete results for every benchmark instance

### Perfect for Presentations

No code is shown in the reports - just clean, professional visualizations perfect for:

- 🎓 **Teaching**: Demonstrate algorithm performance in lectures
- 📝 **Research**: Include in papers and presentations
- 💼 **Demonstrations**: Show results to stakeholders
- 📊 **Analysis**: Understand performance trends

## Project Structure

```
PIMST-BLACK-BOX/
├── README.md                    # This file
├── generate_report.py           # Main script to generate reports
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── benchmarks/
│   ├── data/                   # Benchmark result data (JSON)
│   └── results/                # Generated visualizations
├── src/
│   └── report_generator.py     # Report generation engine
├── docs/
│   ├── getting_started.md      # Getting started guide
│   └── user_guide.md           # Complete user guide
├── reports/                     # Generated HTML reports
├── tests/                       # Test files
└── examples/                    # Usage examples
```

## Data Format

Benchmark results are stored in JSON format. Example structure:

```json
{
  "benchmark_info": {
    "name": "ATSP Benchmark Comparison",
    "date": "2025-01-27",
    "problem_type": "ATSP",
    "instances_tested": 15
  },
  "results": [
    {
      "instance": "ftv33",
      "size": 33,
      "optimal": 1286,
      "lkh3_solution": 1286,
      "lkh3_time": 0.45,
      "pimst_solution": 1286,
      "pimst_time": 0.32,
      "improvement_quality": 0.0,
      "improvement_time": 28.9
    }
  ]
}
```

See `benchmarks/data/example_atsp_results.json` for a complete example with 15 instances.

## Example Results

Using the included example data, the generated report shows:

- ✅ **10 out of 15 instances** where PIMST found better solutions than LKH-3
- ✅ **0.43% average quality improvement** in solution quality
- ✅ **41.2% average speedup** in execution time
- ✅ **Up to 53% faster** on large instances (150+ nodes)

## Documentation

- **[User Guide](docs/user_guide.md)**: Complete usage instructions
- **[Getting Started](docs/getting_started.md)**: Quick start guide
- **[Benchmark Format](benchmarks/README.md)**: Data format specification

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

### Coding Standards

- Follow the existing code style
- Write clear, documented code
- Include tests for new features
- Update documentation as needed

## Use Cases

### For Educators

- Demonstrate algorithm performance without showing code
- Compare different algorithmic approaches
- Show how algorithms scale with problem size
- Create engaging presentations for students

### For Researchers

- Generate publication-ready figures
- Compare experimental results with baselines
- Analyze performance across multiple instances
- Document improvements over state-of-the-art

### For Presentations

- Professional, interactive visualizations
- No technical details unless needed
- Easy to navigate during talks
- Exportable charts and tables

## Roadmap

- [x] HTML report generation with interactive charts
- [x] ATSP benchmark comparison with LKH-3
- [x] Example data with 15 benchmark instances
- [x] User-friendly command-line interface
- [ ] PDF export functionality
- [ ] More chart types and visualizations
- [ ] Batch processing for multiple datasets
- [ ] Custom styling and themes

## Support

For questions, issues, or suggestions, please open an issue in the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Authors

- PIMST Team

## Acknowledgments

This project is part of the PIMST initiative for quality assurance and system validation.

---

**Note**: This README will be updated as the project develops. Please check back regularly for the latest information.

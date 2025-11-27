#!/usr/bin/env python3
"""
PIMST Black Box - Report Generator

Generates visual HTML reports comparing PIMST results with LKH-3 benchmarks.
This tool creates professional presentations without showing code.
"""

import json
import os
from datetime import datetime
from pathlib import Path


class BenchmarkReportGenerator:
    """Generates HTML reports from benchmark data."""

    def __init__(self, data_file, output_dir="reports"):
        """
        Initialize the report generator.

        Args:
            data_file: Path to JSON file with benchmark results
            output_dir: Directory to save generated reports
        """
        self.data_file = data_file
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.data = None

    def load_data(self):
        """Load benchmark data from JSON file."""
        with open(self.data_file, 'r') as f:
            self.data = json.load(f)

    def generate_html_report(self, output_file="benchmark_report.html"):
        """Generate complete HTML report."""
        if not self.data:
            self.load_data()

        html_content = self._generate_html()
        output_path = self.output_dir / output_file

        with open(output_path, 'w') as f:
            f.write(html_content)

        print(f"✓ Report generated: {output_path}")
        return output_path

    def _generate_html(self):
        """Generate HTML content for the report."""
        info = self.data['benchmark_info']
        results = self.data['results']
        summary = self.data['summary']

        # Prepare data for charts
        instances = [r['instance'] for r in results]
        quality_improvements = [r['improvement_quality'] for r in results]
        time_improvements = [r['improvement_time'] for r in results]
        sizes = [r['size'] for r in results]

        html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PIMST vs LKH-3 - Benchmark Results</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .info-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .info-card h3 {{
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        .info-card .value {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        .info-card .unit {{
            font-size: 0.8em;
            color: #666;
        }}
        .summary {{
            padding: 40px;
            background: white;
        }}
        .summary h2 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 2em;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }}
        .stat-card h3 {{
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 10px;
        }}
        .stat-card .stat-value {{
            font-size: 2.5em;
            font-weight: bold;
        }}
        .charts {{
            padding: 40px;
            background: #f8f9fa;
        }}
        .chart-container {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .chart-container h3 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 1.5em;
        }}
        .chart-wrapper {{
            position: relative;
            height: 400px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background: #667eea;
            color: white;
            font-weight: 600;
        }}
        tr:hover {{
            background: #f5f5f5;
        }}
        .better {{
            color: #22c55e;
            font-weight: bold;
        }}
        .equal {{
            color: #3b82f6;
            font-weight: bold;
        }}
        .footer {{
            background: #333;
            color: white;
            text-align: center;
            padding: 20px;
        }}
        .highlight {{
            background: linear-gradient(120deg, #ffd700 0%, #ffed4e 100%);
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏆 PIMST vs LKH-3</h1>
            <p>{info['problem_type']}</p>
            <p>Benchmark Comparison Report - {info['date']}</p>
        </div>

        <div class="info-grid">
            <div class="info-card">
                <h3>Instances Tested</h3>
                <div class="value">{info['instances_tested']}</div>
            </div>
            <div class="info-card">
                <h3>Problem Type</h3>
                <div class="value" style="font-size: 1.2em;">ATSP</div>
            </div>
            <div class="info-card">
                <h3>Test Date</h3>
                <div class="value" style="font-size: 1.2em;">{info['date']}</div>
            </div>
        </div>

        <div class="summary">
            <h2>📊 Summary Results</h2>
            <div class="stats-grid">
                <div class="stat-card highlight">
                    <h3>Average Quality Improvement</h3>
                    <div class="stat-value">{summary['avg_quality_improvement']:.2f}%</div>
                </div>
                <div class="stat-card highlight">
                    <h3>Average Time Improvement</h3>
                    <div class="stat-value">{summary['avg_time_improvement']:.1f}%</div>
                </div>
                <div class="stat-card">
                    <h3>Better Results</h3>
                    <div class="stat-value">{summary['pimst_better_quality']}/{summary['total_instances']}</div>
                </div>
                <div class="stat-card">
                    <h3>Equal Results</h3>
                    <div class="stat-value">{summary['pimst_equal_quality']}/{summary['total_instances']}</div>
                </div>
            </div>
        </div>

        <div class="charts">
            <div class="chart-container">
                <h3>📈 Quality Improvement by Instance</h3>
                <div class="chart-wrapper">
                    <canvas id="qualityChart"></canvas>
                </div>
            </div>

            <div class="chart-container">
                <h3>⚡ Time Improvement by Instance</h3>
                <div class="chart-wrapper">
                    <canvas id="timeChart"></canvas>
                </div>
            </div>

            <div class="chart-container">
                <h3>📊 Improvement vs Problem Size</h3>
                <div class="chart-wrapper">
                    <canvas id="scatterChart"></canvas>
                </div>
            </div>
        </div>

        <div class="summary">
            <h2>📋 Detailed Results</h2>
            <table>
                <thead>
                    <tr>
                        <th>Instance</th>
                        <th>Size</th>
                        <th>Optimal</th>
                        <th>LKH-3</th>
                        <th>PIMST</th>
                        <th>Quality Improvement</th>
                        <th>Time Improvement</th>
                    </tr>
                </thead>
                <tbody>
"""

        # Add table rows
        for r in results:
            quality_class = "better" if r['improvement_quality'] > 0 else "equal"
            html += f"""
                    <tr>
                        <td><strong>{r['instance']}</strong></td>
                        <td>{r['size']}</td>
                        <td>{r['optimal']}</td>
                        <td>{r['lkh3_solution']} ({r['lkh3_time']:.2f}s)</td>
                        <td>{r['pimst_solution']} ({r['pimst_time']:.2f}s)</td>
                        <td class="{quality_class}">{r['improvement_quality']:.2f}%</td>
                        <td class="better">{r['improvement_time']:.1f}%</td>
                    </tr>
"""

        html += f"""
                </tbody>
            </table>
        </div>

        <div class="footer">
            <p>Generated by PIMST Black Box Report Generator</p>
            <p>© 2025 PIMST Team</p>
        </div>
    </div>

    <script>
        // Quality Improvement Chart
        const qualityCtx = document.getElementById('qualityChart').getContext('2d');
        new Chart(qualityCtx, {{
            type: 'bar',
            data: {{
                labels: {json.dumps(instances)},
                datasets: [{{
                    label: 'Quality Improvement (%)',
                    data: {json.dumps(quality_improvements)},
                    backgroundColor: 'rgba(102, 126, 234, 0.6)',
                    borderColor: 'rgba(102, 126, 234, 1)',
                    borderWidth: 2
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{
                            display: true,
                            text: 'Improvement (%)'
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: true,
                        position: 'top'
                    }}
                }}
            }}
        }});

        // Time Improvement Chart
        const timeCtx = document.getElementById('timeChart').getContext('2d');
        new Chart(timeCtx, {{
            type: 'line',
            data: {{
                labels: {json.dumps(instances)},
                datasets: [{{
                    label: 'Time Improvement (%)',
                    data: {json.dumps(time_improvements)},
                    backgroundColor: 'rgba(34, 197, 94, 0.2)',
                    borderColor: 'rgba(34, 197, 94, 1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{
                            display: true,
                            text: 'Improvement (%)'
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: true,
                        position: 'top'
                    }}
                }}
            }}
        }});

        // Scatter Chart - Size vs Improvement
        const scatterCtx = document.getElementById('scatterChart').getContext('2d');
        const scatterData = {json.dumps([{'x': r['size'], 'y': r['improvement_quality']} for r in results])};

        new Chart(scatterCtx, {{
            type: 'scatter',
            data: {{
                datasets: [{{
                    label: 'Quality Improvement vs Problem Size',
                    data: scatterData,
                    backgroundColor: 'rgba(118, 75, 162, 0.6)',
                    borderColor: 'rgba(118, 75, 162, 1)',
                    pointRadius: 8,
                    pointHoverRadius: 12
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    x: {{
                        title: {{
                            display: true,
                            text: 'Problem Size (nodes)'
                        }}
                    }},
                    y: {{
                        beginAtZero: true,
                        title: {{
                            display: true,
                            text: 'Quality Improvement (%)'
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: true,
                        position: 'top'
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""
        return html


def main():
    """Main function to generate report."""
    # Example usage
    data_file = "benchmarks/data/example_atsp_results.json"
    generator = BenchmarkReportGenerator(data_file)
    output_file = generator.generate_html_report()
    print(f"\n✓ Report successfully generated!")
    print(f"  Open: {output_file}")


if __name__ == "__main__":
    main()

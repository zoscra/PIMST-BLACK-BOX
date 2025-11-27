# Benchmarks Directory

This directory contains benchmark data and results for ATSP (Asymmetric Traveling Salesman Problem) comparing PIMST with LKH-3.

## Structure

```
benchmarks/
├── data/           # Benchmark result data (JSON format)
└── results/        # Generated reports and visualizations
```

## Data Format

Benchmark results are stored in JSON format with the following structure:

```json
{
  "benchmark_info": {
    "name": "Benchmark name",
    "date": "YYYY-MM-DD",
    "problem_type": "ATSP",
    "instances_tested": 15
  },
  "results": [
    {
      "instance": "instance_name",
      "size": 100,
      "optimal": 1234,
      "lkh3_solution": 1250,
      "lkh3_time": 2.5,
      "pimst_solution": 1240,
      "pimst_time": 1.2,
      "improvement_quality": 0.8,
      "improvement_time": 52.0
    }
  ],
  "summary": {
    "total_instances": 15,
    "pimst_better_quality": 10,
    "avg_quality_improvement": 0.43,
    "avg_time_improvement": 41.2
  }
}
```

## Field Descriptions

- **instance**: Name of the benchmark instance (e.g., ftv33, ftv47)
- **size**: Number of nodes in the problem
- **optimal**: Known optimal solution value (if available)
- **lkh3_solution**: Solution quality obtained by LKH-3
- **lkh3_time**: Time taken by LKH-3 (in seconds)
- **pimst_solution**: Solution quality obtained by PIMST
- **pimst_time**: Time taken by PIMST (in seconds)
- **improvement_quality**: Quality improvement percentage over LKH-3
- **improvement_time**: Time improvement percentage over LKH-3

## Adding New Benchmarks

1. Create a new JSON file in `benchmarks/data/`
2. Follow the structure shown above
3. Run the report generator to create visualizations

## Example Instances Included

- **ftv33** to **ftv150**: Standard ATSP benchmark instances
- Various problem sizes from 33 to 150 nodes
- Known optimal solutions for validation

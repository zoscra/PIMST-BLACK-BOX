# Tests Directory

This directory contains all test files for the PIMST Black Box project.

## Structure

```
tests/
├── unit/           # Unit tests for individual components
├── integration/    # Integration tests
├── fixtures/       # Test fixtures and sample data
└── conftest.py     # Pytest configuration (if using pytest)
```

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_analyzer.py

# Run with coverage
pytest --cov=src tests/
```

## Guidelines

- Mirror the structure of the `src/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Include both positive and negative test cases
- Aim for high code coverage (>80%)

## Writing Tests

```python
# Example test structure
def test_function_name():
    # Arrange
    input_data = prepare_test_data()

    # Act
    result = function_to_test(input_data)

    # Assert
    assert result == expected_output
```

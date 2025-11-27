# Source Code Directory

This directory contains the main source code for the PIMST Black Box project.

## Structure

```
src/
├── core/           # Core functionality and main modules
├── utils/          # Utility functions and helpers
├── analyzers/      # Black-box analysis tools
├── reporters/      # Result reporting modules
└── config/         # Configuration management
```

## Guidelines

- Keep code modular and well-documented
- Follow the project's coding standards
- Each module should have a clear, single responsibility
- Include docstrings for all public functions and classes

## Getting Started

When adding new source files:
1. Place them in the appropriate subdirectory
2. Update relevant imports in `__init__.py` files
3. Add corresponding tests in the `tests/` directory
4. Document public APIs

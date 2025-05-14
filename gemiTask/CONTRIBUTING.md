# Contributing to gemiTask

Thank you for your interest in contributing to gemiTask! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## How Can I Contribute?

### Reporting Bugs

- Check if the bug has already been reported
- Use the bug report template
- Include detailed steps to reproduce
- Include expected and actual behavior
- Include screenshots if applicable

### Suggesting Features

- Check if the feature has already been suggested
- Use the feature request template
- Include a clear description
- Explain why this feature would be useful
- Include any relevant examples

### Pull Requests

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Add tests for new features
5. Update documentation
6. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sanjaymalladi/gemiTask.git
   cd gemiTask
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Code Style

- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions small and focused
- Write meaningful commit messages

## Testing

- Write tests for new features
- Run existing tests:
  ```bash
  pytest
  ```
- Maintain test coverage:
  ```bash
  pytest --cov=./ --cov-report=term-missing
  ```

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Update command-line help text
- Keep the documentation up to date

## Release Process

1. Update version in `setup.py`
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. The GitHub Action will handle PyPI upload

## Questions?

Feel free to open an issue for any questions or concerns. 
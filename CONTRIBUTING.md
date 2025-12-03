# Contributing to ClimaRisk AI

Thank you for your interest in contributing to ClimaRisk AI! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

### Suggesting Features

1. Check existing feature requests
2. Create an issue describing:
   - The problem you're solving
   - Proposed solution
   - Use cases

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Ensure all tests pass
6. Commit with clear messages
7. Push to your fork
8. Create a Pull Request

## Development Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ClimaRiskAI.git
cd ClimaRiskAI
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If exists
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Set up database**
```bash
docker-compose up -d postgres
alembic upgrade head
```

6. **Run tests**
```bash
pytest
```

## Coding Standards

### Python

- Follow PEP 8 style guide
- Use type hints
- Write docstrings for functions/classes
- Maximum line length: 100 characters
- Use `black` for formatting
- Use `flake8` for linting

```bash
# Format code
black .

# Lint code
flake8 .
```

### Type Hints

```python
def calculate_score(
    latitude: float,
    longitude: float,
    property_type: str = "residential"
) -> Dict[str, float]:
    """Calculate risk score."""
    ...
```

### Docstrings

Use Google-style docstrings:

```python
def predict_flood_risk(latitude: float, longitude: float) -> float:
    """Predict flood risk for a location.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        
    Returns:
        Flood risk score (0-100)
    """
    ...
```

## Commit Messages

Follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Other changes (dependencies, config)

Example:
```
feat: add groundwater risk model

- Implement basic groundwater risk prediction
- Add CGWB data ingestion
- Create feature engineering pipeline
```

## Testing

- Write tests for new features
- Aim for >80% code coverage
- Include unit tests and integration tests
- Test edge cases and error handling

```python
def test_flood_risk_calculation():
    """Test flood risk calculation."""
    model = FloodRiskModel()
    score = model.predict(latitude=28.6139, longitude=77.2090)
    assert 0 <= score <= 100
```

## Documentation

- Update README if needed
- Add docstrings to new functions/classes
- Update API documentation
- Add examples for new features

## Areas for Contribution

- **ML Models**: Improve accuracy, add new risk types
- **Data Sources**: Integrate new data sources
- **Frontend**: UI/UX improvements
- **Documentation**: Improve docs, add tutorials
- **Testing**: Increase test coverage
- **Performance**: Optimize queries, caching
- **Features**: New endpoints, visualizations

## Questions?

- Open an issue for questions
- Check existing documentation
- Review existing code for examples

Thank you for contributing! 🎉


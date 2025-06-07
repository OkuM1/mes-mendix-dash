# Contributing to Smart MES Dashboard

Thank you for your interest in contributing to the Smart MES Dashboard project!

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/smart-mes-dashboard.git
   cd smart-mes-dashboard
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
smart-mes-dashboard/
├── src/                    # Source code
│   ├── api/               # FastAPI backend
│   └── etl/               # ETL pipelines
├── data/                  # Sample and processed data
├── docs/                  # Documentation and assets
├── tests/                 # Test files
└── requirements.txt       # Dependencies
```

## Running the Application

### Start the API Server
```bash
cd src/api
python mes_api.py
```

### Run ETL Pipeline
```bash
cd src/etl
python mes_etl.py
```

## Code Style

- Follow PEP 8 for Python code
- Use type hints where appropriate
- Add docstrings to all functions and classes
- Keep functions focused and modular

## Testing

Run tests using:
```bash
python -m pytest tests/
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Questions?

Open an issue for any questions or suggestions!

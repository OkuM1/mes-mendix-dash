# Changelog

All notable changes to the Smart MES Dashboard project will be documented in this file.

## [1.0.0] - 2025-06-07

### Added
- Initial release of Smart MES Dashboard
- FastAPI backend with RESTful endpoints
- ETL pipeline using Pandas for data processing
- Sample railway manufacturing data
- Professional API documentation
- System architecture visualization
- Mendix integration capabilities

### Features
- Work order management endpoints
- Real-time KPI calculations
- Production efficiency metrics
- Professional API documentation with Swagger
- Clean, modular codebase structure

### API Endpoints
- `GET /` - Health check
- `GET /api/v1/workorders` - Retrieve all work orders
- `GET /api/v1/workorders/{id}` - Get specific work order
- `GET /api/v1/kpis` - Production KPIs and metrics

### Technical Stack
- FastAPI 0.104.1
- Pandas 2.1.3
- Pydantic 2.5.0
- Uvicorn 0.24.0

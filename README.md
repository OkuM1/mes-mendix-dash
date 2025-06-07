# 🏭 Smart MES Dashboard

**A Professional Manufacturing Execution System built with FastAPI + ETL + Mendix Integration**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Professional showcase demonstrating full-stack data engineering capabilities for modern manufacturing environments, specifically designed with Siemens Mobility requirements in mind.**

## 🎯 **Overview**

This project demonstrates enterprise-grade capabilities in:
- **🚀 FastAPI Backend Development** - Professional RESTful APIs
- **📊 ETL Data Processing** - Pandas-powered data pipelines  
- **🔗 Low-Code Integration** - Mendix dashboard connectivity
- **🏭 Manufacturing Domain** - Real-world MES expertise

## 🏗️ **Architecture**

```
smart-mes-dashboard/
├── 📁 src/                         # Source Code
│   ├── api/                        # FastAPI Backend
│   │   ├── mes_api.py             # Main API Server
│   │   └── mock_mes_api.py        # Development Mock
│   └── etl/                       # ETL Pipeline
│       ├── mes_etl.py             # Data Processing
│       └── utils.py               # Utilities
├── 📁 data/                       # Manufacturing Data
│   ├── sample_orders.json         # Railway Work Orders
│   └── processed_*.csv            # ETL Outputs
├── 📁 docs/                       # Documentation
│   ├── architecture.html          # System Visualization
│   └── dashboard_design/          # UI/UX Specs
├── 📁 tests/                      # Test Suite
└── 📄 requirements.txt            # Dependencies
```

## 🚀 **Quick Start**

### **1. Environment Setup**
```bash
# Clone the repository
git clone https://github.com/yourusername/smart-mes-dashboard.git
cd smart-mes-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### **2. Start the MES API**
```bash
cd src/api
python mes_api.py
# 🌐 API Server: http://localhost:8000
# 📋 API Docs: http://localhost:8000/docs
```

### **3. Run ETL Pipeline**
```bash
cd src/etl
python mes_etl.py
# 📊 Processes data and exports CSV for dashboards
```

### **4. View System Architecture**
```bash
# Open architecture visualization
open docs/architecture.html
```

---

## 🔗 **API Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check and service status |
| `GET` | `/api/v1/workorders` | Retrieve all manufacturing work orders |
| `GET` | `/api/v1/workorders/{id}` | Get specific work order details |
| `GET` | `/api/v1/kpis` | Production KPIs and metrics |

### **Sample API Response**
```json
{
  "order_id": "WO-2025-001",
  "product_name": "Railway Signal Controller",
  "quantity_planned": 50,
  "quantity_produced": 33,
  "status": "IN_PROGRESS",
  "efficiency": 78.18,
  "start_time": "2025-06-07T08:00:00",
  "priority": "HIGH"
}
```

### **Live API Documentation**
Visit `http://localhost:8000/docs` for interactive Swagger documentation when the API is running.

---

## 📊 **Sample Output**
```
============================================================
MES DATA PROCESSING SUMMARY
============================================================
📊 Total Work Orders: 6
✅ Completed: 2
🔄 In Progress: 2  
⏳ Pending: 1
📈 Completion Rate: 33.33%
⚡ Production Efficiency: 78.18%
============================================================
```

---

## 🛠️ **Technology Stack**
- **FastAPI** - Modern Python web framework
- **Pandas** - Data analysis and ETL processing
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server for production deployment

---

## 🎨 **Mendix Integration**

This system is designed for seamless integration with Mendix low-code platform:

1. **Start the API** (`python src/api/mes_api.py`)
2. **In Mendix Studio Pro:**
   - Add REST service: `http://localhost:8000/api/v1/workorders`
   - Import JSON structure for work orders
   - Create data views and charts
   - Build production dashboard

3. **ETL Exports:**
   - CSV files in `/data/processed_orders_*.csv`
   - JSON KPIs in `/data/kpis_*.json`

---

## 💼 **Business Context**

This project simulates a real **Siemens Mobility** manufacturing scenario:
- Railway component production tracking
- Quality control and efficiency monitoring  
- Integration between operational systems and management dashboards
- Data-driven decision making for production optimization

Perfect demonstration of skills for **Data Engineering + Low-Code Development** roles.

---

## 📈 **Features**

- ✅ **RESTful API** with FastAPI
- ✅ **ETL Pipeline** with Pandas
- ✅ **Real-time KPIs** calculation
- ✅ **Professional Documentation** with Swagger
- ✅ **Mendix Integration** ready
- ✅ **Sample Manufacturing Data** 
- ✅ **Modular Architecture**
- ✅ **Production Ready** code

---

## 🚀 **Getting Started for Development**

1. **Fork this repository**
2. **Clone your fork**
3. **Follow the Quick Start guide above**
4. **Check out the [Contributing Guide](CONTRIBUTING.md)**
5. **Review the [Changelog](CHANGELOG.md)**

---

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 **Contributing**

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

---

**Built with ❤️ for modern manufacturing and data engineering**

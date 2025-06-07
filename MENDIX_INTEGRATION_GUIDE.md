# Mendix Pro Integration Guide
## Smart MES Dashboard - Siemens Mobility Demo

### 🎯 **Overview**
This guide provides step-by-step instructions for integrating the Smart MES FastAPI backend with Mendix Pro to create a professional manufacturing dashboard.

---

### 🔧 **Prerequisites**
- Mendix Studio Pro installed
- FastAPI backend running (`python api/mes_api.py`)
- Sample data available via: `http://localhost:8000/api/v1/workorders`

---

### 📋 **Step 1: Create New Mendix App**

1. **Open Mendix Studio Pro**
2. **Create New App**:
   - App Name: `Siemens MES Dashboard`
   - Template: `Blank Web App`
   - Development Line: `Main line`

3. **Configure App Settings**:
   - Theme: `Atlas UI`
   - Navigation: `Responsive`

---

### 🔗 **Step 2: Configure REST Service Integration**

#### **A. Add REST Service**
1. **Right-click App Explorer** → `Add` → `Integration` → `Published REST service`
2. **Create Consumed REST Service**:
   - Service Name: `MES_API_Service`
   - Base URL: `http://localhost:8000`

#### **B. Import OpenAPI Specification**
1. **In REST Service** → `Import from OpenAPI`
2. **URL**: `http://localhost:8000/docs` (FastAPI auto-docs)
3. **Select Endpoints**:
   - `GET /api/v1/workorders`
   - `GET /api/v1/kpis`
   - `GET /`

#### **C. Create Domain Model**
```
Entities to Create:
┌─────────────────┐
│   WorkOrder     │
├─────────────────┤
│ OrderId: String │
│ ProductName: Str│
│ QtyPlanned: Int │
│ QtyProduced: Int│
│ Status: Enum    │
│ StartTime: Date │
│ EndTime: Date   │
│ Priority: Enum  │
└─────────────────┘

┌─────────────────┐
│      KPI        │
├─────────────────┤
│ TotalOrders: Int│
│ Completed: Int  │
│ InProgress: Int │
│ Pending: Int    │
│ CompletionRate: │
│   Decimal       │
│ Efficiency:     │
│   Decimal       │
└─────────────────┘
```

---

### 🎨 **Step 3: Create Dashboard Pages**

#### **A. Main Dashboard Page**
1. **Create Page**: `Dashboard_Main`
2. **Layout**: `Atlas_Default`
3. **Add Widgets**:
   - **Header**: Company Logo + "Siemens MES Dashboard"
   - **KPI Cards**: 4 cards showing key metrics
   - **Charts**: Production status pie chart
   - **Data Grid**: Active work orders table

#### **B. Widget Configuration**

**KPI Cards Layout:**
```
┌─────────────────────────────────────────────┐
│  📊 Total Orders  │  ✅ Completed  │  🔄 Active  │  📈 Efficiency  │
│      {count}      │    {count}     │   {count}   │     {percent}   │
└─────────────────────────────────────────────┘
```

**Work Orders Grid:**
- Columns: Order ID, Product, Status, Progress, Priority
- Conditional Formatting: Status-based row colors
- Action Buttons: View Details, Update Status

---

### 📊 **Step 4: Data Integration & Microflows**

#### **A. Data Retrieval Microflow**
1. **Create Microflow**: `MF_RefreshMESData`
2. **Activities**:
   - **Call REST**: GET /api/v1/workorders
   - **Import Mapping**: JSON to WorkOrder entities
   - **Call REST**: GET /api/v1/kpis  
   - **Import Mapping**: JSON to KPI entity
   - **Refresh UI**: Update dashboard widgets

#### **B. Scheduled Data Refresh**
1. **Create Scheduled Event**: `SE_DataRefresh`
2. **Interval**: Every 5 minutes
3. **Microflow**: `MF_RefreshMESData`

---

### 🎯 **Step 5: Dashboard Styling & UX**

#### **A. Siemens Brand Colors**
```css
/* Add to theme/web/sass/custom/_custom.scss */
$siemens-teal: #009999;
$siemens-blue: #0f4c81;
$siemens-green: #76b900;
$siemens-gray: #9b9b9b;

.mes-kpi-card {
    background: linear-gradient(135deg, $siemens-teal, $siemens-blue);
    color: white;
    border-radius: 8px;
    padding: 20px;
    margin: 10px;
}

.status-completed { background-color: $siemens-green !important; }
.status-inprogress { background-color: $siemens-teal !important; }
.status-pending { background-color: $siemens-gray !important; }
```

#### **B. Responsive Design**
- **Desktop**: 4-column KPI layout
- **Tablet**: 2-column KPI layout  
- **Mobile**: 1-column KPI layout

---

### 📈 **Step 6: Advanced Features**

#### **A. Real-time Updates**
1. **WebSocket Integration** (if needed)
2. **Auto-refresh**: Timer widget for live data
3. **Push Notifications**: Alert on critical issues

#### **B. Drill-down Functionality**
1. **Work Order Details Page**
2. **Production Analytics Page**
3. **Quality Metrics Dashboard**

#### **C. Export & Reporting**
1. **Excel Export**: Work orders data
2. **PDF Reports**: Production summary
3. **Email Notifications**: Daily/weekly reports

---

### 🚀 **Step 7: Testing & Deployment**

#### **A. Local Testing**
1. **Start FastAPI**: `python api/mes_api.py`
2. **Run Mendix App**: F5 in Studio Pro
3. **Test Endpoints**: Verify data flow
4. **UI Testing**: Check responsive design

#### **B. Demo Preparation**
1. **Sample Data**: Ensure API returns consistent data
2. **Performance**: Optimize widget loading
3. **Screenshots**: Capture key dashboard views
4. **Video Demo**: Record 2-3 minute walkthrough

---

### 📝 **Step 8: Documentation for Job Application**

#### **A. Technical Documentation**
- **Architecture Diagram**: API ↔ Mendix integration
- **Data Model**: Entity relationships
- **API Endpoints**: Usage and responses
- **Security**: Authentication implementation

#### **B. Business Value**
- **ROI**: Operational efficiency improvements
- **Scalability**: Multi-site deployment capability
- **Integration**: SAP/ERP connectivity potential
- **User Experience**: Intuitive operator interface

---

### 🎯 **Key Demo Points for Siemens Interview**

1. **Real Manufacturing Data**: Siemens railway components
2. **Professional API Design**: FastAPI with proper documentation
3. **ETL Pipeline**: Pandas data processing expertise
4. **Low-Code Integration**: Mendix Pro dashboard
5. **Scalable Architecture**: Production-ready design
6. **Industry Knowledge**: Understanding of MES requirements

---

### 📞 **Next Steps**

1. **Implement Mendix Integration** (follow this guide)
2. **Create Demo Video** (2-3 minutes)
3. **Prepare Interview Presentation**
4. **Document Business Case**
5. **Practice Technical Q&A**

---

**Ready to showcase full-stack data engineering + low-code development skills for Siemens Mobility! 🚂**

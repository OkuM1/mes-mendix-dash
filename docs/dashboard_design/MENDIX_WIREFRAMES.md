# Smart MES Dashboard - Mendix Wireframes
## Dashboard Layout Design for Siemens Mobility

### 🎨 **Main Dashboard Layout**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🏭 SIEMENS MES DASHBOARD                                    [User] [Settings] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │📊 TOTAL     │  │✅ COMPLETED │  │🔄 ACTIVE    │  │📈 EFFICIENCY│        │
│  │   ORDERS    │  │   ORDERS    │  │   ORDERS    │  │             │        │
│  │     6       │  │     2       │  │     3       │  │   78.18%    │        │
│  │             │  │             │  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                                             │
│  ┌─────────────────────────────────┐  ┌───────────────────────────────────┐ │
│  │ 📊 PRODUCTION STATUS            │  │ 🔧 RECENT ACTIVITIES              │ │
│  │                                 │  │                                   │ │
│  │     [PIE CHART]                 │  │ • WO-2025-002: In Progress        │ │
│  │   ✅ Completed: 2               │  │ • WO-2025-006: Started           │ │
│  │   🔄 In Progress: 3             │  │ • WO-2025-001: Completed         │ │
│  │   ⏳ Pending: 1                 │  │ • WO-2025-004: Quality Check     │ │
│  │                                 │  │                                   │ │
│  └─────────────────────────────────┘  └───────────────────────────────────┘ │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────────┐ │
│  │ 📋 ACTIVE WORK ORDERS                                                   │ │
│  │                                                                         │ │
│  │ Order ID    │ Product Name      │ Status      │ Progress │ Priority     │ │
│  │─────────────┼───────────────────┼─────────────┼──────────┼──────────────│ │
│  │ WO-2025-002 │ Brake Control Unit│ In Progress │ 72%      │ 🔴 Urgent    │ │
│  │ WO-2025-006 │ Safety Controller │ In Progress │ 60%      │ 🟡 High      │ │
│  │ WO-2025-003 │ Sensor Module     │ Pending     │ 0%       │ 🟢 Medium    │ │
│  │ WO-2025-005 │ Power Supply Unit │ On Hold     │ 27%      │ 🔵 Low       │ │
│  │                                                                         │ │
│  │ [View Details] [Update Status] [Export]                                 │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 📱 **Mobile Layout (Responsive)**

```
┌─────────────────────────┐
│ 🏭 SIEMENS MES          │
│                    [☰]  │
├─────────────────────────┤
│ ┌─────────┐ ┌─────────┐ │
│ │📊 TOTAL │ │✅ DONE  │ │
│ │   6     │ │   2     │ │
│ └─────────┘ └─────────┘ │
│ ┌─────────┐ ┌─────────┐ │
│ │🔄 ACTIVE│ │📈 EFF   │ │
│ │   3     │ │ 78.18%  │ │
│ └─────────┘ └─────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ WO-2025-002         │ │
│ │ Brake Control Unit  │ │
│ │ 🔄 In Progress      │ │
│ │ Progress: 72%       │ │
│ │ Priority: 🔴 Urgent │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ WO-2025-006         │ │
│ │ Safety Controller   │ │
│ │ 🔄 In Progress      │ │
│ │ Progress: 60%       │ │
│ │ Priority: 🟡 High   │ │
│ └─────────────────────┘ │
│                         │
│ [View All Orders]       │
└─────────────────────────┘
```

### 🎨 **Mendix Widget Structure**

#### **Page Layout: Dashboard_Main**
```
Container (Full Width)
├── Header Container
│   ├── Image (Siemens Logo)
│   ├── Text (MES Dashboard)
│   └── Account Menu
├── KPI Container (4 Columns)
│   ├── KPI Card 1 (Total Orders)
│   ├── KPI Card 2 (Completed)
│   ├── KPI Card 3 (Active)
│   └── KPI Card 4 (Efficiency)
├── Charts Container (2 Columns)
│   ├── Pie Chart (Production Status)
│   └── List View (Recent Activities)
└── Data Grid Container
    └── Work Orders Grid
```

#### **Custom Widget: KPI_Card**
```
Container (Card Style)
├── Icon Container
│   └── Icon (Dynamic based on KPI type)
├── Value Container
│   ├── Text (Main Value)
│   └── Text (Label)
└── Trend Container (Optional)
    └── Text (Trend indicator)
```

### 🎨 **Color Scheme & Styling**

#### **Siemens Brand Colors**
- **Primary**: `#009999` (Siemens Teal)
- **Secondary**: `#0f4c81` (Siemens Blue)  
- **Success**: `#76b900` (Siemens Green)
- **Warning**: `#ff8c00` (Orange)
- **Danger**: `#e74c3c` (Red)
- **Gray**: `#9b9b9b` (Neutral)

#### **Status Colors**
- **Completed**: `#76b900` (Green)
- **In Progress**: `#009999` (Teal)
- **Pending**: `#9b9b9b` (Gray)
- **On Hold**: `#ff8c00` (Orange)
- **Error**: `#e74c3c` (Red)

#### **Priority Colors**
- **Urgent**: `#e74c3c` (Red) 🔴
- **High**: `#ff8c00` (Orange) 🟡  
- **Medium**: `#76b900` (Green) 🟢
- **Low**: `#0f4c81` (Blue) 🔵

### 📊 **Data Widgets Configuration**

#### **KPI Cards Data Sources**
```javascript
// Total Orders
Data Source: Microflow → MF_GetKPIData
XPath: [KPI]/TotalOrders

// Completed Orders  
Data Source: Same microflow
XPath: [KPI]/CompletedOrders

// Efficiency
Data Source: Same microflow
XPath: [KPI]/Efficiency
Format: Percentage (2 decimals)
```

#### **Work Orders Grid Configuration**
```javascript
Data Source: Database → WorkOrder entity
Sorting: Priority (desc), Status, OrderId
Columns:
- OrderId (Text)
- ProductName (Text) 
- Status (Enumeration with colors)
- Progress (Progress bar widget)
- Priority (Enumeration with icons)

Actions:
- View: Open WorkOrder_Details page
- Edit: Open WorkOrder_Edit page  
- Export: Export to Excel
```

#### **Charts Configuration**
```javascript
// Pie Chart - Production Status
Chart Type: Pie
Data Source: Microflow → MF_GetStatusDistribution
Labels: Status values
Values: Count per status
Colors: Status color scheme

// Recent Activities List
Data Source: Database → WorkOrder entity
Sorting: LastModified (desc)
Limit: 5 items
Template: Custom with status icons
```

### 🚀 **Advanced Features Layout**

#### **Work Order Details Page**
```
┌─────────────────────────────────────────────────────────────┐
│ ← Back to Dashboard                    WO-2025-002          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ ┌─────────────────┐  ┌─────────────────────────────────────┐ │
│ │ ORDER INFO      │  │ PRODUCTION PROGRESS                 │ │
│ │                 │  │                                     │ │
│ │ Product:        │  │ ██████████░░ 72%                    │ │
│ │ Brake Control   │  │                                     │ │
│ │ Unit            │  │ Planned: 25 units                   │ │
│ │                 │  │ Produced: 18 units                  │ │
│ │ Priority: 🔴    │  │ Remaining: 7 units                  │ │
│ │ Status: In Prog │  │                                     │ │
│ │                 │  │ Est. Completion: 2 hours            │ │
│ └─────────────────┘  └─────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ TIMELINE & ACTIVITIES                                   │ │
│ │                                                         │ │
│ │ ✅ 09:00 - Order Created                                │ │
│ │ ✅ 09:15 - Materials Allocated                          │ │
│ │ ✅ 10:00 - Production Started                           │ │
│ │ 🔄 12:30 - Quality Check (In Progress)                  │ │
│ │ ⏳ --:-- - Final Assembly (Pending)                     │ │
│ │ ⏳ --:-- - Quality Approval (Pending)                   │ │
│ │                                                         │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ [Update Status] [Add Note] [Print Label]                   │
└─────────────────────────────────────────────────────────────┘
```

### 📱 **Implementation Notes for Mendix**

#### **Responsive Breakpoints**
- **Desktop**: > 1024px (4-column KPI layout)
- **Tablet**: 768px - 1024px (2-column KPI layout)
- **Mobile**: < 768px (1-column KPI layout)

#### **Widget Recommendations**
- **KPI Cards**: Custom widget or Layout Grid with styling
- **Charts**: Charts widget from App Store
- **Progress Bars**: Progress Bar widget
- **Data Grid**: Standard Data Grid 2
- **Icons**: Bootstrap Icons or FontAwesome

#### **Performance Optimization**
- **Data Refresh**: Timer widget every 30 seconds
- **Pagination**: Data Grid with 10 items per page
- **Caching**: Microflow caching for KPI calculations
- **Lazy Loading**: Load charts after main data

---

**This wireframe provides a complete blueprint for implementing the Mendix dashboard with professional UX design aligned with Siemens branding! 🎨🏭**

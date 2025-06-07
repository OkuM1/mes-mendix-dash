"""
MES API v1 - Manufacturing Execution System
Siemens Mobility Demo Project

A clean, professional API that serves real manufacturing data
for ETL processing and Mendix dashboard integration.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json
import os

app = FastAPI(
    title="MES API v1",
    description="Manufacturing Execution System API for Siemens Mobility Demo",
    version="1.0.0"
)

# Allow cross-origin requests for dashboard integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Data Models
class WorkOrder(BaseModel):
    """Work Order model matching Siemens manufacturing standards"""
    order_id: str
    product_name: str
    quantity_planned: int
    quantity_produced: int
    status: str  # "pending", "in_progress", "completed", "on_hold"
    start_time: Optional[str]
    end_time: Optional[str]
    priority: str

class KPI(BaseModel):
    """Key Performance Indicators"""
    total_orders: int
    completed_orders: int
    in_progress_orders: int
    pending_orders: int
    completion_rate: float
    efficiency: float

# Data Loader
def load_work_orders() -> List[dict]:
    """Load work order data from the JSON file"""
    data_file = os.path.join(os.path.dirname(__file__), "../data/sample_orders.json")
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# API Endpoints
@app.get("/")
async def health_check():
    """Simple health check to verify the API is running"""
    return {
        "service": "MES API v1",
        "status": "operational",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/v1/workorders", response_model=List[WorkOrder])
async def get_work_orders(status: Optional[str] = None):
    """
    Get all work orders, with optional status filtering
    This is the main endpoint that Mendix will use
    """
    orders = load_work_orders()
    
    if status:
        orders = [order for order in orders if order.get("status") == status]
    
    return orders

@app.get("/api/v1/workorders/{order_id}", response_model=WorkOrder)
async def get_work_order(order_id: str):
    """Get a specific work order by its ID"""
    orders = load_work_orders()
    
    for order in orders:
        if order.get("order_id") == order_id:
            return order
    
    raise HTTPException(status_code=404, detail=f"Work order {order_id} not found")

@app.get("/api/v1/kpis", response_model=KPI)
async def get_kpis():
    """
    Calculate and return Key Performance Indicators
    Used by ETL for analytics and dashboard metrics
    """
    orders = load_work_orders()
    
    total = len(orders)
    completed = len([o for o in orders if o.get("status") == "completed"])
    in_progress = len([o for o in orders if o.get("status") == "in_progress"])
    pending = len([o for o in orders if o.get("status") == "pending"])
    
    completion_rate = (completed / total * 100) if total > 0 else 0
    
    # Calculate efficiency based on planned vs produced quantities
    total_planned = sum(o.get("quantity_planned", 0) for o in orders)
    total_produced = sum(o.get("quantity_produced", 0) for o in orders)
    efficiency = (total_produced / total_planned * 100) if total_planned > 0 else 0
    
    return KPI(
        total_orders=total,
        completed_orders=completed,
        in_progress_orders=in_progress,
        pending_orders=pending,
        completion_rate=round(completion_rate, 2),
        efficiency=round(efficiency, 2)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

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

# Enable CORS for Mendix integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Pydantic models
class ProductionOrder(BaseModel):
    order_id: str
    product_name: str
    quantity_planned: int
    quantity_produced: int
    status: str  # "pending", "in_progress", "completed", "on_hold"
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    priority: str  # "low", "medium", "high", "urgent"

class Machine(BaseModel):
    machine_id: str
    name: str
    status: str  # "running", "idle", "maintenance", "error"
    current_order: Optional[str]
    efficiency: float  # percentage
    temperature: Optional[float]
    pressure: Optional[float]
    last_maintenance: datetime

class QualityMetric(BaseModel):
    metric_id: str
    order_id: str
    test_type: str
    result: str  # "pass", "fail"
    measurement: float
    specification_min: float
    specification_max: float
    timestamp: datetime

class ProductionStats(BaseModel):
    total_orders: int
    completed_orders: int
    active_orders: int
    overall_efficiency: float
    defect_rate: float
    on_time_delivery: float

# Mock data generators
def generate_mock_orders(count: int = 10) -> List[ProductionOrder]:
    statuses = ["pending", "in_progress", "completed", "on_hold"]
    priorities = ["low", "medium", "high", "urgent"]
    products = ["Widget A", "Component B", "Assembly C", "Part D", "Module E"]
    
    orders = []
    for i in range(count):
        start_time = datetime.now() - timedelta(days=random.randint(0, 7))
        status = random.choice(statuses)
        
        order = ProductionOrder(
            order_id=f"ORD-{1000 + i}",
            product_name=random.choice(products),
            quantity_planned=random.randint(50, 500),
            quantity_produced=random.randint(0, 500),
            status=status,
            start_time=start_time if status != "pending" else None,
            end_time=start_time + timedelta(hours=random.randint(2, 48)) if status == "completed" else None,
            priority=random.choice(priorities)
        )
        orders.append(order)
    
    return orders

def generate_mock_machines(count: int = 5) -> List[Machine]:
    statuses = ["running", "idle", "maintenance", "error"]
    machines = []
    
    for i in range(count):
        machine = Machine(
            machine_id=f"MCH-{100 + i}",
            name=f"Production Line {i + 1}",
            status=random.choice(statuses),
            current_order=f"ORD-{random.randint(1000, 1010)}" if random.choice([True, False]) else None,
            efficiency=round(random.uniform(75.0, 98.0), 2),
            temperature=round(random.uniform(18.0, 25.0), 1) if random.choice([True, False]) else None,
            pressure=round(random.uniform(1.0, 3.0), 2) if random.choice([True, False]) else None,
            last_maintenance=datetime.now() - timedelta(days=random.randint(1, 30))
        )
        machines.append(machine)
    
    return machines

def generate_mock_quality_metrics(count: int = 20) -> List[QualityMetric]:
    test_types = ["Dimensional", "Pressure Test", "Visual Inspection", "Electrical Test", "Weight Check"]
    results = ["pass", "fail"]
    
    metrics = []
    for i in range(count):
        spec_min = random.uniform(10.0, 50.0)
        spec_max = spec_min + random.uniform(5.0, 20.0)
        measurement = random.uniform(spec_min - 2.0, spec_max + 2.0)
        
        metric = QualityMetric(
            metric_id=f"QM-{2000 + i}",
            order_id=f"ORD-{random.randint(1000, 1010)}",
            test_type=random.choice(test_types),
            result="pass" if spec_min <= measurement <= spec_max else "fail",
            measurement=round(measurement, 2),
            specification_min=round(spec_min, 2),
            specification_max=round(spec_max, 2),
            timestamp=datetime.now() - timedelta(hours=random.randint(0, 48))
        )
        metrics.append(metric)
    
    return metrics

# API endpoints
@app.get("/")
async def root():
    return {"message": "Smart MES Dashboard API", "status": "running"}

@app.get("/orders", response_model=List[ProductionOrder])
async def get_orders(status: Optional[str] = None, limit: int = 10):
    """Get production orders, optionally filtered by status"""
    orders = generate_mock_orders(limit)
    
    if status:
        orders = [order for order in orders if order.status == status]
    
    return orders

@app.get("/orders/{order_id}", response_model=ProductionOrder)
async def get_order(order_id: str):
    """Get a specific production order"""
    # In a real implementation, this would query a database
    orders = generate_mock_orders(1)
    if orders:
        orders[0].order_id = order_id
        return orders[0]
    
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/machines", response_model=List[Machine])
async def get_machines(status: Optional[str] = None):
    """Get machine status information"""
    machines = generate_mock_machines()
    
    if status:
        machines = [machine for machine in machines if machine.status == status]
    
    return machines

@app.get("/machines/{machine_id}", response_model=Machine)
async def get_machine(machine_id: str):
    """Get a specific machine's status"""
    machines = generate_mock_machines(1)
    if machines:
        machines[0].machine_id = machine_id
        return machines[0]
    
    raise HTTPException(status_code=404, detail="Machine not found")

@app.get("/quality", response_model=List[QualityMetric])
async def get_quality_metrics(order_id: Optional[str] = None, limit: int = 20):
    """Get quality test results"""
    metrics = generate_mock_quality_metrics(limit)
    
    if order_id:
        metrics = [metric for metric in metrics if metric.order_id == order_id]
    
    return metrics

@app.get("/production/stats", response_model=ProductionStats)
async def get_production_stats():
    """Get overall production statistics"""
    orders = generate_mock_orders(50)
    quality_metrics = generate_mock_quality_metrics(100)
    
    total_orders = len(orders)
    completed_orders = len([o for o in orders if o.status == "completed"])
    active_orders = len([o for o in orders if o.status == "in_progress"])
    
    # Calculate metrics
    overall_efficiency = round(random.uniform(85.0, 95.0), 2)
    failed_tests = len([q for q in quality_metrics if q.result == "fail"])
    defect_rate = round((failed_tests / len(quality_metrics)) * 100, 2) if quality_metrics else 0
    on_time_delivery = round(random.uniform(88.0, 97.0), 2)
    
    return ProductionStats(
        total_orders=total_orders,
        completed_orders=completed_orders,
        active_orders=active_orders,
        overall_efficiency=overall_efficiency,
        defect_rate=defect_rate,
        on_time_delivery=on_time_delivery
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

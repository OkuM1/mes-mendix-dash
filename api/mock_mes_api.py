from fastapi import FastAPI, HTTPException
from typing import List

from .database import (
    initialize_db,
    load_sample_data,
    list_orders,
    get_order as db_get_order,
    create_order as db_create_order,
)
from .models import Order

app = FastAPI()

# Initialise SQLite database on startup
initialize_db()
load_sample_data()

@app.get("/api/v1/workorders", response_model=List[Order])
def get_workorders():
    """Return all available work orders."""
    return list_orders()


@app.get("/api/v1/workorders/{order_id}", response_model=Order)
def get_workorder(order_id: str):
    """Return a specific work order."""
    order = db_get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.post("/api/v1/workorders", response_model=Order, status_code=201)
def create_workorder(order: Order):
    """Create a new work order and store it in the database."""
    db_create_order(order)
    return order

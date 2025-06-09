"""SQLite helpers used by the FastAPI app."""

from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path
from typing import List, Optional

from .models import Order


def _db_path() -> Path:
    """Return the current database path from the environment."""
    return Path(os.getenv("DB_PATH", "data/orders.db"))


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(_db_path())


def initialize_db() -> None:
    """Create the orders table if it does not exist."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            line_id TEXT,
            item_name TEXT,
            quantity INTEGER,
            status TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def load_sample_data() -> None:
    """Populate the database with sample JSON orders if empty."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM orders")
    if cur.fetchone()[0] == 0:
        sample = Path("data/sample_orders.json")
        if sample.exists():
            with open(sample) as fh:
                data = json.load(fh)
            for order in data:
                cur.execute(
                    "INSERT INTO orders(order_id, line_id, item_name, quantity, status) VALUES (?,?,?,?,?)",
                    (
                        order["order_id"],
                        order["line_id"],
                        order["item_name"],
                        order["quantity"],
                        order["status"],
                    ),
                )
    conn.commit()
    conn.close()


def list_orders() -> List[Order]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT order_id, line_id, item_name, quantity, status FROM orders")
    rows = cur.fetchall()
    conn.close()
    return [
        Order(
            order_id=row[0], line_id=row[1], item_name=row[2], quantity=row[3], status=row[4]
        )
        for row in rows
    ]


def get_order(order_id: str) -> Optional[Order]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT order_id, line_id, item_name, quantity, status FROM orders WHERE order_id=?",
        (order_id,),
    )
    row = cur.fetchone()
    conn.close()
    if row:
        return Order(
            order_id=row[0], line_id=row[1], item_name=row[2], quantity=row[3], status=row[4]
        )
    return None


def create_order(order: Order) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders(order_id, line_id, item_name, quantity, status) VALUES (?,?,?,?,?)",
        (order.order_id, order.line_id, order.item_name, order.quantity, order.status),
    )
    conn.commit()
    conn.close()


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
from etl.utils import sanitize_orders, compute_kpis


def test_sanitize_orders():
    df = pd.DataFrame([
        {"order_id": "1", "line_id": "L1", "item_name": "Widget", "quantity": "5", "status": " Pending "},
        {"order_id": None, "line_id": "L2", "item_name": "Bad", "quantity": "not_a_number", "status": "IN PROGRESS"},
    ])
    cleaned = sanitize_orders(df)
    assert len(cleaned) == 1
    row = cleaned.iloc[0]
    assert row.quantity == 5
    assert row.status == "pending"


def test_compute_kpis():
    df = pd.DataFrame([
        {"status": "pending"},
        {"status": "completed"},
        {"status": "pending"},
    ])
    result = compute_kpis(df)
    assert result["pending"] == 2
    assert result["completed"] == 1

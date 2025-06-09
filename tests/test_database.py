import os
from pathlib import Path

import sys
from pathlib import Path as P
sys.path.append(str(P(__file__).resolve().parents[1]))

from api import database
from api.models import Order


def test_database_crud(tmp_path):
    os.environ["DB_PATH"] = str(tmp_path / "orders.db")
    database.initialize_db()
    database.load_sample_data()

    all_orders = database.list_orders()
    assert len(all_orders) >= 1

    new = Order(order_id="Z1", line_id="L9", item_name="Thing", quantity=5, status="pending")
    database.create_order(new)
    fetched = database.get_order("Z1")
    assert fetched is not None
    assert fetched.item_name == "Thing"


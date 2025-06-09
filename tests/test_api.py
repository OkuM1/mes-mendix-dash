import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

os.environ["DB_PATH"] = str(Path(__file__).with_name("api_test.db"))

from fastapi.testclient import TestClient
from api.mock_mes_api import app
from api import database

client = TestClient(app)


def teardown_module(module):
    db_file = Path(os.environ["DB_PATH"])
    if db_file.exists():
        db_file.unlink()


def test_get_workorders():
    resp = client.get("/api/v1/workorders")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_create_and_get_workorder():
    new_order = {
        "order_id": "B2001",
        "line_id": "L5",
        "item_name": "NewItem",
        "quantity": 10,
        "status": "pending"
    }
    resp = client.post("/api/v1/workorders", json=new_order)
    assert resp.status_code == 201
    assert resp.json()["order_id"] == "B2001"

    # verify retrieval
    resp2 = client.get("/api/v1/workorders/B2001")
    assert resp2.status_code == 200
    assert resp2.json()["item_name"] == "NewItem"





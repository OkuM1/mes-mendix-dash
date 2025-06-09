# Smart MES Dashboard

A minimal project simulating a Manufacturing Execution System (MES) with:

- 🧠 FastAPI mock MES API with create and query endpoints
- 📊 ETL pipeline in Pandas
- ✅ Order KPI extraction
- 🧪 Pytest unit tests
- 🧰 Makefile automation
- 💾 SQLite data persistence
- ⏱️ Optional ETL scheduler

## How to Run

```bash
make install      # Install dependencies
make run-api      # Start FastAPI server
make run-etl      # Fetch and process MES data
make run-scheduler # Run ETL on a schedule
make test        # Run unit tests
make clean        # Clean Python cache
```

The API exposes the following endpoints:

- `GET /api/v1/workorders` – list all orders
- `GET /api/v1/workorders/{order_id}` – retrieve a single order
- `POST /api/v1/workorders` – create a new order

Orders are persisted in `data/orders.db`. The file is populated from
`data/sample_orders.json` the first time the API runs.

## Example Output

```
Pending Orders:
  order_id line_id item_name  quantity
0    A1001      L1    Widget        50
3    A1004      L4     Gizmo        25

KPI Summary:
pending        2
in progress    1
completed      1
```

Perfect for showcasing skills in data engineering, MES logic, and Python automation.

To keep KPIs fresh, run `make run-scheduler` which executes the ETL script on a
recurring schedule.

# Smart MES Dashboard

A minimal project simulating a Manufacturing Execution System (MES) with:

- 🧠 FastAPI mock MES API
- 📊 ETL pipeline in Pandas
- ✅ Order KPI extraction
- 🧰 Makefile automation

## How to Run

```bash
make install      # Install dependencies
make run-api      # Start FastAPI server
make run-etl      # Fetch and process MES data
make clean        # Clean Python cache
```

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

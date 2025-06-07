from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/api/v1/workorders")
def get_workorders():
    print("Received GET /api/v1/workorders")
    with open("data/sample_orders.json", "r") as file:
        return json.load(file)

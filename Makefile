.PHONY: install run-api run-etl run-scheduler test clean

install:
	pip install -r requirements.txt

run-api:
	uvicorn api.mock_mes_api:app --reload

run-etl:
        python etl/fetch_mes_data.py

run-scheduler:
        python etl/schedule_etl.py

test:
        pytest -q

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

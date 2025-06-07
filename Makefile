.PHONY: install run-api run-etl clean

install:
	pip install -r requirements.txt

run-api:
	uvicorn api.mock_mes_api:app --reload

run-etl:
	python etl/fetch_mes_data.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

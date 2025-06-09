"""Simple scheduler for running the ETL periodically."""

import argparse
import time

import schedule

from etl.fetch_mes_data import main as run_etl


def schedule_etl(api_url: str, interval: int) -> None:
    schedule.every(interval).seconds.do(run_etl, api_url=api_url)
    print(f"Running ETL every {interval} seconds. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ETL on a schedule")
    parser.add_argument("--api-url", default="http://localhost:8000/api/v1/workorders")
    parser.add_argument("--interval", type=int, default=60, help="Interval in seconds")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    schedule_etl(args.api_url, args.interval)


import os
import schedule
import time

from dotenv import load_dotenv

from data import (
    fetch_data,
    process_data,
    write_to_database,
    write_prediction_to_database,
)
from model import create_model, predict_values


load_dotenv()


def main():
    conn_str = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('DB_HOST')}/{os.environ.get('POSTGRES_DB')}"
    model = create_model()
    model.load_weights("model_weights.h5")
    data = process_data(fetch_data())
    write_to_database(conn_str, data)
    write_prediction_to_database(conn_str, data, predict_values(model, data))


def cron_job():
    print("Running the AAPL stock analysis")
    main()


schedule.every(15).minutes.do(cron_job)

while True:
    schedule.run_pending()
    time.sleep(1)

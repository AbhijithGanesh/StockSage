import requests
import pandas as pd

def fetch_data():
    qurl = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/hi/history/AAPL/15m"
    querystring = {"diffandsplits": "false"}
    headers = {
        "X-RapidAPI-Key": "2528d495edmshd59c6a82a27cae3p1fa4fbjsn6bfa1e78424b",
        "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com",
    }
    response = requests.get(qurl, headers=headers, params=querystring)
    data = response.json().get("items").values()
    return list(data)[-1]

def process_data(data):

    df = pd.DataFrame([data])
    df["time"] = pd.to_datetime(df.get("date_utc"), unit="s")
    df.drop(["date_utc"], axis=1, inplace=True)
    df.drop(["date"], axis=1, inplace=True)
    return df

def write_to_database(conn_str, df):
    df.to_sql("stock_data", conn_str, if_exists="append", index=False)

def write_prediction_to_database(conn_str, df, value):
    df["predicted_high"] = value
    df.to_sql("stock_data_predicted", conn_str, if_exists="append", index=False)

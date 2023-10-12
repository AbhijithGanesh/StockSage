# Stock Price Prediction Project

## Introduction

This project aims to predict the stock price of Apple Inc. (AAPL) using data
from Yahoo Finance via the Rapid API. The prediction models are based on SARIMA
(Seasonal Autoregressive Integrated Moving Average) and LSTM (Long Short-Term
Memory) implemented using TensorFlow. The project also utilizes Grafana for data
visualization, PostgreSQL for data storage, FastAPI for REST endpoints, and
Docker for containerization.

## Disclaimers

This is just a sample analysis and it is not financial analysis for Apple Inc or
any stock. I've tested out both SARIMA and LSTM for this project and have stored
the weights of LSTM

## Prerequisites

- [Python 3](https://www.python.org/downloads/)
- [Docker](https://docker.com)
- [Grafana](https://https://grafana.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [TensorFlow](https://www.tensorflow.org/install/pip)
- [Rapid API Key](https://rapidapi.com/search/yahoo%20finance)

## How to get started

- Clone the repository

```bash
git clone https://github.com/AbhijithGanesh/StockSage.git
```

- Set up your environment:

### Refer the [.env.example](.env.example)

```env
POSTGRES_USER=''
POSTGRES_PASSWORD=''
POSTGRES_DB=''
DB_HOST=''
RAPID_API_KEY=''
```

- Installing python dependencies

```bash
pip install -r requirements.txt
```

- Spin up the Docker Instance:

```bash
docker compose up
```

- Run the FastAPI server:

```bash
uvicorn app:app
```

## Acknowledgements

- Thanks to Yahoo Finance and Rapid API for providing the stock price data.
- The SARIMA and LSTM models are built using TensorFlow.
- Grafana and PostgreSQL help with data visualization and storage.
- FastAPI provides the RESTful API for accessing predictions.
- Docker makes the project containerized and deployable.

## Tech Stack

- Data Fetching:
  - Yahoo Finance
  - Rapid API

- Data Storage:
  - PostgreSQL
  - (TimeScaleDB will be implemented in the future)

- Data Visualization:
  - Grafana

- REST Endpoint:
  - FastAPI

- Machine Learning Models:
  - SARIMA
  - LSTM (Long Short-Term Memory) using TensorFlow

- Containerization:
  - Docker

## License

This project is licensed under the [GPL](.LICENSE). Feel free to re-use it😉

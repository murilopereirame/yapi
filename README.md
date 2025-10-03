# 📈 yapi

A small RESTful API wrapper around yfinance that makes stock quotes and historical data available over HTTP.

Lightweight, easy to run locally or in a container. Great for quick integrations, demos, and hacktoberfest contributions.

- Homepage: https://github.com/murilopereirame/yapi
- Language: Python

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
  - [Clone & install](#clone--install)
  - [Run (development)](#run-development)
  - [Run with Docker](#run-with-docker)
- [API](#api)
  - [Endpoints](#endpoints)
  - [Examples](#examples)
- [Configuration / Environment variables](#configuration--environment-variables)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Simple HTTP endpoints to access yfinance data (quotes, history, basic info).
- JSON responses suitable for programmatic consumption.
- Intended to be small and easy to extend.

## Prerequisites

- Python 3.11+
- pip

## Quickstart

### Clone & install

```bash
git clone https://github.com/murilopereirame/yapi.git
cd yapi
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Run (development)

If the API is implemented using FastAPI / Uvicorn (common setup):

```bash
fastapi dev app/main.py
```

## API

This section contains suggested endpoints that yapi typically provides. Adapt to the actual implementation.

Base URL (default local): http://localhost:8000

### Endpoints
- GET /tickers?symbol={SYMBOL}
  - Purpose: Get the current info about a stock ticker.
  - Query params:
    - symbol (required)

### Examples

Get latest quote for Apple (AAPL):

```bash
curl "http://localhost:8000/tickers?symbol=AAPL"
```

Example JSON response (illustrative):

```json
{
  "price": 172.34,
  "query_date": 1759527489,
  "symbol": "AAPL"
}
```

## Development

- Follow standard Python development practices: create a virtualenv, install dependencies.
- Run tests with green + unittest:
  ```bash
  green -vvvv tests/**/*_test.py
  ```

## Contributing

Contributions are welcome! A good workflow:

1. Fork the repository.
2. Create a feature branch: git checkout -b feat/my-change
3. Make changes and add tests.
4. Open a pull request describing your change.

Please follow the repository's existing code style and add tests for new behavior. If you'd like help picking a task, open an issue or label something with "help wanted".

## License

This project is licensed under MIT License. See LICENSE for details.

## Acknowledgements

- [yfinance](https://github.com/ranaroussi/yfinance) — great Python wrapper for Yahoo Finance data.
- [FastAPI](https://github.com/fastapi/fastapi) — high performance, easy to learn, fast to code, ready for production framework.
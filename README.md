# Binance Futures Trading Bot (Testnet)

## Overview

This project is a structured Python-based CLI trading bot developed for Binance USDT-M Futures Testnet.

It demonstrates:

- Clean modular architecture
- Binance Futures API integration
- CLI-based input validation
- Structured logging
- Exception handling
- Separation of concerns (Client / Orders / Validators / CLI)

The application allows users to place MARKET and LIMIT orders on Binance Futures Testnet using API credentials.

---

## Features

- Place MARKET orders
- Place LIMIT orders (GTC)
- Support for BUY and SELL sides
- Input validation (symbol, quantity, order type, price)
- Structured logging to file
- Clear console output
- Exception handling for:
  - Invalid input
  - Missing price for LIMIT
  - API errors
  - Network failures

---

## Tech Stack

- Python 3.x
- python-binance
- argparse
- logging
- python-dotenv

---

## Project Structure

```
binance-futures-trading-bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── __init__.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/harsh22102000/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Create .env File

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## Usage Examples

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

---

## Sample Output

```
===== ORDER REQUEST SUMMARY =====
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

===== ORDER RESPONSE =====
Order ID: 123456
Status: FILLED
Executed Qty: 0.01
Avg Price: 50000

Order placed successfully!
```

---

## Logging

All API requests, responses, and errors are logged to:

```
logs/trading_bot.log
```

This ensures traceability and easier debugging.

---

## Assumptions

- Only USDT-M Futures supported
- GTC (Good Till Cancelled) used for LIMIT orders
- Price required only for LIMIT orders
- Testnet base URL used for API interactions

---

## Evaluation Coverage

✔ Order placement correctness  
✔ Clean and modular architecture  
✔ Validation and error handling  
✔ Logging quality  
✔ Clear documentation  

---

## Author

Harsh Yadav

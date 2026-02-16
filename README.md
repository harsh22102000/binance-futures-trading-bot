# Binance Futures Testnet Trading Bot

## Setup

1. Create Binance Futures Testnet account
2. Generate API key + secret
3. Create .env file:

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

4. Install dependencies:

pip install -r requirements.txt

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Logs

Logs are stored in:
logs/trading_bot.log

## Assumptions

- Only USDT-M Futures supported
- Price required only for LIMIT orders
- GTC used for LIMIT orders

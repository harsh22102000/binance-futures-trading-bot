import argparse
import os
from dotenv import load_dotenv
from bot.logging_config import setup_logging
from bot.orders import place_order

load_dotenv()
setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    print("\n===== ORDER REQUEST SUMMARY =====")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    if args.price:
        print(f"Price: {args.price}")

    try:
        response = place_order(
            api_key,
            api_secret,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Order failed: {str(e)}")

if __name__ == "__main__":
    main()

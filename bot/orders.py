from .client import BinanceFuturesClient
from .validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

def place_order(api_key, api_secret, symbol, side, order_type, quantity, price=None):
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(float(quantity))
    price = validate_price(float(price) if price else None, order_type)

    client = BinanceFuturesClient(api_key, api_secret)

    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    response = client.create_order(**params)
    return response

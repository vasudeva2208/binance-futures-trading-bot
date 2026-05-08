import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True,
    help="Trading symbol example BTCUSDT"
)

parser.add_argument(
    "--side",
    required=True,
    help="BUY or SELL"
)

parser.add_argument(
    "--type",
    required=True,
    help="MARKET or LIMIT"
)

parser.add_argument(
    "--quantity",
    required=True,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    help="Price required for LIMIT orders"
)

args = parser.parse_args()

try:

    symbol = args.symbol.upper()

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    quantity = validate_quantity(args.quantity)

    price = args.price

    if order_type == "LIMIT" and not price:
        raise ValueError("Price is required for LIMIT order")

    response = place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    print("\n===== ORDER SUCCESS =====")

    print("Order ID:", response.get("orderId"))
    print("Symbol:", response.get("symbol"))
    print("Status:", response.get("status"))
    print("Side:", response.get("side"))
    print("Type:", response.get("type"))
    print("Quantity:", response.get("origQty"))
    print("Executed Quantity:", response.get("executedQty"))
    print("Average Price:", response.get("avgPrice"))

except Exception as e:

    print("\nERROR:", e)
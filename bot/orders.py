from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Placing order | Symbol: {symbol} | Side: {side} | Type: {order_type} | Quantity: {quantity} | Price: {price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(
            f"""
ORDER SUCCESS
Order ID: {response.get('orderId')}
Symbol: {response.get('symbol')}
Side: {response.get('side')}
Type: {response.get('type')}
Status: {response.get('status')}
Quantity: {response.get('origQty')}
Executed Quantity: {response.get('executedQty')}
Average Price: {response.get('avgPrice')}
"""
        )

        return response

    except Exception as e:

        logger.error(f"ERROR: {str(e)}")

        raise
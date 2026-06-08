import logging
from binance.exceptions import BinanceAPIException,BinanceOrderException

logger = logging.getLogger('trading_bot')

def place_order(client_wrapper, symbol, side, order_type, quantity, price = None):
    """Constructs, logs, and executes a futures order on the Testnet."""
    try:
        params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }

        if order_type == 'LIMIT':
            params['timeInForce'] = 'GTC'
            params['price'] = price

        # Log the outgoing request so we can inspect it in the log files
        logger.info(f"Sending order requests to Binance : {params}")

        # Execute the order using the underlying python binance client
        response = client_wrapper.client.futures_create_order(**params)

        # Log the successful response tracking ID
        logger.info(f"Order successfully filled/placed. Order ID: {response.get('orderId')}")
        return response
    
    except BinanceAPIException as e:
        # Catches exchange specific issues 
        logger.error(f"Binance API Error Code [{e.status_code}]: {e.message}")
    except BinanceOrderException as e:
        # Catches local syntax errors of the structure of the order
        logger.error(f"Binance Order Validation Error: {e.message}")
    except Exception as e:
        # Catches network issues or unanticipated Python runtime errors
        logger.error(f"Unexpected connectivity or system error: {e}")
    
    return None
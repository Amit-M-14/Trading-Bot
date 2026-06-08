import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger("trading_bot")

class BinanceTestnetClient:
    def __init__(self, api_key, api_secret):
        """Initializes the Binance client specifically for the Futures Testnet."""

        self.client = Client(api_key,api_secret,testnet=True)

        try:
            self.client.futures_ping()
            logger.info("Successfully connected to Binance Futures Testnet.")
        except BinanceAPIException as e:
            logger.error(f"Failed to connect to Binance API: {e}")
            raise
        except Exception as e:
            logger.error(f"Network error occurred during connection: {e}")
            raise
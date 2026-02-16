import logging
from binance.client import Client

logger = logging.getLogger(__name__)

TESTNET_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_URL

    def create_order(self, **kwargs):
        try:
            logger.info(f"Placing order: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.error(f"API Error: {str(e)}")
            raise

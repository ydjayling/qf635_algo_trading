"""

Create a method to send market order. User will specify the following parameters:
    - api key
    - api secret
    - price
    - size
    - side (True=buy, False=sell)

"""

import dotenv
import os

dotenv.load_dotenv('vault/secrets.env')

# TODO
def send_market_order(key: str, secret: str, symbol: str, quantity: float, side: bool):
    pass


if __name__ == '__main__':
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    send_market_order(api_key, api_secret, 'BTCUSDT', 0.1, True)

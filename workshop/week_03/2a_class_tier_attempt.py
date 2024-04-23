"""
Tier represents a price level. Bids and asks are an array of tier.

"""


class Tier:
    def __init__(self, price: float, size: float, quote_id: str = None):
        self.price = price
        self.size = size
        self.quote_id = quote_id

    def __str__(self):
        return '({}, {}, {})'.format(self.price, self.size, self.quote_id)


"""
Order book:
    100,  2     |       101, 5
     99, 50     |       102, 7
     98, 12
"""
# TODO Use Tier class to represent bids and asks in an order book. Compute mid from top-of-book prices.
bids = [(100, 2, 'b1'), (99, 50, 'b2'), (98, 12, 'b3')]
asks = [(101, 5, 'a1'), (102, 7, 'a2')]

bids = [Tier(price, size, quote_id) for price, size, quote_id in bids]
asks = [Tier(price, size, quote_id) for price, size, quote_id in asks]

# Get spread
print("The best bid and ask are: ", bids[0], asks[0])
print("The spread is: ", asks[0].price - bids[0].price)

# Get mid price
print("The mid price is: ", 0.5 * (bids[0].price + asks[0].price))
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+
import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    sku: str, list of sku, count is given by amount of letters

    """

    # this would usually come from a db or similar
    prices = {
        "A": {"price": 50, "offer": (3, 130)},
        "B": {"price": 30, "offer": (2, 45)},
        "C": {"price": 20, "offer": None},
        "D": {"price": 15, "offer": None},
    }

    valid_skus = ["A", "B", "C", "D"]
    if not re.match(r"^[A,B,C,D]*$", skus):
        return -1
    total_cost = 0
    for sku in valid_skus:
        quantity = skus.count(sku)
        if quantity > 0:
            if prices[sku]["offer"]:
                offer_quantity, offer_price = prices[sku]["offer"]
                if quantity >= offer_quantity:
                    match_offer_quantity = quantity//offer_quantity
                    reminder = quantity - (match_offer_quantity*offer_quantity)
                    total_cost += (reminder * prices[sku]["price"]) + (match_offer_quantity * offer_price)
                    print(f"sku: {sku}, price: {prices[sku]['price']}, match_offer_qty: {match_offer_quantity}, reminder: {reminder}")
            else:
                total_cost += quantity * prices[sku]["price"]

    return total_cost




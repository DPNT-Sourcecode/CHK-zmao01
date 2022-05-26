import re

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """
    sku: str, list of sku, count is given by amount of letters

    """

    # this would usually come from a db or similar
    prices = {
        "A": {"price": 50, "offers": [(5, 200, "discount"), (3, 130, "discount")]},
        "B": {"price": 30, "offers": [(2, 45, "discount")]},
        "C": {"price": 20, "offers": []},
        "D": {"price": 15, "offers": []},
        "E": {"price": 40, "offers": [(2, ("B", 1), "free_item")]},
    }

    valid_skus = ["A", "E", "B", "C", "D"]
    if not re.match(r"^[A,B,C,D,E]*$", skus):
        return -1
    total_cost = 0
    free_items = {}
    for sku in valid_skus:
        quantity = skus.count(sku)
        if quantity > 0:
            if sku in free_items:
                quantity -= free_items[sku]
            to_process = quantity
            for offer in prices[sku]["offers"]:
                offer_quantity, offer_price, offer_type = offer

                if to_process >= offer_quantity:
                    if offer_type == "discount":
                        match_offer_quantity = to_process // offer_quantity
                        to_process = to_process - (match_offer_quantity * offer_quantity)
                        total_cost += (match_offer_quantity * offer_price)
                        continue
                    elif offer_type == "free_item":
                        match_offer_quantity = to_process // offer_quantity
                        free_item, free_item_quantity = offer_price
                        free_items[free_item] = free_item_quantity*match_offer_quantity

            if to_process > 0:
                total_cost += (to_process * prices[sku]["price"])

    return total_cost


# def checkout_1(skus: str) -> int:
#     """
#     sku: str, list of sku, count is given by amount of letters
#
#     """
#
#     # this would usually come from a db or similar
#     prices = {
#         "A": {"price": 50, "offer": (3, 130)},
#         "B": {"price": 30, "offer": (2, 45)},
#         "C": {"price": 20, "offer": None},
#         "D": {"price": 15, "offer": None},
#     }
#
#     valid_skus = ["A", "B", "C", "D"]
#     if not re.match(r"^[A,B,C,D]*$", skus):
#         return -1
#     total_cost = 0
#     for sku in valid_skus:
#         quantity = skus.count(sku)
#         if quantity > 0:
#             if prices[sku]["offer"]:
#                 offer_quantity, offer_price = prices[sku]["offer"]
#                 if quantity >= offer_quantity:
#                     match_offer_quantity = quantity // offer_quantity
#                     reminder = quantity - (match_offer_quantity * offer_quantity)
#                     total_cost += (reminder * prices[sku]["price"]) + (match_offer_quantity * offer_price)
#
#                     continue
#
#             total_cost += quantity * prices[sku]["price"]
#
#     return total_cost
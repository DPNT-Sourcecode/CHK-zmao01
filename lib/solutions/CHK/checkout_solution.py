import re

# Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
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
        "F": {"price": 10, "offers": [(3, 20, "discount")]},
        "G": {"price": 20, "offers": []},
        "H": {"price": 10, "offers": [(10, 80, "discount"), (5, 45, "discount")]},
        "I": {"price": 35, "offers": []},
        "J": {"price": 60, "offers": []},
        "K": {"price": 70, "offers": [(2, 150, "discount")]},
        "L": {"price": 90, "offers": []},
        "M": {"price": 15, "offers": []},
        "N": {"price": 40, "offers": [(3, ("M", 1), "free_item")]},
        "O": {"price": 10, "offers": []},
        "P": {"price": 50, "offers": [(5, 200, "discount")]},
        "Q": {"price": 30, "offers": [(3, 80, "discount")]},
        "R": {"price": 50, "offers": [(3, ("Q", 1), "free_item")]},
        "S": {"price": 20, "offers": []},
        "T": {"price": 20, "offers": []},
        "U": {"price": 40, "offers": [(4, 120, "discount")]},
        "V": {"price": 50, "offers": [(3, 130, "discount"), (2, 90, "discount")]},
        "W": {"price": 20, "offers": []},
        "X": {"price": 17, "offers": []},
        "Y": {"price": 20, "offers": []},
        "Z": {"price": 21, "offers": []},
    }

    group_offer = {
        "skus": ["Z", "T", "S", "Y", "X"],
        "quantity": 3,
        "price": 45
    }

    valid_skus = ["A", "E", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "N", "M", "O", "P", "R", "Q", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if not re.match(r"^[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]*$", skus):
        return -1
    total_cost = 0
    free_items = {}

    group_offers = {
        "total_quantity": 0,
        "skus_quantity": {}
    }

    # applying group offer before processing cart
    for sku in group_offer['skus']:
        sku_quantity = skus.count(sku)
        group_offers["total_quantity"] += sku_quantity
        group_offers["skus_quantity"][sku] = sku_quantity

    match_group_offer_quantity = group_offers["total_quantity"] // group_offer["quantity"]
    to_process = group_offers["total_quantity"] - (match_group_offer_quantity * group_offer["quantity"])
    total_cost += (match_group_offer_quantity * group_offer["quantity"])

    for sku, quantity in group_offers["skus_quantity"].items()



    for sku in valid_skus:
        # count amount for each sku
        quantity = skus.count(sku)
        if quantity > 0:
            # only process skus that are in the cart
            if sku in free_items:
                # remove any free items from previous offers
                quantity -= free_items[sku]
            to_process = quantity

            for offer in prices[sku]["offers"]:
                # if the sku has an offer, process it
                offer_quantity, offer_price, offer_type = offer

                if to_process >= offer_quantity:
                    # only process if the sku matches the required quantity to trigger the offer
                    # (this relies on offers being in order)
                    if offer_type == "discount":
                        # if the order is a simple discount, apply it, treat sku that don't trigger offer normally
                        match_offer_quantity = to_process // offer_quantity
                        to_process = to_process - (match_offer_quantity * offer_quantity)
                        total_cost += (match_offer_quantity * offer_price)
                        continue
                    elif offer_type == "free_item":
                        # if the offer give a free item, add the free item to the list of free skus.
                        # this too relies on the order in which skus are processed
                        match_offer_quantity = to_process // offer_quantity
                        free_item, free_item_quantity = offer_price
                        free_items[free_item] = free_item_quantity*match_offer_quantity

            if to_process > 0:
                # this code deal with sku with no offers (and leftover skus from items that had offers)
                total_cost += (to_process * prices[sku]["price"])

    return total_cost

# def checkout_4(skus: str) -> int:
#     """
#     sku: str, list of sku, count is given by amount of letters
#
#     """
#
#     # this would usually come from a db or similar
#     prices = {
#         "A": {"price": 50, "offers": [(5, 200, "discount"), (3, 130, "discount")]},
#         "B": {"price": 30, "offers": [(2, 45, "discount")]},
#         "C": {"price": 20, "offers": []},
#         "D": {"price": 15, "offers": []},
#         "E": {"price": 40, "offers": [(2, ("B", 1), "free_item")]},
#         "F": {"price": 10, "offers": [(3, 20, "discount")]},
#         "G": {"price": 20, "offers": []},
#         "H": {"price": 10, "offers": [(10, 80, "discount"), (5, 45, "discount")]},
#         "I": {"price": 35, "offers": []},
#         "J": {"price": 60, "offers": []},
#         "K": {"price": 80, "offers": [(2, 150, "discount")]},
#         "L": {"price": 90, "offers": []},
#         "M": {"price": 15, "offers": []},
#         "N": {"price": 40, "offers": [(3, ("M", 1), "free_item")]},
#         "O": {"price": 10, "offers": []},
#         "P": {"price": 50, "offers": [(5, 200, "discount")]},
#         "Q": {"price": 30, "offers": [(3, 80, "discount")]},
#         "R": {"price": 50, "offers": [(3, ("Q", 1), "free_item")]},
#         "S": {"price": 30, "offers": []},
#         "T": {"price": 20, "offers": []},
#         "U": {"price": 40, "offers": [(4, 120, "discount")]},
#         "V": {"price": 50, "offers": [(3, 130, "discount"), (2, 90, "discount")]},
#         "W": {"price": 20, "offers": []},
#         "X": {"price": 90, "offers": []},
#         "Y": {"price": 10, "offers": []},
#         "Z": {"price": 50, "offers": []},
#     }
#
#     valid_skus = ["A", "E", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "N", "M", "O", "P", "R", "Q", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#     if not re.match(r"^[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]*$", skus):
#         return -1
#     total_cost = 0
#     free_items = {}
#     for sku in valid_skus:
#         quantity = skus.count(sku)
#         if quantity > 0:
#             if sku in free_items:
#                 quantity -= free_items[sku]
#             to_process = quantity
#             for offer in prices[sku]["offers"]:
#                 offer_quantity, offer_price, offer_type = offer
#
#                 if to_process >= offer_quantity:
#                     if offer_type == "discount":
#                         match_offer_quantity = to_process // offer_quantity
#                         to_process = to_process - (match_offer_quantity * offer_quantity)
#                         total_cost += (match_offer_quantity * offer_price)
#                         continue
#                     elif offer_type == "free_item":
#                         match_offer_quantity = to_process // offer_quantity
#                         free_item, free_item_quantity = offer_price
#                         free_items[free_item] = free_item_quantity*match_offer_quantity
#
#             if to_process > 0:
#                 total_cost += (to_process * prices[sku]["price"])
#
#     return total_cost



# def checkout_3(skus: str) -> int:
#     """
#     sku: str, list of sku, count is given by amount of letters
#
#     """
#
#     # this would usually come from a db or similar
#     prices = {
#         "A": {"price": 50, "offers": [(5, 200, "discount"), (3, 130, "discount")]},
#         "B": {"price": 30, "offers": [(2, 45, "discount")]},
#         "C": {"price": 20, "offers": []},
#         "D": {"price": 15, "offers": []},
#         "E": {"price": 40, "offers": [(2, ("B", 1), "free_item")]},
#         "F": {"price": 10, "offers": [(3, 20, "discount")]}
#     }
#
#     valid_skus = ["A", "E", "B", "C", "D", "F"]
#     if not re.match(r"^[A,B,C,D,E,F]*$", skus):
#         return -1
#     total_cost = 0
#     free_items = {}
#     for sku in valid_skus:
#         quantity = skus.count(sku)
#         if quantity > 0:
#             if sku in free_items:
#                 quantity -= free_items[sku]
#             to_process = quantity
#             for offer in prices[sku]["offers"]:
#                 offer_quantity, offer_price, offer_type = offer
#
#                 if to_process >= offer_quantity:
#                     if offer_type == "discount":
#                         match_offer_quantity = to_process // offer_quantity
#                         to_process = to_process - (match_offer_quantity * offer_quantity)
#                         total_cost += (match_offer_quantity * offer_price)
#                         continue
#                     elif offer_type == "free_item":
#                         match_offer_quantity = to_process // offer_quantity
#                         free_item, free_item_quantity = offer_price
#                         free_items[free_item] = free_item_quantity*match_offer_quantity
#
#             if to_process > 0:
#                 total_cost += (to_process * prices[sku]["price"])
#
#     return total_cost


# def checkout_2(skus: str) -> int:
#     """
#     sku: str, list of sku, count is given by amount of letters
#
#     """
#
#     # this would usually come from a db or similar
#     prices = {
#         "A": {"price": 50, "offers": [(5, 200, "discount"), (3, 130, "discount")]},
#         "B": {"price": 30, "offers": [(2, 45, "discount")]},
#         "C": {"price": 20, "offers": []},
#         "D": {"price": 15, "offers": []},
#         "E": {"price": 40, "offers": [(2, ("B", 1), "free_item")]},
#     }
#
#     valid_skus = ["A", "E", "B", "C", "D"]
#     if not re.match(r"^[A,B,C,D,E]*$", skus):
#         return -1
#     total_cost = 0
#     free_items = {}
#     for sku in valid_skus:
#         quantity = skus.count(sku)
#         if quantity > 0:
#             if sku in free_items:
#                 quantity -= free_items[sku]
#             to_process = quantity
#             for offer in prices[sku]["offers"]:
#                 offer_quantity, offer_price, offer_type = offer
#
#                 if to_process >= offer_quantity:
#                     if offer_type == "discount":
#                         match_offer_quantity = to_process // offer_quantity
#                         to_process = to_process - (match_offer_quantity * offer_quantity)
#                         total_cost += (match_offer_quantity * offer_price)
#                         continue
#                     elif offer_type == "free_item":
#                         match_offer_quantity = to_process // offer_quantity
#                         free_item, free_item_quantity = offer_price
#                         free_items[free_item] = free_item_quantity*match_offer_quantity
#
#             if to_process > 0:
#                 total_cost += (to_process * prices[sku]["price"])
#
#     return total_cost


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


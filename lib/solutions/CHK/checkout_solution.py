# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+
from random import randint

prices = {
    "A": {"price": 50, "offer": (3, 130)},
    "B": {"price": 30, "offer": (2, 45)},
    "C": {"price": 20, "offer": None},
    "D": {"price": 15, "offer": None},
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    randint(100,1000)




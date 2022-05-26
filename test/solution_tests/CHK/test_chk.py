import pytest
from solutions.CHK import checkout_solution

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


class TestCheckout():
    def test_checkout_invalid(self):
        assert checkout_solution.checkout("3qwgyh5") == -1

    @pytest.mark.parametrize(
        "skus,expected", [
            ("AAAAAAAAA", 380),
            # ("CCCCD", 95),
            # ("A", 50),
            # ("AAA", 130),
            # ("AAAA", 180),
            # ("AAAAB", 210),
            # ("BBA", 95),
            # ("BC", 50),
            # ("AAB", 130),
            # ("AAAB", 160),
        ]
    )
    def test_checkout_happy(self, skus: str, expected: int):
        assert checkout_solution.checkout(skus) == expected


# class TestCheckout1():
#     def test_checkout_invalid(self):
#         assert checkout_solution.checkout("3qwgyh5") == -1
#
#     @pytest.mark.parametrize(
#         "skus,expected", [
#             ("CCCCC", 100),
#             ("CCCCD", 95),
#             ("A", 50),
#             ("AAA", 130),
#             ("AAAA", 180),
#             ("AAAAB", 210),
#             ("BBA", 95),
#             ("BC", 50),
#             ("AAB", 130),
#             ("AAAB", 160),
#         ]
#     )
#     def test_checkout_happy(self, skus: str, expected: int):
#         assert checkout_solution.checkout(skus) == expected

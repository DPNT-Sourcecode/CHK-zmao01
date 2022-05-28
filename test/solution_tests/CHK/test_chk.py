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
            ("CCCCD", 95),
            ("A", 50),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAB", 210),
            ("BBA", 95),
            ("BC", 50),
            ("AAB", 130),
            ("AAAB", 160),
            ("AAAAAAAAAB", 410),
            ("EEB", 80),
            ("AAAAAAAAAEE", 460),
            ("AAAAAAAAAEE", 460),
            ("AAAAAAAAAEEB", 460),
            ("AAAAAAAAAEEBB", 490),
            ("AAAAAAAAAEEBBB", 505),
            ("EEBEE", 160),
            ("EEBBEE", 160),
            ("EEBBEEB", 190),
            ("EEBBBBEE", 205),
            ("F", 10),
            ("FF", 20),
            ("FFF", 20),
            ("FFFF", 30),
            ("FFFFFF", 40),
            ("FFFFFFF", 50),
            ("HHHHHHHHHH", 80),
            ("Z", 21),
            ("ZZ", 42),
            ("ZZZ", 45),
            ("ZZZZ", 66),
            ("STX", 45),
            ("STY", 45),
            ("XYZ", 45),
            ("XYZZ", 62),
            ("SSSS", 65),
            ("SSSSSS", 90),
            ("SSSSSSSSS", 135),
            ("SSSSAAAAASSSSS", 335),
            ("STTZ", 65),
            ("SSXS", 62),
            ("ZXXXXZX", 107)

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






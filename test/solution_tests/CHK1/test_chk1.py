import pytest
from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_normal(self):
        assert checkout_solution.checkout("AAB") == 130

    def test_checkout_discount(self):
        assert checkout_solution.checkout("AAAB") == 160

    def test_checkout_invalid(self):
        assert checkout_solution.checkout("3qwgyh5") == -1


    @pytest.mark.parametrize(
        "skus,expected", [
            ("CCCCC", 100),
            ("CCCCD", 95),
            ("A", 50),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAB", 220),
            ("BBA", 95),
            ("BC", 50),
        ]
    )
    def test_checkout_happy(self, skus: str, expected: int):
        assert checkout_solution.checkout(skus) == expected




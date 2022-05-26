from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_normal(self):
        assert checkout_solution.checkout("AAB") == 130

    def test_checkout_discount(self):
        assert checkout_solution.checkout("AAAB") == 160

    def test_checkout_invalid(self):
        assert checkout_solution.checkout("3qwgyh5") == -1


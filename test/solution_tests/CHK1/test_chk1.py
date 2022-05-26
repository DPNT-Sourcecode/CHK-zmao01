from solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_normal(self):
        assert checkout_solution.checkout("A1B2") == 110

    def test_checkout_discount(self):
        assert checkout_solution.checkout("A3B2") == 190

    def test_checkout_invalid(self):
        assert checkout_solution.checkout("3qwgyh5") == -1


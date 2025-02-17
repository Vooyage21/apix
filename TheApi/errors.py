class InvalidAmountError(Exception):
    def __init__(self, amount):
        super().__init__(
            f"Invalid amount of jokes requested: {amount}. Maximum allowed is 10. Minimum allowed is 1."
        )
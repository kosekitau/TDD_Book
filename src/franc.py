from .money import Money


class Franc(Money):
    def __init__(self, amount: int) -> None:
        self.amount: int = amount
        self.currency = "CHF"

    def times(self, multiplier: int) -> int:
        return Franc(amount=self.amount * multiplier)

from .money import Money


class Franc(Money):
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def times(self, multiplier: int) -> int:
        return Money.franc(amount=self.amount * multiplier)

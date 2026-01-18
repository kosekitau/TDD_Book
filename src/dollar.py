from typing import Literal
from .money import Money


class Dollar(Money):
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def times(self, multiplier: int) -> int:
        return Money.dollar(amount=self.amount * multiplier)

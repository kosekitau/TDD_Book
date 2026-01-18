from typing import Literal
from .money import Money


class Dollar(Money):
    def __init__(self, amount: int) -> None:
        self.amount: int = amount
        self.currency = "USD"

    def times(self, multiplier: int) -> int:
        return Dollar(amount=self.amount * multiplier)

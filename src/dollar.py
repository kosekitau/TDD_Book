from typing import Literal
from .money import Money


class Dollar(Money):
    def times(self, multiplier: int) -> int:
        return Dollar(amount=self.amount * multiplier)

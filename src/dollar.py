from typing import Literal


class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount
        pass

    def times(self, multiplier: int) -> int:
        return self.amount * multiplier

    def equals(self, other) -> bool:
        if not isinstance(other, Dollar):
            return False
        return self.amount == other.amount

from typing import TYPE_CHECKING
from src.expression import Expression


class Sum(Expression):

    def __init__(self, augend, addend) -> None:
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to: str) -> "Money":
        from src.money import Money

        amount: int = (
            self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        )
        return Money(amount=amount, currency=to)

    def plus(self, addend) -> "Sum":
        return Sum(augend=self, addend=addend)

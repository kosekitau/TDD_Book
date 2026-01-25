from src.expression import Expression
from src.money import Money
from src.sum_ import Sum


class Bank:
    def reduce(self, source: Expression, to: str):
        sum_ = source
        return sum_.reduce(to)

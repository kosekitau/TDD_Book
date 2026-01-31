from src.expression import Expression
from src.money import Money


class Bank:
    def reduce(self, source: Expression, to: str):
        sum_: Expression = source
        return sum_.reduce(to)

    def addRate(self, from_, to, rate):
        pass

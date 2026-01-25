from src.expression import Expression
from src.money import Money


class Bank:
    def reduce(self, source: Expression, to: str):
        if isinstance(source, Money):
            return source
        sum_: Expression = source
        return sum_.reduce(to)

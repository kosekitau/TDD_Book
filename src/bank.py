from src.expression import Expression
from src.money import Money


class Bank:
    def reduce(self, source: Expression, to: str):
        return source.reduce(self, to)

    def addRate(self, from_, to, rate):
        pass

    def rate(self, from_, to) -> int:
        rate: int = 2 if from_ == "CHF" and to == "USD" else 1
        return rate

from src.expression import Expression
from src.money import Money


class Bank:
    def __init__(self) -> None:
        self.rates: dict = {}

    def reduce(self, source: Expression, to: str) -> None:
        return source.reduce(bank=self, to=to)

    def addRate(self, from_, to, rate) -> None:
        self.rates[(from_, to)] = rate

    def rate(self, from_, to) -> int:
        if from_ == to:
            return 1
        return self.rates[(from_, to)]

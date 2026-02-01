from abc import ABC
from src.expression import Expression


class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return (self.amount == other.amount) and (self.currency == other.currency)

    def times(self, multiplier: int) -> Expression:
        return Money(amount=self.amount * multiplier, currency=self.currency)

    def return_currency(self) -> str:
        return self.currency

    def plus(self, addend: Expression) -> "Sum":
        from src.sum_ import Sum

        return Sum(augend=self, addend=addend)

    def reduce(self, bank, to: str) -> "Money":
        rate: int = bank.rate(self.currency, to)
        return Money(amount=self.amount / rate, currency=to)

    # staticmethodはインスタンスを作らず直接このmethodを呼び出せる
    # ex):Money.dollar()と書くだけでDollar(amount)を返す
    @staticmethod
    def dollar(amount: int) -> "Money":
        return Money(amount=amount, currency="USD")

    @staticmethod
    def franc(amount: int) -> "Money":
        return Money(amount=amount, currency="CHF")

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

    def times(self, multiplier: int) -> None:
        return Money(amount=self.amount * multiplier, currency=self.currency)

    def return_currency(self) -> str:
        return self.currency

    def plus(self, addend):
        return Money(amount=addend.amount + self.amount, currency=self.currency)

    # staticmethodはインスタンスを作らず直接このmethodを呼び出せる
    # ex):Money.dollar()と書くだけでDollar(amount)を返す
    @staticmethod
    def dollar(amount: int):
        return Money(amount=amount, currency="USD")

    @staticmethod
    def franc(amount: int):
        return Money(amount=amount, currency="CHF")

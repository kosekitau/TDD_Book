from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return (self.amount == other.amount) and (self.__class__ == other.__class__)

    @abstractmethod
    def times(self, multiplier: int) -> None:
        pass

    def return_currency(self) -> str:
        return self.currency

    # staticmethodはインスタンスを作らず直接このmethodを呼び出せる
    # ex):Money.dollar()と書くだけでDollar(amount)を返す
    @staticmethod
    def dollar(amount: int) -> "Dollar":
        # 循環参照を避けるためメソッド内呼び出し
        from .dollar import Dollar

        return Dollar(amount=amount, currency="USD")

    @staticmethod
    def franc(amount: int) -> "Franc":
        from .franc import Franc

        return Franc(amount=amount, currency="CHF")

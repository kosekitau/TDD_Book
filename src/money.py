from abc import ABC, abstractmethod


class Money:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return (self.amount == other.amount) and (self.__class__ == other.__class__)

    # staticmethodはインスタンスを作らず直接このmethodを呼び出せる
    # ex):Money.dollar()と書くだけでDollar(amount)を返す
    @staticmethod
    def dollar(amount: int) -> "Dollar":
        # 循環参照を避けるためメソッド内呼び出し
        from .dollar import Dollar

        return Dollar(amount=amount)

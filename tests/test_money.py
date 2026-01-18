import pytest
from src.dollar import Dollar
from src.franc import Franc
from src.money import Money


class Test_Money:
    def test_Multiplication(self) -> None:
        five: Dollar = Money.dollar(amount=5)
        assert Dollar(amount=10) == five.times(2)
        assert Dollar(amount=15) == five.times(3)

    def test_Equality(self) -> None:
        assert Dollar(amount=5) == Dollar(amount=5)
        assert Dollar(amount=5) != Dollar(amount=6)
        assert Franc(amount=5) == Franc(amount=5)
        assert Franc(amount=5) != Franc(amount=6)
        assert Dollar(amount=5) != Franc(amount=5)

    def test_FrancMultiplication(self) -> None:
        five = Franc(amount=5)
        assert Franc(amount=10) == five.times(2)
        assert Franc(amount=15) == five.times(3)

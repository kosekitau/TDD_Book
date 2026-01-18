import pytest
from src.money import Money


class Test_Money:
    def test_Multiplication(self) -> None:
        five = Money.dollar(amount=5)
        assert Money.dollar(amount=10) == five.times(2)
        assert Money.dollar(amount=15) == five.times(3)

    def test_Equality(self) -> None:
        assert Money.dollar(amount=5) == Money.dollar(amount=5)
        assert Money.dollar(amount=5) != Money.dollar(amount=6)
        assert Money.franc(amount=5) == Money.franc(amount=5)
        assert Money.franc(amount=5) != Money.franc(amount=6)
        assert Money.dollar(amount=5) != Money.franc(amount=5)

    def test_FrancMultiplication(self) -> None:
        five = Money.franc(amount=5)
        assert Money.franc(amount=10) == five.times(2)
        assert Money.franc(amount=15) == five.times(3)

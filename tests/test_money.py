import pytest
from src.dollar import Dollar
from src.franc import Franc


class Test_Money:
    def test_Multiplication(self) -> None:
        five = Dollar(amount=5)
        product: int = five.times(multiplier=2)
        assert Dollar(amount=10) == product
        product = five.times(multiplier=3)
        assert Dollar(amount=15) == product

    def test_Equality(self) -> None:
        assert Dollar(amount=5) == Dollar(amount=5)
        assert Dollar(amount=5) != Dollar(amount=6)
        assert Franc(amount=5) == Franc(amount=5)
        assert Franc(amount=5) != Franc(amount=6)

    def test_FrancMultiplication(self) -> None:
        five = Franc(amount=5)
        assert Franc(amount=10) == five.times(2)
        assert Franc(amount=15) == five.times(3)

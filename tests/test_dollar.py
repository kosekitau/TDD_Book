import pytest
from src.dollar import Dollar


class Test_Money:
    def test_Multiplication(self) -> None:
        five = Dollar(amount=5)
        five.times(multiplier=2)
        assert 10 == five.amount
        five.times(multiplier=3)
        assert 15 == five.amount

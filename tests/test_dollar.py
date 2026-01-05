import pytest
from src.dollar import Dollar


class Test_Money:
    def test_Multiplication(self) -> None:
        five = Dollar(amount=5)
        product: int = five.times(multiplier=2)
        assert 10 == product
        product = five.times(multiplier=3)
        assert 15 == product

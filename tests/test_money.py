import pytest
from src.money import Money


class Test_Money:
    def test_Multiplication(self) -> None:
        five: Money = Money.dollar(amount=5)
        assert Money.dollar(amount=10) == five.times(multiplier=2)
        assert Money.dollar(amount=15) == five.times(multiplier=3)

    def test_Equality(self) -> None:
        assert Money.dollar(amount=5) == Money.dollar(amount=5)
        assert Money.dollar(amount=5) != Money.dollar(amount=6)
        assert Money.dollar(amount=5) != Money.franc(amount=5)

    def test_Currency(self) -> None:
        assert "CHF" == Money.franc(amount=1).return_currency()
        assert "USD" == Money.dollar(amount=1).return_currency()

    def test_SimpleAddition(self) -> None:
        money = Money.dollar(amount=5).plus(Money.dollar(amount=5))
        assert money == Money.dollar(amount=10)

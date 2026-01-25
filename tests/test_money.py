import pytest
from src.money import Money
from src.bank import Bank
from src.expression import Expression
from src.sum_ import Sum


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
        five = Money.dollar(amount=5)
        sum_ = five.plus(addend=five)
        bank = Bank()
        reduced = bank.reduce(
            source=sum_, to="USD"
        )  # reduceは式を単純な形に変形させるの意味
        assert reduced == Money.dollar(amount=10)

    def test_PlusReturnSum(self):
        five = Money.dollar(amout=5)
        result: Expression = five.plus(five)
        sum_: Sum = Sum(result)
        assert five == sum.augend
        assert five == sum.addend

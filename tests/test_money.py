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
        five: Money = Money.dollar(amount=5)
        sum_ = five.plus(addend=five)
        bank = Bank()
        reduced = bank.reduce(
            source=sum_, to="USD"
        )  # reduceは式を単純な形に変形させるの意味
        assert reduced == Money.dollar(amount=10)

    def test_PlusReturnSum(self) -> None:
        five: Money = Money.dollar(amount=5)
        sum_: Sum = five.plus(addend=five)
        assert five == sum_.augend  # 被加算数
        assert five == sum_.addend  # 加数

    def test_ReduceSum(self) -> None:
        sum_: Sum[Money, Money] = Sum(
            augend=Money.dollar(amount=3), addend=Money.dollar(amount=4)
        )
        bank = Bank()
        result = bank.reduce(source=sum_, to="USD")
        assert result == Money.dollar(amount=7)

    def test_ReduceMoney(self) -> None:
        bank = Bank()
        result = bank.reduce(source=Money.dollar(amount=1), to="USD")
        assert result == Money(amount=1, currency="USD")

    def test_ReduceMoneyDifferentCurrency(self) -> None:
        bank = Bank()
        bank.addRate(from_="CHF", to="USD", rate=2)  # 2フランは1ドル
        result = bank.reduce(source=Money.franc(amount=2), to="USD")
        assert result == Money.dollar(amount=1)

    def test_IdentityRate(self) -> None:
        bank = Bank()
        assert 1 == bank.rate(from_="USD", to="USD")

    def test_MixedAddition(self) -> None:
        fiveBucks: Expression = Money.dollar(amount=5)
        tenFrancs: Expression = Money.franc(amount=10)
        bank = Bank()
        bank.addRate(from_="CHF", to="USD", rate=2)
        result = bank.reduce(source=fiveBucks.plus(addend=tenFrancs), to="USD")
        assert result == Money.dollar(amount=10)

    def test_SumPlusMoeny(self) -> None:
        fiveBucks: Expression = Money.dollar(amount=5)
        tenFrancs: Expression = Money.franc(amount=10)
        bank = Bank()
        bank.addRate(from_="CHF", to="USD", rate=2)
        sum_ = Sum(augend=fiveBucks, addend=tenFrancs).plus(addend=fiveBucks)
        result = bank.reduce(source=sum_, to="USD")
        assert result == Money.dollar(amount=15)

    def test_SumTimes(self):
        fiveBucks: Expression = Money.dollar(amount=5)
        tenFrancs: Expression = Money.franc(amount=10)
        bank = Bank()
        bank.addRate(from_="CHF", to="USD", rate=2)
        sum_ = Sum(augend=fiveBucks, addend=tenFrancs).times(2)
        result = bank.reduce(source=sum_, to="USD")
        assert result == Money.dollar(amount=20)

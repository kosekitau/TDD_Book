from src.dollar import Dollar


class Test_Monkey:
    def test_Multiplication(self) -> None:
        five = Dollar(amount=5)
        five.times(multiplier=2)
        assert 10 == five.amount

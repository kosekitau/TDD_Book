from src.dollar import Dollar


class Test_Monkey:
    def test_Multiplication(self):
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount

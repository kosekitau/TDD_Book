class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount
        pass

    def times(self, multiplier: int) -> None:
        self.amount *= multiplier

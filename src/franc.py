class Franc:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount

    def times(self, multiplier: int) -> int:
        return Franc(amount=self.amount * multiplier)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Franc):
            return False
        return self.amount == other.amount

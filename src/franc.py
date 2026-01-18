from .money import Money


class Franc(Money):
    def times(self, multiplier: int) -> int:
        return Franc(amount=self.amount * multiplier)

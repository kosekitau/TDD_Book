class Money:
    def __init__(self, amount: int) -> None:
        self.amount: int = amount

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return (self.amount == other.amount) and (self.__class__ == other.__class__)

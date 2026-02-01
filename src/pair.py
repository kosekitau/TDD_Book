class Pair:
    def __init__(self, from_: str, to: str) -> None:
        self.from_: str = from_
        self.to: str = to

    def __eq__(self, other: object) -> None:
        return (self.from_ == other.from_) and (self.to == other.to)

    def hashCode(self) -> int:
        return 0

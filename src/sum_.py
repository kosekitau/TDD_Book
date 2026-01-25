from src.expression import Expression


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

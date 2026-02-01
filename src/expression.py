from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to) -> None:
        pass

    @abstractmethod
    def plus(self, addend) -> None:
        pass

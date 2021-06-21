from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass
    
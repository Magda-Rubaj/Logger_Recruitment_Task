from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self, file: str) -> None:
        super().__init__()
        self.file = file

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def retrieve(self):
        raise NotImplementedError
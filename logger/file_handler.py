import pickle
from typing import List
from .handler import Handler
from .log_entry import LogEntry


class FileHandler(Handler):
    def __init__(self, file: str) -> None:
        super().__init__(file)

    def save(self, log) -> None:
        with open(self.file, 'ab') as f:
            pickle.dump(log, f)

    def retrieve(self) -> List[LogEntry]:
        logs = []
        with open(self.file, 'rb') as f:
            while True:
                try:
                    logs.append(pickle.load(f))
                except EOFError:
                    break
        return logs

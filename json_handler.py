from log_entry import LogEntry
from handler import Handler
import json
import os


class JsonHandler(Handler):
    def __init__(self, file: str) -> None:
        super().__init__(file)

    def save(self, log) -> None:
        super().save()
        if not os.path.exists(self.file):
            with open(self.file, 'w+'):
                logs = []
        else:
            with open(self.file) as f:
                content = f.read()
                logs = json.loads(content)

        logs.append(log.__dict__)
        with open(self.file, 'w') as f:
            json.dump(logs, f)

    def retrieve(self):
        super().retrieve()
        with open(self.file, 'r') as f:
            logs = json.load(f, object_hook=lambda d: LogEntry(**d))
        return logs
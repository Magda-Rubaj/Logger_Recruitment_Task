from handler import Handler
import json
import os


class JsonHandler(Handler):
    def __init__(self, file: str) -> None:
        super().__init__(file)

    def save(self, log):
        super().save()
        with open(self.file, 'r+') as f:
            if os. stat(self.file).st_size == 0:
                logs = []
            else:
                logs = json.load(f)
        logs.append(log.__dict__)
        with open(self.file, 'w+') as f:
            json.dump(logs, f)

    def retrieve(self):
        super().retrieve()
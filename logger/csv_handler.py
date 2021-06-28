from .log_entry import LogEntry
from .handler import Handler
import csv


class CSVHandler(Handler):
    def __init__(self, file: str) -> None:
        super().__init__(file)

    def save(self, log):
        with open(self.file, 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(log.get_row())
        
    def retrieve(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            logs = [LogEntry(*entry) for entry in reader]
        return logs
        
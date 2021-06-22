from datetime import datetime


class LogEntry(object):

    def __init__(self, date: datetime, level: str, msg: str) -> None:
        self.date = date.__str__()
        self.level = level
        self.msg = msg
    
    def get_row(self):
        return [self.date, self.level, self.msg]

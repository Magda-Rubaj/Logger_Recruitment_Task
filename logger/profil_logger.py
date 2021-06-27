from datetime import datetime
from log_entry import LogEntry


class ProfilLogger(object):

    def __init__(self, handlers) -> None:
        self.handlers = handlers

    def _log(self, msg: str, level: str) -> None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_log = LogEntry(date, level, msg)
        for handler in self.handlers:
            handler.save(new_log)

    def info(self, msg: str) -> None:
        level = "INFO"
        self._log(msg, level)

    def warning(self, msg: str) -> None:
        level = "WARNING"
        self._log(msg, level)

    def critical(self, msg: str) -> None:
        level = "CRITICAL"
        self._log(msg, level)

    def error(self, msg: str) -> None:
        level = "ERROR"
        self._log(msg, level)

    def debug(self, msg: str) -> None:
        level = "DEBUG"
        self._log(msg, level)

    def set_log_level(self, msg: str) -> None:
        pass

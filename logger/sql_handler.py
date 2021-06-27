import sqlite3
from typing import List
from .handler import Handler
from .log_entry import LogEntry


class SQLHandler(Handler):
    def __init__(self, file: str) -> None:
        super().__init__(file)

    def _create_table(self, cursor) -> None:
        command = """CREATE TABLE IF NOT EXISTS logs(
            date text,
            level text, 
            msg text
        );"""
        cursor.execute(command)

    def save(self, log) -> None:
        create_logs = """INSERT INTO logs(date, level, msg)
                        VALUES(?, ?, ?)"""
        with sqlite3.connect(self.file) as conn:
            cursor = conn.cursor()
            self._create_table(cursor)
            logs = (log.date, log.level, log.msg)
            cursor.execute(create_logs, logs)
            conn.commit()
            cursor.close()

    def retrieve(self) -> List[LogEntry]:
        select = """SELECT * FROM logs"""
        with sqlite3.connect(self.file) as conn:
            cursor = conn.cursor()
            cursor.execute(select)
            logs = [LogEntry(*entry) for entry in cursor]
        return logs

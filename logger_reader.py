import re
from datetime import datetime
from typing import Optional


class ProfilLoggerReader(object):
    date = 0
    level = 1
    msg = 2

    def __init__(self, handler) -> None:
        self.handler = handler

    def _check_date(self, date: str, start_date: datetime) -> bool:
        if start_date is not None:
            to_datetime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
            if to_datetime > start_date:
                return True
            return False
        return True

    def find_by_text(self, text: str, start_date: Optional[datetime] = None):
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if text in log[self.msg]
            and self._check_date(log[self.date], start_date)]
        print(filtered_logs)

    def find_by_regex(self, regex: str, start_date: Optional[datetime] = None):
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if bool(re.search(regex, log[self.msg]))]
        print(filtered_logs)

    def groupby_level(self):
        pass

    def groupby_month(self):
        pass

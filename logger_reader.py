import re
from datetime import datetime
from itertools import groupby
from operator import itemgetter
from typing import Dict, List, Optional
from log_entry import LogEntry


class ProfilLoggerReader(object):
    date = 0
    level = 1
    msg = 2

    def __init__(self, handler) -> None:
        self.handler = handler

    def _range_start(self, date: str, start_date: datetime) -> bool:
        if start_date is not None:
            to_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            if  to_datetime >= start_date:
                return True
            return False
        return True

    def _range_end(self, date: str, end_date: datetime) -> bool:
        if end_date is not None:
            to_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            if  to_datetime <= end_date:
                return True
            return False
        return True

    def find_by_text(self, text: str, start_date: Optional[datetime] = None):
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if text in log[self.msg]
            and self._range_start(log[self.date], start_date)]
        print(filtered_logs)

    def find_by_regex(self, regex: str, start_date: Optional[datetime] = None):
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if bool(re.search(regex, log[self.msg]))
            and self._range_start(log[self.date], start_date)]
        print(filtered_logs)

    def groupby_level(self, start_date: Optional[datetime] = None,
                      end_date: Optional[datetime] = None) -> None:
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if self._range_start(log[self.date], start_date) 
            and self._range_end(log[self.date], end_date)]
        sorted_logs = sorted(filtered_logs, key=itemgetter(1))
        result = {}
        for key, group in groupby(sorted_logs, itemgetter(1)):
            result[key] = list(group)
        print(result)

    def groupby_month(self):
        pass

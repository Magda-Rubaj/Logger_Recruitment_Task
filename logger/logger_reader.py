import re
from datetime import datetime
from itertools import groupby
from typing import Dict, List, Optional
from log_entry import LogEntry


class ProfilLoggerReader(object):

    def __init__(self, handler) -> None:
        self.handler = handler

    def _check_date(self, date: str, start_date: datetime, end_date: datetime) -> bool:
        to_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        if end_date is None and start_date is None:
            return True  
        elif end_date is None:
            return to_datetime >= start_date
        elif start_date is None:
            return to_datetime <= end_date
        if end_date < start_date:
            raise ValueError("Wrong dates order")
        return (to_datetime <= end_date and to_datetime >= start_date)
       
    def find_by_text(self, text: str, start_date: Optional[datetime] = None,
                     end_date: Optional[datetime] = None) -> List[LogEntry]:
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if text in log.msg
            and self._check_date(log.date, start_date, end_date)]
        return filtered_logs

    def find_by_regex(self, regex: str, start_date: Optional[datetime] = None,
                      end_date: Optional[datetime] = None) -> List[LogEntry]:
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if bool(re.search(regex, log.msg))
            and self._check_date(log.date, start_date, end_date)]
        return filtered_logs

    def groupby_level(self, start_date: Optional[datetime] = None,
                      end_date: Optional[datetime] = None) -> Dict[str, List[LogEntry]]:
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if self._check_date(log.date, start_date, end_date)]
        sorted_logs = sorted(filtered_logs, key=lambda x: x.level)
        result = {}
        for key, group in groupby(sorted_logs, lambda x: x.level):
            result[key] = list(group)
        return result

    def groupby_month(self, start_date: Optional[datetime] = None,
                      end_date: Optional[datetime] = None) -> Dict[str, List[LogEntry]]:
        all_logs = self.handler.retrieve()
        filtered_logs = [
            log for log in all_logs if self._check_date(log.date, start_date, end_date)]
        sorted_logs = sorted(filtered_logs, key=lambda x: x.get_month())
        result = {}
        for key, group in groupby(sorted_logs, lambda x: x.get_month()):
            result[key] = list(group)
        return result

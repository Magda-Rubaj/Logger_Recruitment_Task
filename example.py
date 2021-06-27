from logger.csv_handler import CSVHandler
from logger.json_handler import JsonHandler
from logger.sql_handler import SQLHandler
from logger.file_handler import FileHandler
from logger.logger_reader import ProfilLoggerReader
from logger.profil_logger import ProfilLogger
from datetime import datetime

json_handler = JsonHandler("logs.json")
csv_handler = CSVHandler("logs.csv")
sql_handler = SQLHandler("logs.sqlite")
file_handler = FileHandler("logs.txt")

logger = ProfilLogger(handlers=[json_handler, csv_handler, sql_handler, file_handler])
logger.info("Some message")
log_reader = ProfilLoggerReader(handler=file_handler)
start = datetime(2021, 6, 27, 23, 59, 1)
end = datetime(2021, 6, 28, 0, 1, 10)
print(log_reader.groupby_level(end_date=end))
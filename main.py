from csv_handler import CSVHandler
from json_handler import JsonHandler
from sql_handler import SQLHandler
from file_handler import FileHandler
from logger_reader import ProfilLoggerReader
from profil_logger import ProfilLogger
from datetime import datetime

json_handler = JsonHandler("logs.json")
csv_handler = CSVHandler("logs.csv")
sql_handler = SQLHandler("logs.sqlite")
file_handler = FileHandler("logs.txt")

logger = ProfilLogger(handlers=[json_handler, csv_handler, sql_handler, file_handler])
logger.info("Some message")
log_reader = ProfilLoggerReader(handler=file_handler)
start = datetime(2021, 6, 26, 19, 56, 1)
end = datetime(2021, 6, 26, 20, 8, 10)
print(log_reader.groupby_level())

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
logger.info("Some info message")
logger.error("Some error message")
logger.debug("Some debug message")
logger.set_log_level("WARNING")
logger.info("Some other info message")
logger.error("Some other error message")

log_reader = ProfilLoggerReader(handler=csv_handler)
start = datetime(2021, 6, 28, 2, 35, 1) #enter dates to match your logs
end = datetime(2021, 6, 28, 2, 38, 1)
print(log_reader.groupby_level())
print(log_reader.groupby_month())
print(log_reader.find_by_text("info", start_date=start)) 
print(log_reader.find_by_regex("[a-g]{1} info", end_date=end)) 
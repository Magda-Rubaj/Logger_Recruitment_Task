from csv_handler import CSVHandler
from json_handler import JsonHandler
from logger_reader import ProfilLoggerReader
from profil_logger import ProfilLogger

json_handler = JsonHandler("logs.json")
csv_handler = CSVHandler("logs.csv")

logger = ProfilLogger(handlers=[json_handler, csv_handler])
logger.info("Some info message")
log_reader = ProfilLoggerReader(handler=json_handler)
log_reader.find_by_text("info message")

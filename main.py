from csv_handler import CSVHandler
from json_handler import JsonHandler
from logger_reader import ProfilLoggerReader
from profil_logger import ProfilLogger

json_handler = JsonHandler("logs.json")
csv_handler = CSVHandler("logs.csv")

logger = ProfilLogger(handlers=[json_handler, csv_handler])
logger.info("Some message")
log_reader = ProfilLoggerReader(handler=json_handler)
log_reader.find_by_regex("[a-g]{1} message")
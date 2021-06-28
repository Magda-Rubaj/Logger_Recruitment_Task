# Logger_Recruitment_Task - Magdalena Rubaj

## Installation

To install the library run:

```bash
python setup.py bdist_wheel

pip install /path/to/wheelfile.whl
```
Python 3.8 is required.

## Logger

To use logger handlers for logging files need to be created:
```bash
json_handler = JsonHandler("logs.json")
csv_handler = CSVHandler("logs.csv")
sql_handler = SQLHandler("logs.sqlite")
file_handler = FileHandler("logs.txt")
```
To create logger object:
```bash
logger = ProfilLogger(handlers=[]) #pass list of handlers as argument
```
By default saving logs starts from DEBUG level. To change minimal log level:
```bash
logger.set_log_level("WARNINIG")
```
To create log:
```bash
logger.info("Some info message") # Works the same way for other levels
```

## Querying saved logs

To create reader object:
```bash
log_reader = ProfilLoggerReader(handler) #pass handler to file, you want to get logs from
```
Filtering logs by text:
```bash
log_reader.find_by_text(text: str, start_date: Optional[datetime], end_date: Optional[datetime])
```
Filtering logs by regex:
```bash
log_reader.find_by_regex(regex: str, start_date: Optional[datetime], end_date: Optional[datetime])
```
Get logs grouped by level:
```bash
log_reader.groupby_level(self, start_date: Optional[datetime], end_date: Optional[datetime])
```
Get logs grouped by month:
```bash
log_reader.groupby_month(self, start_date: Optional[datetime], end_date: Optional[datetime])
```
To see example usage check example.py file.



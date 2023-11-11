import json, dotenv, os


dotenv.load_dotenv(override=True)


COOKIES = json.loads(os.getenv('COOKIES', 'null'))
HEADERS = json.loads(os.getenv('HEADERS', 'null'))

REQ_SLEEP = float(os.getenv('REQ_SLEEP', 0.5))

SHEET_SERVICE = json.loads(os.getenv('SHEET_SERVICE', 'null'))
SHEET_KEY = os.getenv('SHEET_KEY')


if not all((COOKIES, HEADERS, SHEET_SERVICE, SHEET_KEY)):
    raise Exception('SOME CONFIG INIT MISSED!')

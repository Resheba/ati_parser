from config import SHEET_SERVICE, SHEET_KEY

from gspread import service_account_from_dict, Client, Spreadsheet


_gc: Client = service_account_from_dict(SHEET_SERVICE)

SHEET: Spreadsheet = _gc.open_by_key(SHEET_KEY)

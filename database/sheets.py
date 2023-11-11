from .model import Filter
from ._conf import SHEET

from gspread import Worksheet


class FilterSheet:
    worksheet: Worksheet = SHEET.worksheet('filter')
    _start_row: int = 2

    @classmethod
    def get_filter(cls) -> Filter:
        row: map[str | None] = map(
            lambda value: value or None,
            cls.worksheet.row_values(cls._start_row))
        return Filter(*row)
    
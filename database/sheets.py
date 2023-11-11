from .model import Company, Filter
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
    

class CompanySheet:
    worksheet: Worksheet = SHEET.worksheet('company')
    _start_row: int = 2

    @classmethod
    def append_company(
        cls,
        company: Company,
        *,
        name_col: int = 1,
        inn_col: int = 2,
        boss_fname_col: int = 3
    ) -> None:
        row: tuple[str|None] = company.to_row(name_col=name_col, inn_col=inn_col, boss_fname_col=boss_fname_col)
        cls.worksheet.append_row(row)

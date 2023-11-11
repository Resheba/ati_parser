from dataclasses import dataclass


@dataclass(slots=True)
class Company:
    name: str
    inn: str = None
    boss_fname: str = None

    def to_row(
            self, 
            name_col: int = 1,
            inn_col: int = 2,
            boss_fname_col: int = 3
            ) -> tuple[str | None]:
        col_indexes: dict[int, str] = {name_col: self.name, inn_col: self.inn, boss_fname_col: self.boss_fname}
        return tuple(
            col_indexes.get(col) 
            for col in 
            range(1, max(name_col, inn_col, boss_fname_col) + 1)
            )


@dataclass(slots=True)
class Filter:
    alias_id: str | None = None
    auto_number: str | None = None
    balls_limit: int | None = None
    city_id: int | None = None
    contact: str | None = None
    email: str | None = None
    firm_name: str | None = None
    firm_type_id: int | None = None
    from_deletes: bool = False
    from_history: bool = False
    inn: str | None = None
    language: int | None = 0
    phone_number: str | None = None

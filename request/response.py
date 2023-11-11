from requests.models import Response


class Firm:
    def __init__(
            self,
            affiliation_firms_inn: list[str] = None,
            affiliation_firms_names: list[str] = None,
            alias_id: str = None,
            brand: str | None = None,
            city: str = None,
            contacts: list[str] = None,
            firm_type: str = None,
            firm_type_id: int = None,
            name: str = None,
            name_eng: str = None,
            name_rus: str = None,
            rating: int = None,
            search_source: int = None,
            **kwargs
            ) -> None:
        self.affiliation_firms_inn: list[str] = affiliation_firms_inn
        self.affiliation_firms_names: list[str] = affiliation_firms_names
        self.alias_id: str = alias_id
        self.brand: str | None = brand
        self.city: str = city
        self.contacts: list[str] = contacts
        self.firm_type: str = firm_type
        self.firm_type_id: int = firm_type_id
        self.name: str = name
        self.name_eng: str = name_eng
        self.name_rus: str = name_rus
        self.rating: int = rating
        self.search_source: int = search_source
        self.extra: dict = kwargs
    
    def __str__(self) -> str:
        return f"Firm({self.name}, contacts_len={len(self.contacts or ())})"
    
    def __repr__(self) -> str:
        return self.__str__()
    

class QueryMetaData:
    def __init__(self, total_count: int = None, **kwargs) -> None:
        self.total_count: int = total_count
        self.extra: dict = kwargs

    def __str__(self) -> str:
        return f"Query(tc={self.total_count}, e={self.extra})"
    
    def __repr__(self) -> str:
        return self.__str__()


class SearchResponse:
    firms: tuple[Firm]
    query_meta_data: QueryMetaData

    def __init__(
            self,
            response: Response
            ) -> None:
        self.firms: tuple[Firm] = tuple()
        self.query_meta_data: QueryMetaData = QueryMetaData()

        self.response: Response = response
        self.parse(response=response)

    def parse(self, response: Response) -> None:
        self.data: dict = response.json()
        if response.status_code == 200:

            if self.data:
                self.firms: tuple[Firm] = tuple(
                    Firm(**kwargs) 
                    for kwargs in self.data.get('firms', tuple())
                    )
                self.query_meta_data: QueryMetaData = QueryMetaData(**self.data.get('query_meta_data', dict()))
    
    def __str__(self) -> str:
        return f"SearchResponse({self.response}, {self.firms}, {self.query_meta_data})"
        
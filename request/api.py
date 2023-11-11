from .session import APISession
from .response import SearchResponse

from requests import Response


class ATIApi:
    _session: APISession = APISession()
    _search_url: str = 'https://ati.su/webapi/extendedsearch/v1/firms/advanced'
    _offset_max: int = 10e2

    @classmethod
    def search(
       cls,
       /,
       alias_id: str | None = None,
       auto_number: str | None = None,
       balls_limit: int | None = None,
       city_id: int | None = None,
       contact: str | None = None,
       email: str | None = None,
       firm_name: str | None = None,
       firm_type_id: int | None = None,
       from_deletes: bool = False,
       from_history: bool = False,
       inn: str | None = None,
       language: int | None = 0,
       phone_number: str | None = None,
       offset: int = 0,
       limit: int = 100
    ) -> SearchResponse:
        response: Response = cls._session.post(
            url=cls._search_url,
            params=cls._params(offset=offset, limit=limit),
            json=dict(alias_id=alias_id, auto_number=auto_number, balls_limit=balls_limit, city_id=city_id,
                    contact=contact, email=email, firm_name=firm_name, firm_type_id=firm_type_id,
                    from_deletes=from_deletes, from_history=from_history, inn=inn, language=language,
                    phone_number=phone_number)
        )
        search_reasponse: SearchResponse = SearchResponse(response=response)
        if search_reasponse.query_meta_data.total_count:
            if search_reasponse.query_meta_data.total_count > len(search_reasponse.firms) and offset < cls._offset_max:
                search_reasponse.firms += cls.search(alias_id=alias_id, auto_number=auto_number, balls_limit=balls_limit, city_id=city_id,
                                                    contact=contact, email=email, firm_name=firm_name, firm_type_id=firm_type_id,
                                                    from_deletes=from_deletes, from_history=from_history, inn=inn, language=language,
                                                    phone_number=phone_number, offset=offset+limit, limit=limit).firms
        return search_reasponse                

    @staticmethod
    def _params(
        offset: int = 0,
        limit: int = 100
    ) -> dict[str, int]:
        return dict(offset=offset, limit=limit)
    
    # @staticmethod
    # def json_data(
    #    alias_id: str | None = None,
    #    auto_number: str | None = None,
    #    balls_limit: int | None = None,
    #    city_id: int | None = None,
    #    contact: str | None = None,
    #    email: str | None = None,
    #    firm_name: str | None = None,
    #    firm_type_id: int | None = None,
    #    from_deletes: bool = False,
    #    from_history: bool = False,
    #    inn: str | None = None,
    #    language: int | None = 0,
    #    phone_number: str | None = None
    # ) -> dict:
    #     return dict(alias_id=alias_id, auto_number=auto_number, balls_limit=balls_limit, city_id=city_id,
    #                 contact=contact, email=email, firm_name=firm_name, firm_type_id=firm_type_id,
    #                 from_deletes=from_deletes, from_history=from_history, inn=inn, language=language,
    #                 phone_number=phone_number)
    
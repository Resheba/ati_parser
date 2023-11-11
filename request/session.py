from config import REQ_SLEEP, COOKIES, HEADERS

import time
from typing import Any
from requests import Session
from requests.models import Response


class APISession(Session):
    '''
    Descendant of the Session class

    But with `sleep` before `get` and `post` methods
    '''
    def get(self, url: str | bytes, *, params: Any | None = None, data: Any | None = None, headers: Any | None = None, cookies: Any | Any | None = None, files: Any | None = None, auth: Any | None = None, timeout: Any | None = None, allow_redirects: bool = None, proxies: Any | None = None, hooks: Any | None = None, stream: bool | None = None, verify: Any | None = None, cert: Any | None = None, json: dict | None = None
            ) -> Response:
        time.sleep(REQ_SLEEP)

        headers: dict = headers or HEADERS
        cookies: dict = cookies or COOKIES
        
        response: Response = super().get(url, params=params, data=data, headers=headers, cookies=cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert, json=json)
        return response

    def post(self, url: str | bytes, data: Any | None = None, json: dict | None = None, *, params: Any | None = None, headers: Any | None = None, cookies: Any | Any | None = None, files: Any | None = None, auth: Any | None = None, timeout: Any | None = None, allow_redirects: bool = None, proxies: Any | None = None, hooks: Any | None = None, stream: bool | None = None, verify: Any | None = None, cert: Any | None = None
             ) -> Response:
        time.sleep(REQ_SLEEP)

        headers: dict = headers or HEADERS
        cookies: dict = cookies or COOKIES

        response: Response = super().post(url, data, json, params=params, headers=headers, cookies=cookies, files=files, auth=auth, timeout=timeout, allow_redirects=allow_redirects, proxies=proxies, hooks=hooks, stream=stream, verify=verify, cert=cert)
        return response
    
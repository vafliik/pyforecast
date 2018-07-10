from typing import Dict, Optional, Tuple
from timeit import default_timer as timer

import requests
import requests_cache

requests_cache.install_cache(cache_name='forecast_cache', backend='sqlite', expire_after=180)


class Requestor:

    def __init__(self, account_id, auth_token, base_url=None):
        self._account_id = account_id
        self._auth_token = auth_token
        if base_url is None:
            self._base_url = "https://api.forecastapp.com"

        self._headers = {
            'Forecast-Account-ID': self._account_id,
            'Authorization': 'Bearer {}'.format(self._auth_token),
            'User-Agent': 'Forecast Harvest Python API',
        }


    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        start = timer()
        r = requests.get("{}/{}".format(self._base_url, endpoint), headers=self._headers)
        end = timer()
        print("GET: {0} | Time: {1} | Cache: {2}".format(endpoint, end - start, r.from_cache, ))
        return r.json()

    def post(self, endpoint: str, params: Optional[Dict] = None) -> Tuple[Dict, int, str]:
        start = timer()
        r = requests.post("{}/{}".format(self._base_url, endpoint), headers=self._headers, json=params)
        end = timer()
        print("POST: {0} | Time: {1} | Cache: {2}".format(endpoint, end - start, r.from_cache, ))
        return r.json(), r.status_code, r.text

    @staticmethod
    def clear_cache():
        requests_cache.clear()

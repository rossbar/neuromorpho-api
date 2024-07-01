from urllib3.util import create_urllib3_context
from urllib3 import PoolManager
from requests.adapters import HTTPAdapter
from requests import Session

import warnings


warnings.filterwarnings("always")
warnings.warn(
    (
        "\n\nThe neuromorpho_api package is no longer needed to access neuromorpho.org\n"
        "data from Python. Use `requests` directly instead."
    ),
    DeprecationWarning,
)


__all__ = ["requestor"]

_baseurl = "https://neuromorpho.org"

class _AddedCipherAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = create_urllib3_context(ciphers=":HIGH:!DH:!aNULL")
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize, block=block, ssl_context=ctx
        )


requestor = Session()
requestor.mount(_baseurl, _AddedCipherAdapter())

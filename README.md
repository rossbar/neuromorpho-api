neuromorpho-api
===============

Querying the [neuromorpho.org](https://neuromorpho.org/) database in Python
with [requests](https://pypi.org/project/requests/).

```{admonition} Update: 05-2024

As of May 2024, the SSL key for neuromorpho.org has been updated, and the
workaround packaged here is no longer necessary!
The [requests](https://pypi.org/project/requests/) package can now be used
directly with the neuromorpho.org API.
This project will be archived, though the documentation will remain live and
updated to demonstrate programmatic access of neuromorpho data.
```

## Quickstart

```python
>>> import requests

>>> neuron_endpoint = "https://neuromorpho.org/api/neuron/"
>>> resp = requests.get(neuron_endpoint + "fields")
>>> resp.json()
{'Neuron Fields': ['neuron_id',
  'neuron_name',
  'archive',
  'age_scale',
  'gender',
  ...
```

See the tutorial for more detailed examples, including
[selecting neurons by attribute pattern matching][nmapi-selection] and
[downloading SWC traces][nmapi-swc].

[nmapi-selection]: https://neuromorpho-api.readthedocs.io/en/latest/tutorial.html#neuron-query
[nmapi-swc]: https://neuromorpho-api.readthedocs.io/en/latest/tutorial.html#neuron-traces

---

## What ~~is~~ was this package?

The `neuromorpho-api` package provides a `requests.Session` instance with a
custom `SSLContext` needed for interacting with
[neuromorpho.org](https://neuromorpho.org/).

### Why can't I just use `requests` directly?

#### NOTE: should no longer be an issue as of 05-24

You may see something like the following:

```python
>>> import requests
>>> requests.get("https://neuromorpho.org/api/neuron/id/1")
Traceback (most recent call last)
   ...
SSLError: HTTPSConnectionPool(host='neuromorpho.org', port=443): Max retries exceeded with url: /api/neuron/id/1 (Caused by SSLError(SSLError(1, '[SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:1006)')))
```

It appears the key provided by `neuromorpho.org` is incompatible with the
default Python SSL cipher.
This package works around this issue using [Robin De Schepper's solution
posted on Stack Overflow](https://stackoverflow.com/a/76217135).
At some point in the future, the neuromorpho certificate may (hopefully) be
updated, at which point this package will be archived.

### Future compatibility

The `requestor` provided by this package is intended as a temporary workaround
for the current DH key issue with neuromorpho.org.
If the neuromorpho.org certificate is updated, the `requestor` with the custom
SSLContext will no longer be necessary, and users can switch to using
`requests` directly.
Therefore, the following import alias is recommended:

```python
from neuromorpho-api import requestor as requests
```

With an updated certificate, the above can be changed to:

```python
import requests
```

and all code that depends on `requests.get` should continue to work as expected.

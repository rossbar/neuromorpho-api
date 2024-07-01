---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Tutorial

A quick runthrough demonstrating basic API queries.

```{code-cell}
import requests
```

## Neuron metadata

Let's start in the same place as the [neuromorpho.org API reference docs][nm-id]:
grabbing metadata for a single neuron by neuron id.

```{code-cell}
:tags: [hide-output]
endpoint = "https://neuromorpho.org/api/"
r = requests.get(endpoint + "neuron/id/1")
# Check that the status_code is 200 and raise if not
r.raise_for_status()
data = r.json()
data
```

[nm-id]: https://neuromorpho.org/apiReference.html#neuron-id

## Neuron query

In practice, it is unlikely you will know the neuromorpho id(s) of the
neuron(s) you're interested in.
This is where `requests` really comes in handy, allowing you to
[specify the parameters supported by the neuromorpho api][nm-params] with
Python dictionaries.

For example, let's construct a query to select all neurons by name from a
single image in the Siegert archive:

```{code-cell}
# Neuron name - note the `*` wildcard to select all neurons whose name matches
# this pattern
siegert_dataset = "CB_CKp25_2w_F_Animal01_*"

# The GET parameters
query_params = {"q": f"neuron_name:{siegert_dataset}"}

r = requests.get(endpoint + "neuron/select/", params=query_params)
# We let requests handle the URL construction
r.url
```

The data for multiple neurons is returned in the form of a nested dict from
which individual neuron metadata can be extracted.

```{code-cell}
r.raise_for_status()  # Make sure the request was successful
data = r.json()["_embedded"]["neuronResources"]
f"Number of neurons matching query: {len(data)}"
```
```{code-cell}
# Individual neuron names
sorted(record["neuron_name"] for record in data)
```

[nm-params]: https://neuromorpho.org/apiReference.html#neuron-query

## Neuron traces

Up to this point, we've only demonstrated how to extract the neuron metadata
available via the neuromorpho API.

Individual SWC traces are also accessible via `GET` request, albeit from
different URLs.

```{note}
Accessing SWC files does not appear to be part of the public neuromorpho API,
so the recipe below may not generalize to all datasets. It should however
give you a rough idea of how the data appear to be organized.
```

The general form of URLs for the SWC data include three parameters:

1. The archive name
2. The data version (e.g. `Source-Version` or `CNG version` for original or
   standardized versions, respectively), and
3. The neuron name

Items 1 and 3 can be extracted from the neuron metadata, while item 2 specifies
which version of SWC file you want.

Let's return to our previous query of the Seigert data and download the SWC
data for one of the neurons.

Let's start by codifying the above with a string template:

```{code-cell}
import random
import string

# A general-ish URL template for accessing SWC data
swc_url_template = string.Template(
    "https://neuromorpho.org/dableFiles/$archive/$version/$fname.swc"
)
```

Then we'll arbitrarily select one of the neurons from the previous query for
our example, and construct SWC url:

```{code-cell}
record = random.choice(data)
record["neuron_name"]
```

```{code-cell}
# Construct the SWC URL for the original (source) version of this specific neuron
swc_url = swc_url_template.substitute(
    archive=record["archive"].lower(),
    version="Source-Version",
    fname=record["neuron_name"],
)
swc_url
```

Finally, we download the data. Note the `raise_for_status` is particularly
helpful here to catch issues with our URL template.

```{code-cell}
r = requests.get(swc_url)
r.raise_for_status()
```

If all went well, the SWC data should be available in the response's `content`
as a byte-string:

```{code-cell}
import io
import pandas as pd

raw_data = io.BytesIO(r.content)
df = pd.read_csv(raw_data, delimiter=" ")
df
```


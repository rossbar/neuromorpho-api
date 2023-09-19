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

# Examples

The [neuromorpho.org API reference](https://neuromorpho.org/apiReference.html)
provides examples for accessing neuron and publication data via the API using
`curl`.

We repeat those examples here, showing how to use `requests` instead.
There are four public API endpoints: `neuron`, `literature`, `morphometry`, and
`pvec` which provide access to neuron metadata, publication metadata, neuron
morphometry, and neuron persistence vectors, respectively.

## Neuron

```{code-cell}
from neuromorpho_api import requestor as requests
neuron_endpoint = "https://neuromorpho.org/api/neuron"
```

### All neurons

```{note}
We won't actually run this one, as it is an expensive query returning more than
80k neuron records.
```

```python
r = requests.get(neuron_endpoint)
```

### Neuron by id or name

Neurons can be requested by id:

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((neuron_endpoint, "id/1")))
r.raise_for_status()
r.json()
```

or by name:

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((neuron_endpoint, "name/cnic_001")))
r.raise_for_status()
r.json()
```

### Custom selection query

Query strings are denoted by the `q` parameter. The general syntax for query
parameters is: `{neuron_field_name}:{comma-separated criteria}`.

See the official [API docs](https://neuromorpho.org/apiReference.html#neuron-query)
for details.

```{code-cell}
:tags: [hide-output]
# Query all neurons from cats
params = {"q": "species:cat"}
r = requests.get("/".join((neuron_endpoint, "select")), params=params)
r.raise_for_status()

# Show only the pagination, for brevity's sake
r.json()
```

### Filter queries

Selection queries can include filters with the `fq` parameter.
A query can included multiple filters:

```{code-cell}
:tags: [hide-output]
params = {
    "q": "species:cat,rat,monkey",
    "fq": [  # Additional filters
        "stain:lucifer yellow",
        "brain_region:layer 3",
        "strain:Macaque",
    ],
}
r = requests.get("/".join((neuron_endpoint, "select")), params=params)
print(f"Target URL:\n  {r.url}")
r.raise_for_status()
r.json()
```

### Neuron fields

The listing of all neuron fields can be queried:

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((neuron_endpoint, "fields")))
r.raise_for_status()
r.json()
```

### Neuron field values

Valid values for a given field:

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((neuron_endpoint, "fields/species")))
r.raise_for_status()
r.json()
```

### Neuron field partitioning

Returns a listing of the number of neurons per each value in a given field.
For instance, to view the total number of neurons by species:

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((neuron_endpoint, "partition/species")))
r.raise_for_status()
r.json()
```

## Literature

```{code-cell}
pub_endpoint = "https://neuromorpho.org/api/literature"
```

### All publications

```{note}
We won't actually run this one, as it is an expensive query returning nearly
32k records.
```

```python
r = requests.get(pub_endpoint)
```

% ### Publication by article ID
% 
% ```{code-cell}
% :tags: [hide-output]
% r = requests.get("/".join((pub_endpoint, "id/56e9c95de4b0355017b314d2")))
% r.raise_for_status()
% r.json()
% ```

### Publication select query

```{code-cell}
:tags: [hide-output]
# Query all publications involving neurons from cats
params = {"q": "species:mouse"}
r = requests.get("/".join((pub_endpoint, "select")), params=params)
r.raise_for_status()
r.json()
```

### Literature fields

Query all available literature fields

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((pub_endpoint, "fields")))
r.raise_for_status()
r.json()
```

### Literature field values

Query valid values for a given field

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((pub_endpoint, "fields/tracingSystem")))
r.raise_for_status()
r.json()
```

### Literature field partitions

The number of publications for each value in a literature field

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((pub_endpoint, "partition/tracingSystem")))
r.raise_for_status()
r.json()
```

## Morphometry

```{code-cell}
morph_endpoint = "https://neuromorpho.org/api/morphometry"
```

### Morphometry data for all neurons

```{note}
We won't actually run this one, as it is an expensive query returning over 80k
records.
```

```python
r = requests.get(morph_endpoint)
```

### Morphometry by neuron id or name

```{code-cell}
:tags: [hide-output]
# By neuron id
r = requests.get("/".join((morph_endpoint, "id/1")))
r.raise_for_status()

# By neuron name
r = requests.get("/".join((morph_endpoint, "name/cnic_001")))
r.raise_for_status()
r.json()
```

## Persistence vectors

```{code-cell}
pvec_endpoint = "https://neuromorpho.org/api/pvec"
```

### Persistence vectors for all neurons

```{note}
We won't actually run this one, as it is an expensive query returning over 100k
records.
```

```python
r = requests.get(pvec_endpoint)
```

### By neuron id

```{code-cell}
:tags: [hide-output]
r = requests.get("/".join((pvec_endpoint, "id/1")))
r.raise_for_status()
r.content.decode()
```

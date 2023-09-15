"""
Tests for the ``requestor`` object: a ``requests.Session`` with a custom
SSLContext.

These are essentially smoke tests, i.e. we're testing for the absence of
``SSLError`` exceptions.

NOTE: These tests actually make GET requests to the server! Good citizenship
dictates the tests should be run sparingly.
"""
from neuromorpho_api import requestor


def test_neuron_endpoint():
    resp = requestor.get("https://neuromorpho.org/api/neuron/fields")
    assert resp.status_code == 200
    assert "Neuron Fields" in resp.json()

"""
Tests for the ``requestor`` object: a ``requests.Session`` with a custom
SSLContext.

These are essentially smoke tests, i.e. we're testing for the absence of
``SSLError`` exceptions.

NOTE: These tests actually make GET requests to the server! Good citizenship
dictates the tests should be run sparingly.
"""
import warnings
import pytest
import requests
from requests.exceptions import SSLError


@pytest.mark.xfail
def test_neuron_endpoint():

    with warnings.catch_warnings():
        from neuromorpho_api import requestor

    resp = requestor.get("https://neuromorpho.org/api/neuron/fields")
    assert resp.status_code == 200
    assert "Neuron Fields" in resp.json()


def test_default_ssl_context():
    """
    This is expected to pass so long as the DH key for the neuromorpho.org cert
    is valid.
    """
    resp = requests.get("https://neuromorpho.org/api/neuron/fields")

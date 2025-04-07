from rest_framework.test import APIClient
import pytest

def test_home_returns_200():

    client = APIClient()
    response = client.get('http://127.0.0.1:8000/')
    assert response.status_code == 200
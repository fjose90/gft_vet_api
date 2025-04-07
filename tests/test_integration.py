from rest_framework.test import RequestsClient
import pytest


@pytest.mark.django_db
def test_home_returns_200():

    client = RequestsClient()
    response = client.get('http://127.0.0.1:8000/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'Bem vindo a API da Clínica Veterinária'}

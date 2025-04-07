from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
def test_home_returns_400():

    client = APIClient()
    response = client.get('/')
    assert response.status_code == 400

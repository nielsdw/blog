import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_jwt(client):
    client = APIClient()
    User.objects.create_user(username="foo", password="bar")
    response = client.post("/api/token/",
                           {"username": "foo",
                            "password": "bar"
                            },
                           format='json'
                           )
    assert response.status_code == 200
    assert response.data["access"] is not None
    assert response.data["refresh"] is not None

    response = client.get('/blogs')
    assert response.status_code == 401  # Unauthorized

    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data["access"])

    response = client.get('/blogs')
    assert response.status_code == 200

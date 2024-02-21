from django.urls import reverse


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_get_rate_list(client):
    response = client.get(reverse('rate-list'))
    assert response.status_code == 200

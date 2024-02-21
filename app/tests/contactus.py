from django.urls import reverse
from django.conf import settings

from currency.models import ContactUs


def test_post_contact_us_empty_form_200(client):
    response = client.post(reverse('contactus-create'))
    assert response.status_code == 200


def test_post_contact_us_empty_form_errors(client):
    response = client.post(reverse('contactus-create'))
    assert response.context_data['form'].errors == {
        'name': ['This field is required.'],
        'email_from': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


def test_post_contact_us_invalid_email(client):
    payload = {
        'name': 'Name',
        'email_from': 'INVALID_EMAIL',
        'subject': 'Subject',
        'message': 'Body',
    }
    response = client.post(reverse('contactus-create'), data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_from': ['Enter a valid email address.']
    }


def test_post_contact_us_valid_data(client, mailoutbox):
    initial_count = ContactUs.objects.count()
    payload = {
        'name': 'Name',
        'email_from': 'email@example.com',
        'subject': 'Subject',
        'message': 'Body',
    }
    response = client.post(reverse('contactus-create'), data=payload)
    assert response.status_code == 302
    assert response.headers['Location'] == '/currency/contactus/list/'
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
    assert ContactUs.objects.count() == initial_count + 1

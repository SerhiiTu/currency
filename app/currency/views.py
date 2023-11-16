from django.shortcuts import render
from django.http.response import HttpResponse
from currency.models import Rate, ContactUs


# Create your views here.
def rate_list(request):
    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, TYPE: {rate.type}, BUY: {rate.buy}, SELL: {rate.sell}, SOURCE: {rate.source}, CREATED: {rate.created}</br>')

    return HttpResponse(str(results))


def contactus_list(request):
    results = []
    messages = ContactUs.objects.all()

    for message in messages:
        results.append(
            f'ID: {message.id}, EMAIL: {message.email_from}, SUBJECT: {message.subject}, MESSAGE: {message.message}</br>')

    return HttpResponse(str(results))

from django.shortcuts import render
from currency.models import Rate, ContactUs


# Create your views here.
def rate_list(request):
    rates = Rate.objects.all()
    context = {
        "rates": rates
    }

    return render(request, 'rate_list.html', context)


def contactus_list(request):
    messages = ContactUs.objects.all()

    context = {
        "messages": messages
    }

    return render(request, 'contactus_list.html', context)

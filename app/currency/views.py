from django.shortcuts import render, get_object_or_404
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm
from django.http.response import HttpResponseRedirect


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


def source_list(request):
    sources = Source.objects.all()
    context = {
        "sources": sources
    }

    return render(request, 'source_list.html', context)


def rate_create(request):
    if request.method == "POST":
        form = RateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    else:
        form = RateForm()

    context = {
        "form": form
    }

    return render(request, 'rate_create.html', context)


def rate_update(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    if request.method == "POST":
        form = RateForm(data=request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    else:
        form = RateForm(instance=rate)

    context = {
        "form": form
    }

    return render(request, 'rate_create.html', context)


def rate_delete(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    if request.method == "GET":
        context = {
            "rate": rate
        }

        return render(request, 'rate_delete.html', context)
    elif request.method == "POST":
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def rate_retrieve(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    context = {
        "rate": rate
    }

    return render(request, 'rate_retrieve.html', context)


def source_create(request):
    if request.method == "POST":
        form = SourceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    else:
        form = SourceForm()

    context = {
        "form": form
    }

    return render(request, 'source_create.html', context)


def source_update(request, pk):
    source = get_object_or_404(Source, id=pk)

    if request.method == "POST":
        form = SourceForm(data=request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    else:
        form = SourceForm(instance=source)

    context = {
        "form": form
    }

    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, id=pk)

    if request.method == "GET":
        context = {
            "source": source
        }

        return render(request, 'source_delete.html', context)
    elif request.method == "POST":
        source.delete()
        return HttpResponseRedirect('/source/list/')


def source_retrieve(request, pk):
    source = get_object_or_404(Source, id=pk)

    context = {
        "source": source
    }

    return render(request, 'source_retrieve.html', context)

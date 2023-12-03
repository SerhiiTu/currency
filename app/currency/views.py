from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy("rate-list")


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy("contactus-list")


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy("source-list")


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy("rate-list")


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy("contactus-list")


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy("source-list")
    model = Source


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy("rate-list")


class ContactUsDeleteView(DeleteView):
    model = ContactUs
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy("contactus-list")


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy("source-list")


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_retrieve.html'


class ContactUsDetailView(DetailView):
    model = ContactUs
    template_name = 'contactus_retrieve.html'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_retrieve.html'


class IndexView(TemplateView):
    template_name = "index.html"

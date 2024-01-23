from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactUsForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
import re
from django_filters.views import FilterView
from currency.filters import RateFilter, ContactUsFilter, SourceFilter

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from currency.tasks import send_mail_in_background


class RateListView(FilterView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'
    paginate_by = 20
    filterset_class = RateFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        query_parameters = self.request.GET.urlencode()

        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context


class ContactUsListView(FilterView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'
    paginate_by = 20
    filterset_class = ContactUsFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        query_parameters = self.request.GET.urlencode()

        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context


class SourceListView(FilterView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'
    paginate_by = 20
    filterset_class = SourceFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        query_parameters = self.request.GET.urlencode()

        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy("rate-list")


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy("contactus-list")

    def _send_email(self):
        subject = "User contact Us"
        body = f'''
                Name: {self.object.name}
                Email: {self.object.email_from}
                Subject: {self.object.subject}
                Message: {self.object.message}
                '''

        send_mail_in_background(subject, body)  # поки вимкнув

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()

        return redirect


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy("source-list")


class RateUpdateView(UserPassesTestMixin, UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy("rate-list")

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy("contactus-list")


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy("source-list")
    model = Source


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy("rate-list")

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsDeleteView(DeleteView):
    model = ContactUs
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy("contactus-list")


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy("source-list")


class RateDetailView(LoginRequiredMixin, DetailView):
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

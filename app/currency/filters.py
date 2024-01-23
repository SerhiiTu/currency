import django_filters

from currency.models import Rate, ContactUs, Source


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ['exact'],
            'sell': ['exact'],
            'rate_type': ['exact']
        }


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {
            'name': ['contains', 'exact'],
            'email_from': ['startswith', 'exact'],
            'subject': ['contains', 'exact'],
            'message': ['contains', 'exact'],
        }


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = {
            'name': ['contains', 'exact'],
            'source_type': ['exact'],
            'source_url': ['contains', 'exact'],
        }

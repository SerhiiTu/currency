from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from currency.api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.api.paginators import RatePagination, SourcePagination, ContactUsPagination
from currency.api.throtling import RateThrottle
from currency.filters import RateFilter, SourceFilter, ContactUsFilter
from currency.models import Rate, Source, ContactUs


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = ('buy', 'sell', 'created')
    throttle_classes = (RateThrottle,)


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    pagination_class = SourcePagination
    filterset_class = SourceFilter
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = ('name', 'source_type')
    throttle_classes = (RateThrottle,)


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    pagination_class = ContactUsPagination
    filterset_class = ContactUsFilter
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = ('name', 'email_from', 'subject', 'message')
    throttle_classes = (RateThrottle,)

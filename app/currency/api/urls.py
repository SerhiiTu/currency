from django.urls import path
from rest_framework import routers

from currency.api.views import RateViewSet, SourceListAPIView, ContactUsViewSet

app_name = 'currency_api'

router_rate = routers.SimpleRouter(trailing_slash=True)
router_rate.register(r'rates', RateViewSet, basename='api-rate')

router_contactus = routers.SimpleRouter(trailing_slash=True)
router_contactus.register(r'contactus', ContactUsViewSet, basename='api-contactus')

urlpatterns = [
                  path('sources/', SourceListAPIView.as_view(), name='api-source-list'),
              ] + router_rate.urls + router_contactus.urls

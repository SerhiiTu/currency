from django.urls import path

from currency.views import (
    RateListView, ContactUsListView, SourceListView, RateCreateView, ContactUsCreateView, SourceCreateView,
    RateUpdateView, ContactUsUpdateView, SourceUpdateView, RateDeleteView, ContactUsDeleteView, SourceDeleteView,
    RateDetailView, ContactUsDetailView, SourceDetailView,
)

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('contactus/list/', ContactUsListView.as_view(), name='contactus-list'),
    path('source/list/', SourceListView.as_view(), name='source-list'),

    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/retrieve/<int:pk>/', RateDetailView.as_view(), name='rate-retrieve'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus-update'),
    path('contactus/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contactus-delete'),
    path('contactus/retrieve/<int:pk>/', ContactUsDetailView.as_view(), name='contactus-retrieve'),

    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/retrieve/<int:pk>/', SourceDetailView.as_view(), name='source-retrieve'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),

]

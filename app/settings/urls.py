"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from currency.views import (rate_list,
                            contactus_list,
                            source_list,
                            rate_create,
                            rate_retrieve,
                            rate_update,
                            rate_delete,
                            source_create,
                            source_retrieve,
                            source_update,
                            source_delete,
                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('contactus/list/', contactus_list),
    path('source/list/', source_list),
    path('rate/create/', rate_create),
    path('rate/retrieve/<int:pk>/', rate_retrieve),
    path('rate/update/<int:pk>/', rate_update),
    path('rate/delete/<int:pk>/', rate_delete),
    path('source/create/', source_create),
    path('source/retrieve/<int:pk>/', source_retrieve),
    path('source/update/<int:pk>/', source_update),
    path('source/delete/<int:pk>/', source_delete),

]

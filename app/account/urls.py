from django.urls import path
from account.views import ProfileView, UserSignUpView, UserActivateView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>/', UserActivateView.as_view(), name='user_activate'),
]

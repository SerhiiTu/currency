from django.contrib.auth import get_user_model
from django.views.generic import UpdateView, CreateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import UserForm
from django.urls import reverse_lazy
from account.forms import UserSignUpForm

User = get_user_model()


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        qs = self.get_queryset()

        return qs.get(id=self.request.user.id)


class UserSignUpView(CreateView):
    queryset = User.objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')

        user = User.objects.filter(username=username).first()
        if user is not None:
            user.is_active = True
            user.save()

        return super().get_redirect_url(*args, **kwargs)

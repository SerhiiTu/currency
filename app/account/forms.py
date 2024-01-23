from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'age',
            'phone_number',
        )


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'age',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data: dict = super().clean()

        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords should match!')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.save()

        self._send_email()

        return user

    def _send_email(self):
        activate_path = reverse('user_activate', args=(self.instance.username,))
        subject = 'Thanks for signing up'
        body = f"""
        Follow this link to activate your account:
        {settings.HTTP_METHOD}://{settings.DOMAIN}{activate_path}
        """

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [self.instance.email],
            fail_silently=False,
        )

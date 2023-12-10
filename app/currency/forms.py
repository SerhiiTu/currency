from django import forms

from currency.models import Rate, Source, ContactUs
from django.contrib.auth import get_user_model


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('rate_type',
                  'buy',
                  'sell',
                  'source',
                  )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ('name',
                  'source_type',
                  'source_url',
                  )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name',
                  'email_from',
                  'subject',
                  'message',
                  )


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
                )

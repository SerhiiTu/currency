from django import forms

from currency.models import Rate, Source, ContactUs


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
        fields = (
            'logo',
            'name',
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

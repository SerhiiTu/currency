from django import forms

from currency.models import Rate, Source


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

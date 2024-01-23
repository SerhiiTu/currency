from rest_framework import serializers

from currency.models import Rate, Source, ContactUs

from currency.tasks import send_mail_in_background


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'created',
            'source',
            'rate_type',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'source_type'
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'name',
            'email_from',
            'subject',
            'message',
        )

    def create(self, validated_data):
        create = super().create(validated_data)

        self._send_mail()

        return create

    def _send_mail(self):
        subject = "User contact Us"
        body = f'''
                        Name: {ContactUs.objects.last().name}
                        Email: {ContactUs.objects.last().email_from}
                        Subject: {ContactUs.objects.last().subject}
                        Message: {ContactUs.objects.last().message}
                        '''

        send_mail_in_background(subject, body)

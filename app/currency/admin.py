from django.contrib import admin

from currency.models import Rate, Source, ContactUs, RequestResponseLog


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "rate_type",
        "buy",
        "sell",
        "source",
        "created",
    )

    readonly_fields = (
        "rate_type",
    )

    list_filter = (
        "rate_type",
        "source",
    )


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "source_type",
        "source_url",
    )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email_from",
        "subject",
        "message",
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(RequestResponseLog)
class RequestResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "path",
        "request_method",
        "time",
    )

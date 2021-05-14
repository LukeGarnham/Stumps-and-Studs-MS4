from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'message_date',
    )

    ordering = ('message_date',)


admin.site.register(Contact, ContactAdmin)

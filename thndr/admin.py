from django.contrib import admin

from thndr.models import Account


class AccountAdmin(admin.ModelAdmin):
    search_fields = ("id", "user__pk",)
    list_display = ("id", 'user', "balance")


admin.site.register(Account, AccountAdmin)

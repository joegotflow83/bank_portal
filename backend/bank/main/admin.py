from django.contrib import admin

from .models import Transaction, Account, UserInfo, RejectedInfo


admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(UserInfo)
admin.site.register(RejectedInfo)

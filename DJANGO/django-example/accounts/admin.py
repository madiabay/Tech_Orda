from django.contrib import admin
from accounts import models

# Register your models here.

admin.site.register(models.Account)
admin.site.register(models.Wallet)
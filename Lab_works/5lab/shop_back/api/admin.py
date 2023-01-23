from django.contrib import admin
from api import models


# Register your models here.
admin.site.register(model_or_iterable=models.Product)
admin.site.register(model_or_iterable=models.Category)